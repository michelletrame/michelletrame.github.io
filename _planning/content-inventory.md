# Content inventory & storytelling gaps

Working doc for the redesign. `_planning/` is excluded from the published site
(Jekyll skips folders starting with `_`), but the repo is public, so nothing
confidential goes in here.

## Benchmark: what makes AT&T the strongest case study

The AT&T deck has an arc the others don't consistently hit:

1. **Framing trio**: Challenge / My contributions / Our solution, one sentence each
2. **A human voice up front**: a research quote ("Paying your bill early is just giving your money away…" —Candice) before any process
3. **Context / This artifact / Next steps**: says what the work *was* and where it went
4. **Principles, each proven by design**: Earning Trust, Purposeful Organization, Adaptivity, Thoughtful Backstops, Reducing Friction, A Holistic View. Each has a claim, 2–3 bolded sub-points, and screens that show it
5. **Customer journeys**: Kate, Jack, Elena; concrete people moving through time

What it's missing (and what every case study should add): **outcomes**
(what shipped, what changed, metrics if any) and a **reflection**.

## Shared case study template (proposed)

| # | Section | Required? | Notes |
|---|---|---|---|
| 1 | Hero: title, org, cover image | ✔ | |
| 2 | Meta strip: role, timeframe, team, methods | ✔ | **New** — none of the case studies list timeframe/team consistently |
| 3 | Challenge / Contribution / Solution | ✔ | All 9 already have this |
| 4 | Voice: research pull-quote | ✔ | Missing for Canvas, In the Test, Backcountry Babes, Hack Reactor |
| 5 | Context | ✔ | |
| 6 | Research & insights | ✔ | Numbered insights pattern (APF, Vouch, BB, HR already use it) |
| 7 | Principles / design decisions, each with visuals | ✔ | The AT&T pattern |
| 8 | Journeys or process artifacts | optional | |
| 9 | Outcomes & next steps | ✔ | **Biggest gap across the board** |
| 10 | Reflection: what I'd do differently / what I learned | optional | |
| 11 | Next / previous case study | ✔ | |

## Per case study

### 1. Canvas — "Making teaching tools work for teachers" (needs the most work)
- **Source:** Webflow page (trio only, ~90 words) + `canvas-case-study.pdf` (7-slide Stride handoff: Differentiation Tags, Manage Tags tray, Tag As, Assign To)
- **Have:** challenge, solution (lightweight vs. full-featured release), contributions (surveys, generative research, content design, user testing, specs); annotated UI screens
- **Missing (need from Michelle):** the research story (what teachers said; a quote), why "tags" and not groups, the lightweight-vs-full decision and what the demand signal showed, outcomes/adoption, timeframe/team
- **Images:** card image is AI-generated → **to be replaced (generate new)**. Screens can be cropped from the PDF.

### 2. REI Co-op — "Efficient, optimized store fulfillment" (password-gated)
- **Source:** `rei-case-study-compressed.pdf` (40 slides). Text is extractable.
- **Have:** trio, Context/Artifact/Next steps, methodology (8 stores, 18 interviews by role), workflow map (Upstream → Claim & Search → Picking → Packing), 4 opportunity areas each with a "Stories from our stores" quote + HMW, competitive references
- **Missing:** outcomes (which opportunities were pursued / shipped), the designer's own SOM app design work (deck is research-heavy)
- **Images:** card `PXL_20220628_184436577.jpg`; slides from PDF

### 3. AT&T — "A high-trust, low-stress phone bill" (password-gated, benchmark)
- **Source:** `att-billing-case-study.pdf` (14 slides, image-only; no text layer, copy transcribed by hand)
- **Have:** see benchmark above
- **Missing:** outcomes; slides carry "AT&T Proprietary (Internal Use Only)" footers — strip from page images
- **Images:** card `att-bill.png`; screens from PDF

### 4. Austin Parks Foundation — "Addressing inclusion in parks"
- **Source:** Webflow (~1,900 words, 12 images). Strong already.
- **Have:** quotes (Sally, Anders, Bryan, Daniel, Robert), 3 insights, 9 design criteria, Park Portfolio model
- **Missing:** outcome (did APF adopt anything?), timeframe/team; external link `ac4dxapf.org` likely dead — check
- **Images:** dog-walker, apf-timeline-wide-01, participant-tumbnails, interviewing, complexity-curve, jim-invasive-removal, sally-heart, rico-grafitti, Park Adopter structure, Park Portfolio model; card `Screen Shot 2019-12-05…`

### 5. Vouch — "Borrowing money and protecting relationships"
- **Source:** Webflow (~1,800 words, 20 images). Long "We made / We learned" pilot log ×8
- **Have:** quotes (Holly, Jack), stats (46% ended poorly; 4% vs 700% interest), 3 insights + principles, pilot timeline
- **Missing:** tighten the 8× made/learned log into a scannable timeline; "Current state of Vouch" is dated (2020)
- **Images:** vouch-screens, Vouch illustrations, Loan Dashboard, agreements, designing, loan-builders-new, loan-calc, onboarding, template, timeline, v1-mock-1, version1, vouch-landing-v1/2/3, wireframes, JUST-participants; card `vouch-screens-cover-01`

