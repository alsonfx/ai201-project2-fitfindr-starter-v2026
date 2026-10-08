# FitFindr

> ### 👋 Start here
>
> **New to this repo? Read [RUNNING.md](RUNNING.md) first** — setup, every
> command, and what to do when something breaks.
>
> Once `python test.py` passes:
>
> ```bash
> python app.py listings --full -n 6      # read the data (Milestone 1)
> python app.py fields                    # what you can filter on
> python app.py ask 'vintage graphic tee under $30'
> ```
>
> All three tools are stubs, so that last command will do nothing useful yet.
> That's the starting position.
>
> **The rest of this file is your submission.** Fill it in as you go.

---

<!-- ─────────────────────────────────────────────────────────────────────────
     HOW TO USE THIS FILE

     This is your submission. Fill each section in as you finish the milestone
     it belongs to — don't leave it all to the end.

     Unit 3 asks for the first five sections. Unit 4 adds the five below them.
     Leave the unit 4 sections alone until then; they're here so you know
     what's coming.

     Everything is pasted as TEXT. No screenshots, no images, no video links.
     A typed block of output gets full credit; a picture of the same output
     gets none.
     ───────────────────────────────────────────────────────────────────────── -->

<!-- ═══════════════════════ UNIT 3 — THE BUILD ═══════════════════════ -->

## What This Does

FitFindr takes a natural language query for an item of clothing, parses it, and searches a dataset of listings to find a match. If an item is found, it evaluates the user's existing wardrobe and suggests an outfit incorporating the new item. Finally, it creates a "fit card" with a catchy caption for social media. If no item matches the search query, it gracefully ends the session and suggests that the user adjust their query.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Tool Inventory

<!-- Four lines per tool. This is worth 2 points and it's the single most
     common place students lose them.

     "Returns a list" earns NOTHING. The description has to say what is IN
     the list.

     The empty case isn't optional either — it's the thing your loop branches
     on, and if you don't decide it here you'll discover it as a crash in
     Milestone 5. -->

### `search_listings`

- **What it does: searches the listing file and returns a match**
- **Inputs: description, size, and max_price**
- **Returns: an array/list of items that mtach the keyword and cost**
- **When it has nothing: it should return an empty string**

### `suggest_outfit`

- **What it does: it should match items in the listings together and suggest a combination of them**
- **Inputs: new_item and wardrobe**
- **Returns: an array that contains items that match the wardrobe criteria**
- **When it has nothing: empty string**

### `create_fit_card`

- **What it does: write a short caption someone would actually post**
- **Inputs: outfit, new_item**
- **Returns: a caption based on the outfit and the new_item**
- **When it has nothing: empty string**

---

## Planning Loop

<!-- Your branch rule, stated as a rule — the condition AND both paths — plus
     the file and function that holds it.

     Like this:
       "If search_listings returns an empty list, put a message in the session
        and stop. Otherwise take the first result and go to suggest_outfit."
        — agent.py::run_agent

     The grader checks your code against what you claim here, so the file and
     function have to be real. -->

**Branch rule:** If `search_listings` returns an empty list or nothing, put a message in the session and stop. Otherwise, take the first result and go to `suggest_outfit`.

**Where it lives:** `agent.py::run_agent`

**How the query is parsed:** The query is parsed using regular expressions to extract `size` and `max_price`, while the original query string is used as the `description`.

**What moves through the session:** The parsed query parameters, the search results, the selected item, the user's wardrobe, the outfit suggestion, the fit card, and any error message generated during execution.

---

## Sample Run

<!-- Two things go here.

     1. One FULL query and its output, pasted as text.
     2. Your three per-tool terminal tests — the command and what it printed. -->

**One full query**

```
$ python app.py ask '...'
```

**The three tools, tested one at a time**

