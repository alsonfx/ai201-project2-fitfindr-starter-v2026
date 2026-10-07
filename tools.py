"""
The three FitFindr tools.

Each one is a standalone function you can call and test on its own, before any
of them are wired into the loop. Build and test them one at a time — three
untested tools joined by a loop is one problem that looks like six, because you
can't tell which layer is lying to you.

    search_listings(description, size, max_price)  → list[dict]
    suggest_outfit(new_item, wardrobe)             → str
    create_fit_card(outfit, new_item)              → str

All three are stubs right now. They run and they do nothing — that's the
starting position and it's deliberate.

⚠️ Before you write any of them, fill in the **Tool Inventory** section of your
README (Milestone 2). Four lines per tool: what it does, each input with its
type, exactly what it returns, and what it returns when it has nothing to give.
That last line is what your loop branches on. "Returns a list" earns nothing —
the description has to say what is *in* the list.
"""

import config  # noqa: F401 — you'll use this in search_listings
from generate import generate
from utils.data_loader import load_listings


# ── Tool 1: search_listings ───────────────────────────────────────────────────

def search_listings(
    description: str,
    size: str | None = None,
    max_price: float | None = None,
) -> list[dict]:
    """
    Search the listings data for items matching a description, and optionally a
    size and a price ceiling.

    This is the tool that doesn't call the model, which makes it the easiest one
    to test and the one to move onto MCP in unit 4.

    Args:
        description: keywords describing what the user wants
                     (e.g. "vintage graphic tee").
        size:        a size string to filter by, or None to skip size filtering.
                     Match case-insensitively — "M" should match "S/M".

                     ⚠️ Read the sizes in the data before you reach for a plain
                     substring test. `"s" in "us 9"` is True, and so is
                     `"l" in "xl"`. A filter that returns shoes when someone
                     asked for a small top reads like a broken search, and it
                     will quietly cost you in unit 4 when you test criterion 1.
                     What counts as a size match is part of your spec — decide
                     it and write it into your Tool Inventory.
        max_price:   maximum price, inclusive, or None to skip price filtering.

    Returns:
        A list of matching listing dicts, best match first.
        **Returns an empty list when nothing matches — an empty list, not None,
        and not an exception.** Your loop branches on this.

    Each listing dict has these fields:
        id, title, description, category, style_tags (list), size,
        condition, price (float), colors (list), brand (str or None), platform

    Note that `brand` is None for most listings. That is deliberate and
    realistic — thrift listings often have no brand. If something you write
    assumes a brand is always there, you will find out in unit 4.

    TODO:
        1. Load every listing with load_listings().
        2. Filter by max_price and by size, when each is provided.
        3. Score what's left by keyword overlap with `description`.
        4. Drop anything scoring zero.
        5. Sort by score, highest first, and return the listing dicts —
           at most config.SEARCH_RESULT_LIMIT of them.

    Test it from a terminal before you move on:
        python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"
    """
    import re
    listings = load_listings()

    # 1. Filter by max_price
    if max_price is not None:
        listings = [item for item in listings if item['price'] <= max_price]

    # 2. Filter by size
    if size is not None:
        size_lower = size.lower()
        filtered = []
        for item in listings:
            item_size = item['size'].lower()
            # Split sizes by non-word chars to handle cases like "S/M" -> ["s", "m"]
            tokens = re.findall(r'[a-z0-9]+', item_size)
            if size_lower in tokens or size_lower == item_size:
                filtered.append(item)
        listings = filtered

    # 3. Score by keyword overlap with description
    desc_tokens = set(re.findall(r'\w+', description.lower()))
    scored_listings = []

    for item in listings:
        # Combine text fields for keyword matching
        text_to_search = (item['title'] + " " + item['description'] + " " + " ".join(item.get('style_tags', []))).lower()
        item_tokens = set(re.findall(r'\w+', text_to_search))
        
        score = len(desc_tokens.intersection(item_tokens))
        
        if score > 0:
            scored_listings.append((score, item))

    # 4. Sort by score (descending)
    scored_listings.sort(key=lambda x: x[0], reverse=True)

    # 5. Return at most config.SEARCH_RESULT_LIMIT items
    return [item for score, item in scored_listings][:config.SEARCH_RESULT_LIMIT]