### 6. In the Test — "Raising the bar for test prep apps"
- **Source:** Webflow (14 images)
- **Have:** analogous research, story-arc design, way-finding, "No wrong answers", impact & next steps
- **Missing:** research quote, any test results
- **Images:** hero, journey, laptops, multi-planet, new-flow, one-planet, postits, sketches, star-reference, story, traditional-flow; card `small-cover`

### 7. IxDA20: Meet Vera — "Creating space for emotional sharing"
- **Source:** Webflow (16 images). Design-charette project.
- **Note:** title differs: homepage card says "Creating Space for **Emotional** Sharing", page h1 says "Creating Space for Sharing"
- **Missing:** clearer framing that this was a 2-day charette (sets expectations for depth)
- **Images:** Ember Map, Ember-prototype(-2), Group, IMG_20200207_142402, elizabot, ellie, ember-fox, ember-plant-screen-2perky, roomba-tweet, venn, vera-cover, vera-data

### 8. Backcountry Babes — "Rebuilding sponsor relationships"
- **Source:** Webflow (21 images)
- **Have:** 3 insights, 3 objectives, client profiles, data storytelling, outcomes (existing/new sponsors, new opportunities); the only case study with a real outcomes section
- **Missing:** a quote
- **Images:** 26.IMG_0731, 28.IMG_0757, Backcountry Splitboard Touring Breckenridge, IMG_4158, observations, rosie-winterfest, mature-babe, young-babe, social/other dashboard, weston, 8 sponsor logos

### 9. Hack Reactor — "Co-designing for perfect teams"
- **Source:** Webflow (11 images)
- **Have:** staff observations, old vs. new process, 3 insights, "the problem we solved was not the problem we started with" (great reflection beat)
- **Missing:** a student quote
- **Images:** HR-BBP_5307-Casual, IMG_2787, group-maker, hack reactor, hr-summary-tiles, josh-and-dan, me-at-hack-reactor, students-mylani; card `HR-four-pairs-tall`

### 10. New case study — last priority, TBD

## Other content fixes
- Medium handle → `@michelle.trame` (confirmed)
- Resume link → `resume-2026.pdf` everywhere (Canvas page nav still points to 2024)
- About page image `bike-hex.png` still hotlinked
- Typos carried over from Webflow to fix during migration: "thier" (APF), "conincidental" (HR), "constrainsts" (REI), "cirucmstances", "accomodate", "mutliple", "deviatons", "prioducrs", "anomolous" (AT&T), "An complete overhaul" (AT&T)

## Migration notes

### Austin Parks Foundation (migrated → `work-apf.html`)
- Timeframe "August–December 2019" inferred from the project timeline diagram + screenshot filename dates. Confirm.
- Webflow labelled the design-criteria groups out of order ("Design criteria for insight 2" sat above the park-identity criteria, which answer insight 1). The new page groups them in insight order without numeric labels.
- The "Robert" quote was an image caption on Webflow; it stays a caption on the photo of him.
- `ac4dxapf.org` link kept but unverified (can't reach it from the build environment). Check it's still live.
- Still missing: an outcome. What did APF do with the recommendations?

## ⚠️ Before the final push (merge to master)
- [x] Michelle confirmed type-of-work tags in `_data/work.yml` (REI and AT&T updated; the rest confirmed as is). Webflow reused tag images, so these may be borrowed from other projects:
  REI (= APF's), Backcountry Babes (= AT&T's), Canvas and In the Test (= Vouch's).

### Vouch, In the Test, Vera, Backcountry Babes, Hack Reactor (migrated)
Michelle to review:
- **Vouch**: "My co-founders and I are continuing to work on Vouch" (2020) changed to past tense ("continued"). The old "Let us help you manage your loan / vouchtogether.com" call to action was dropped as likely out of date. Confirm what's true now.
- **Vouch**: the three insights are paired one-to-one with the three principles (Webflow listed them side by side without saying so).
- **Vouch**: the stats ($183B, 46%, 4% vs 700%) have no sources on the page.
- **Vera**: page uses the homepage title "Creating space for emotional sharing" (the Webflow page said "Creating space for sharing").
- **Hack Reactor**: photos are only 700–900px wide, so the hero is soft on large screens. Higher-res originals from the Desktop folder would help.
- **All**: meta strip details (role, methods, partner) are drawn from the existing copy; check wording.

### REI (rebuilt as a private page, like AT&T)
Source lives in gitignored `private/rei.html`; images via `private/make-rei-images.py`. Michelle to review:
- Store count corrected to **7** (5 observation + 2 interview stores, per the methodology slide); the homepage card previously said eight.
- No outcome yet: the page ends with the deck's next steps. Add what was pursued or shipped. (TODO comment marks the spot.)
- Competitor screenshots (Amazon, Instacart, Target) are shown as references; the Target one is Michelle's own order email.

### Grading case study (new; replaces the Canvas interim page in the private build)
Source: gitignored `private/grading.html` (permalink /work-canvas.html), materials in `private/gradebook/`.
- Password protected per Michelle. University and teammates not named (roles only).
- Paper prototype photos added. Still waiting on the rubric builder screenshot as a file. Drop them into `private/src-img/grading-private/` as faculty-paper-prototype-wall, faculty-paper-prototype-table, faculty-prototypes-board, faculty-sticky-notes, rubric-builder; the page shows them automatically.
- Public build still serves the old interim Canvas page under the new card title until the password gate is decided.