```
$ python -c "from tools import search_listings; print(search_listings('graphic tee', max_price=30))"
[{'id': 'lst_002', 'title': 'Y2K Baby Tee — Butterfly Print', 'description': 'Super cute early 2000s baby tee with butterfly graphic. Fitted crop length. Tag says medium but fits like a small.', 'category': 'tops', 'style_tags': ['y2k', 'vintage', 'graphic tee', 'cottagecore'], 'size': 'S/M', 'condition': 'excellent', 'price': 18.0, 'colors': ['white', 'pink', 'purple'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_006', 'title': 'Graphic Tee — 2003 Tour Bootleg Style', 'description': 'Vintage-style bootleg tee with faded graphic. Slightly boxy fit. 100% cotton, soft and worn-in.', 'category': 'tops', 'style_tags': ['graphic tee', 'vintage', 'grunge', 'streetwear', 'band tee'], 'size': 'L', 'condition': 'good', 'price': 24.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_017', 'title': 'Mesh Long-Sleeve Top — Black', 'description': 'Sheer black mesh long-sleeve. Great for layering under a graphic tee or over a bralette. Stretchy material, fits true to size.', 'category': 'tops', 'style_tags': ['y2k', 'grunge', 'goth', 'layering'], 'size': 'S/M', 'condition': 'excellent', 'price': 15.0, 'colors': ['black'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_033', 'title': 'Vintage Band Tee — Faded Grey', 'description': 'Faded grey band-style tee with distressed graphic. Crew neck. Fits boxy. Well-loved but no holes or major damage.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'band tee', 'graphic tee', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 19.0, 'colors': ['grey', 'charcoal'], 'brand': None, 'platform': 'depop'}, {'id': 'lst_011', 'title': 'Low-Rise Cargo Pants — Khaki', 'description': 'Y2K era low-rise cargo pants. Lots of pockets. Khaki color, slightly distressed at the hems. Great for layering with a long tee.', 'category': 'bottoms', 'style_tags': ['y2k', 'cargo', '2000s', 'streetwear'], 'size': 'W29', 'condition': 'fair', 'price': 27.0, 'colors': ['khaki', 'tan'], 'brand': None, 'platform': 'poshmark'}, {'id': 'lst_015', 'title': 'Vintage Graphic Hoodie — Faded Black', 'description': 'Faded black pullover hoodie with barely-visible vintage graphic on the chest. Cozy interior. Some pilling but adds to the worn-in look.', 'category': 'tops', 'style_tags': ['vintage', 'grunge', 'graphic', 'streetwear'], 'size': 'L', 'condition': 'fair', 'price': 26.0, 'colors': ['black', 'charcoal'], 'brand': None, 'platform': 'depop'}]
```

```
$ python -c "from tools import suggest_outfit; from utils.data_loader import get_example_wardrobe, load_listings; print(suggest_outfit(load_listings()[0], get_example_wardrobe()))"
Here are two specific outfit ideas using the vintage Levi’s 501s and the items currently in your wardrobe. 

### Outfit 1: Effortless Casual (Great for daytime/errands)
* **Top:** White ribbed tank top
* **Outerwear:** Vintage black denim jacket
* **Shoes:** Chunky white sneakers
* **Accessories:** Black crossbody bag

**Why it works:** The white ribbed tank tucked into the medium-wash 501s creates a classic, clean base that highlights the jeans' fit. Layering the vintage black denim jacket on top plays into the "denim-on-denim" trend while keeping a cohesive, casual vibe. The chunky white sneakers and black crossbody bag keep the look modern, comfortable, and balanced.

---

### Outfit 2: Streetwear Edge (Great for cooler weather/going out)
* **Top:** Black cropped zip hoodie
* **Shoes:** Black combat boots
* **Accessories:** Brown leather belt and Black crossbody bag

**Why it works:** The Levi's 501 has a classic straight-leg cut that pairs exceptionally well with chunkier footwear. Tucking the jeans in slightly or letting them break over the black combat boots creates a rugged, grounded silhouette. Adding the brown leather belt breaks up the black-and-blue color palette, while the black cropped zip hoodie hits at just the right spot to accentuate the high waist of the 501s.
```

```
$ python -c "from tools import create_fit_card; from utils.data_loader import load_listings; print(create_fit_card('jeans and white sneakers', load_listings()[0]))"
Scored the ultimate 90s off-duty vibe with these Vintage Levi's 501 Jeans in a dreamy medium wash for just $38.00 on Depop! I'm planning to style them with a faded band tee and crisp white sneakers for the effortless Sunday morning look. Thrift gods were definitely on my side today.
```

---

## How I Used AI