# ── Tool 2: suggest_outfit ────────────────────────────────────────────────────

def suggest_outfit(new_item: dict, wardrobe: dict) -> str:
    """
    Given a thrifted item and the user's wardrobe, suggest one or two outfits.

    This one calls the model, through `generate()`. You don't need to think
    about rate limits — the adapter handles pacing for you.

    Args:
        new_item: a listing dict — the item the user is considering.
        wardrobe: a wardrobe dict with an 'items' key holding a list of items.
                  **It may be empty.** Handle that.

    Returns:
        A non-empty string with outfit suggestions.
        With an empty wardrobe, return general styling advice rather than
        raising or returning "". Unit 4 has you trigger the empty wardrobe on
        purpose, so decide now what it should do.

    TODO:
        1. Check whether wardrobe['items'] is empty.
        2. If it is, ask the model for general styling ideas for this item.
        3. If it isn't, format the wardrobe items into the prompt and ask for
           specific combinations naming pieces the user already owns.
        4. Return the model's response.

    Test it from a terminal before you move on:
        python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"
    """
    item_name = new_item.get('title', 'this item')
    item_desc = new_item.get('description', '')
    
    items = wardrobe.get('items', [])
    if not items:
        prompt = (
            f"I am considering buying {item_name}. {item_desc}\n"
            "I don't have anything in my wardrobe yet. "
            "Could you give me some general styling advice and suggest an outfit or two "
            "I could build around this item?"
        )
    else:
        wardrobe_list = "\n".join(f"- {w.get('name', 'item')} ({w.get('category', '')})" for w in items)
        prompt = (
            f"I am considering buying {item_name}. {item_desc}\n"
            "Here is what I currently have in my wardrobe:\n"
            f"{wardrobe_list}\n\n"
            "Can you suggest one or two specific outfits combining the new item with pieces I already own?"
        )
        
    return generate(prompt)


# ── Tool 3: create_fit_card ───────────────────────────────────────────────────

def create_fit_card(outfit: str, new_item: dict) -> str:
    """
    Write a short caption someone would actually post about the find.

    This calls the model too.

    Args:
        outfit:   the outfit suggestion string from suggest_outfit().
        new_item: the listing dict for the item.

    Returns:
        A two-to-four sentence caption.
        If `outfit` is empty or whitespace, return a descriptive message rather
        than raising.

    The caption should read like a real post rather than a product description,
    mention the item and its price and platform once each, and be specific about
    the vibe.

    It should also come out **differently for different inputs**. If you run
    this three times on the same item and get three word-for-word identical
    strings, it's one of two things, and both are near the top of `config.py`:

        • CACHE_ENABLED — the adapter handed back an answer it already had
        • TEMPERATURE   — at 0.0 the model gives the same words every time

    TODO:
        1. Guard against an empty or whitespace-only `outfit`.
        2. Build a prompt with the item details and the outfit.
        3. Call generate() and return the response.

    Test it from a terminal before you move on:
        python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"
    """
    if not outfit or not outfit.strip():
        return "I couldn't create a fit card because no outfit suggestion was provided."

    item_name = new_item.get('title', 'this item')
    price = new_item.get('price', 0.0)
    platform = new_item.get('platform', 'unknown platform')
    brand = new_item.get('brand') or 'vintage/unbranded'

    prompt = (
        f"Write a short social media caption about finding this item:\n"
        f"Item: {item_name}\n"
        f"Brand: {brand}\n"
        f"Price: ${price:.2f}\n"
        f"Platform: {platform}\n\n"
        f"The outfit I'm planning to wear it with: {outfit}\n\n"
        "Make it sound like a real person posting about their thrift find. "
        "CRITICAL CONSTRAINTS:\n"
        "1. You MUST include the exact price.\n"
        "2. You MUST mention the brand (if it's vintage/unbranded, say that).\n"
        "3. You MUST suggest EXACTLY ONE accessory to wear with it.\n"
        "4. The entire output MUST be strictly under 100 words."
    )

    return generate(prompt)