<!-- Two specific moments. What you asked, what came back, what you changed.

     "I used Claude to help me code" is not enough.

     "I gave Claude my search_listings spec. It returned None on no match
     instead of an empty list, so I changed it" is the level we want. -->

**Moment 1**

- *What I asked for:* I asked the AI to modify `agent.py::run_agent` to pass values strictly through the `session` dictionary instead of directly between variables.
- *What came back:* The AI refactored the function to read from and write to keys like `session["selected_item"]` and `session["outfit_suggestion"]`, along with adding a debug print of the session at the end of the `_show` function.
- *What I changed:* I kept the AI's structural changes to ensure all state is testable and visible, ensuring the `fit_card` correctly referenced `session["outfit_suggestion"]`.

**Moment 2**

- *What I asked for:* I asked the AI to ensure the empty-results error message was helpful rather than just "No results".
- *What came back:* The AI provided: "No matching items found. Please try adjusting your search terms, broadening the size, or increasing the price limit."
- *What I changed:* I accepted the exact string because it directly names the actionable steps the user could take to fix their query.

**Moment 3**

- *What I asked for:* In Unit 4, I asked the AI to rewrite the `create_fit_card` prompt to strongly enforce my constraints: strict inclusion of the brand, exact price, exactly one accessory, and length strictly under 100 words.
- *What came back:* The AI suggested structuring the prompt with a bolded "CRITICAL CONSTRAINTS" section, laying out the four requirements as a numbered list. It also smartly suggested dynamically adding "vintage/unbranded" if the brand field was None.
- *What I changed:* I pasted the new prompt into my `tools.py` exactly as suggested, and it instantly bumped my evaluation results from a 0/5 MISSED to a 5/5 MET because the model actually respected the strongly formatted constraints.

<!-- ═══════════════════════ UNIT 4 — THE TEST ═══════════════════════

     Don't fill these in during unit 3.
     ═══════════════════════════════════════════════════════════════════ -->

---

## Run Log — Before

<!-- Five criteria, five tries each, in this exact format.

     Five, because your criteria are written out of five. Mark each try PASS
     or FAIL, count the passes, and read that count against your target — a
     row targeting 4 of 5 with three PASS cells is MISSED (3/5).

     `python run_eval.py --label before` runs everything and writes the table
     into results/. Paste it here and fill in the verdicts. -->

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ----- | ----- | ------- |
| 1. matching query completes | 4/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2. impossible query stops early | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3. state tracking verification | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 4. fit card format test | 5/5 | FAIL | FAIL | FAIL | FAIL | FAIL | MISSED (0/5) |
| 5. complex query handling | 4/5 | FAIL | FAIL | FAIL | FAIL | FAIL | MISSED (0/5) |

**Real output from one try for each criterion**, pasted as text, produced by `run_eval.py::main` calling `agent.py::run_agent`:

```text
### 1. matching query completes
- Query: `vintage graphic tee under $30`
- Wardrobe: example
- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)

Trace:
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 10 items: Y2K Baby Tee — Butterfly Print, Graphic Tee — 2003 Tour Bootleg Style, Mesh Long-Sleeve Top — Black … +7 more
[2] suggest_outfit
      in:  dict with keys: item, wardrobe
      out: Here are two specific outfit ideas using the Y2K butterfly baby tee and pieces from your current wardrobe, lea…
[3] create_fit_card
      in:  dict with keys: outfit, item
      out: Found this absolute dream of a Y2K butterfly baby tee on Depop for just $18.00 and I am officially in my early…

### 2. impossible query stops early
- Query: `designer ballgown size XXS under $5`
- Wardrobe: example
- stopped early: yes — No matching items found. Please try adjusting your search terms, broadening the size, or increasing the price limit.

Trace:
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: [] (empty)

### 3. state tracking verification
- Query: `Y2K pants`
- Wardrobe: example
- stopped early: no
- selected_item: Low-Rise Cargo Pants — Khaki ($27.0, poshmark)

Trace:
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 8 items: Low-Rise Cargo Pants — Khaki, Y2K Baby Tee — Butterfly Print, Corduroy Wide-Leg Pants — Rust … +5 more
[2] suggest_outfit
      in:  dict with keys: item, wardrobe
      out: Here are two outfit formulas combining the new Y2K low-rise khaki cargo pants with pieces already in your wardrobe...

### 4. fit card format test
- Query: `vintage graphic tee`
- Wardrobe: example
- stopped early: no
- selected_item: Y2K Baby Tee — Butterfly Print ($18.0, depop)

Fit card:
Just scored the ultimate Y2K butterfly baby tee on Depop for only $18, and I am obsessed! Can't wait to style the sweet butterfly graphic with baggy denim and chunky sneakers for the ultimate Y2K streetwear vibe. 🦋✨

### 5. complex query handling
- Query: `find me a red dress and check if a style is available today`
- Wardrobe: example
- stopped early: no
- selected_item: Oversized College Crewneck — Faded Red ($21.0, thredup)

Trace:
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 10 items: Oversized College Crewneck — Faded Red, Oversized Flannel Shirt — Plaid Red/Black, Graphic Tee — 2003 Tour Bootleg Style … +7 more
[2] suggest_outfit
      in:  dict with keys: item, wardrobe
      out: Based on your current wardrobe, the **Oversized College Crewneck in Faded Red** will fit right in because you …
[3] create_fit_card
      in:  dict with keys: outfit, item
      out: Scored this faded red Oversized College Crewneck on thredUp for just $21.00, and it’s already doing all the he…
```

---

## Verdicts and Diagnoses

| # | Criterion | Target | Verdict | How I decided |
| - | --------- | ------ | ------- | ------------- |
| 1 | matching query completes | 4/5 | MET (5/5) | The agent completed all tool calls and generated a fit card for a valid search query every time. |
| 2 | impossible query stops early | 5/5 | MET (5/5) | The agent immediately halted and returned the expected error string after receiving an empty list from `search_listings`. |
| 3 | state tracking verification | 5/5 | MET (5/5) | The trace confirms the exact `item` received by `search_listings` was passed into `suggest_outfit` correctly. |
| 4 | fit card format test | 5/5 | MISSED (0/5) | The fit card failed to consistently include exactly one accessory and the item's brand because the prompt didn't strictly mandate these fields, and the brand was missing from the item listing string anyway. |
| 5 | complex query handling | 4/5 | MISSED (0/5) | The agent failed to route distinct parts of the query to different tools; it just forwarded the entire complex query verbatim into the `search_listings` tool description field. |

**Diagnoses**

1. **Criterion 4 (fit card format test) missed:** The model's output was the problem. The prompt for `create_fit_card` didn't strongly enforce the inclusion of the brand and exactly one accessory. Furthermore, the dataset schema doesn't explicitly contain a `brand` field, so the model had to guess or omit it, resulting in failures.
2. **Criterion 5 (complex query handling) missed:** The loop's branch/routing was the problem. The agent's parsing logic jams the entire user query directly into the `description` field for `search_listings`. It has no logic to decompose a query and selectively route instructions to `suggest_outfit` or avoid searching for non-clothing questions.

---

## Loop Trace

<!-- One full run, printed step by step, with the MCP call visible in it.

     `python app.py ask '...' --trace` once you've added the trace.step()
     calls in Milestone 2.

     Worth pasting BOTH the happy path and the empty-search path. The empty
     one should be visibly shorter, because it stops. If your two traces are
     the same length, your branch isn't working — and this is the fastest way
     anyone will ever find that out. -->

**Happy path**

```
$ uv run app.py ask 'vintage graphic tee under $20' --trace
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: 10 items: Y2K Baby Tee — Butterfly Print, Graphic Tee — 2003 Tour Bootleg Style, Mesh Long-Sleeve Top — Black … +7 more
[2] suggest_outfit
      in:  dict with keys: item, wardrobe
      out: Here are two specific outfit ideas using the Y2K Butterfly Baby Tee and pieces already in your wardrobe, leani…
[3] create_fit_card
      in:  dict with keys: outfit, item
      out: Found the absolute holy grail Y2K Butterfly Baby Tee on Depop for just $18.00! Can't wait to style the ultimat…

  Found:    Y2K Baby Tee — Butterfly Print — $18.0 on depop

  Outfit:   Here are two specific outfit ideas using the Y2K Butterfly Baby Tee and pieces already in your wardrobe, leaning into that authentic early-2000s aesthetic...

  Fit card: Found the absolute holy grail Y2K Butterfly Baby Tee on Depop for just $18.00! Can't wait to style the ultimate early-2000s streetwear look by pairing it with baggy dark-wash jeans, chunky sneakers, and a brown leather belt. It’s giving total effortless Y2K mall-rat energy and I am obsessed.
```

**Empty search**

```
$ uv run app.py ask 'ballgown' --trace
[1] search_listings
      in:  dict with keys: description, size, max_price
      out: [] (empty)

  No matching items found. Please try adjusting your search terms, broadening the size, or increasing the price limit.
```

**On the MCP move:** The `search_listings` call output remained exactly the same because `mcp_client` unwraps the JSON structure transparently back to a python `list[dict]`.

---

## The Improvement

<!-- What you changed, why your diagnosis pointed at it, and the after-run in
     the same table format. One change, measured properly.

     `python run_eval.py --label after` -->

**What I changed:** I rewrote the prompt for `create_fit_card` in `tools.py` to explicitly enforce the constraints under a "CRITICAL CONSTRAINTS" section. I instructed the model to always include the exact price, mention the brand (or state if it's vintage/unbranded), suggest exactly one accessory, and keep the output strictly under 100 words.

**Which failure it was meant to fix:** The failure of Criterion 4 (fit card format test) where the model failed to follow the strict constraints because they weren't strongly enforced in the prompt.

### Run Log — After

| Criterion | Target | Try 1 | Try 2 | Try 3 | Try 4 | Try 5 | Verdict |
| --------- | ------ | ----- | ----- | ----- | ----- | ----- | ------- |
| 1. matching query completes | 4/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 2. impossible query stops early | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 3. state tracking verification | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 4. fit card format test | 5/5 | PASS | PASS | PASS | PASS | PASS | MET (5/5) |
| 5. complex query handling | 4/5 | FAIL | FAIL | FAIL | FAIL | FAIL | MISSED (0/5) |

**Did it help, and how do I know:** Yes, it worked perfectly! The `create_fit_card` model consistently output exactly one accessory (e.g. "chunky white sneakers" or "black crossbody bag"), accurately included the price, successfully defaulted to "vintage/unbranded" since `brand` wasn't present, and stayed tightly under 100 words. Criterion 4 improved from a 0/5 MISSED to a 5/5 MET.

---

## What's Still Broken

Criterion 5 is still completely broken. The agent's loop is too simplistic to do query decomposition or complex routing. Right now, it just dumps the entire unparsed complex sentence verbatim into `search_listings`. Since the search relies on a basic token overlap, it ends up getting confused by irrelevant words. Fixing this would require a major structural change—either an intermediate parser or an LLM-based semantic router ahead of the tools—but I stopped here to adhere to the "one improvement only" rule!

<!-- ═════════════════════════════════════════════════════════════════════

     SUBMISSION CHECKLIST — unit 3

       [ ] criteria.md has five numbered criteria, each with a target
       [ ] Each criterion has a reason underneath it
       [ ] All five unit 3 sections above have real content
       [ ] Tool Inventory: all three tools, inputs WITH TYPES, a specific
           return value, and the empty case
       [ ] Planning Loop names the branch rule and agent.py::run_agent
       [ ] Sample Run: one full query plus the three per-tool tests, as text
       [ ] At least four new commits
       [ ] Repository URL submitted — WRITE IT DOWN, you submit the same one
           next unit

     SUBMISSION CHECKLIST — unit 4

       [ ] mcp_server.py exists with one tool registered
           (or a written record of exactly where the rewire broke)
       [ ] Run Log — Before, five criteria, five tries each
       [ ] Real output pasted underneath, naming file and function
       [ ] A verdict on every criterion
       [ ] A diagnosis for every miss, naming a place AND a mechanism
       [ ] Loop Trace, with the MCP call visible in it
       [ ] All three failure modes triggered and handled
       [ ] One improvement, with Run Log — After in the same format
       [ ] What's Still Broken
       [ ] At least four new commits
       [ ] The SAME repository URL as last unit

     Do not delete and recreate this repository. Your commit history is what
     shows your criteria existed before your results did.
     ═════════════════════════════════════════════════════════════════════ -->

---

📖 **How to run this project: [RUNNING.md](RUNNING.md)**
