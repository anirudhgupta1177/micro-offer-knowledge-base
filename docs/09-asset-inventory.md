# 09 — Asset Inventory

Every image, illustration and clip in the micro-offer funnel, and where it is used.
Assets live in `micro-offer-funnel/public/assets/`, with the manifest and intrinsic
dimensions in `src/data/assets.js`.

---

## 1. Phase stills — `assets/phases/`

The live build, unedited.

| File | Shows | Used in |
| --- | --- | --- |
| `phase1-intro.png` | The opening of the live training, explaining what gets built end to end | Intro section |
| `phase1.png` | Infrastructure map with domain-to-mailbox ratios and monthly cost maths | Phase 1 card · Bonus 3 |
| `phase2.png` | The outbound AI skill file generating ICPs and copy inside Claude | Phase 2 card |
| `phase3.png` | The real client campaign being configured and launched inside Instantly | Phase 3 card |

## 2. Phase clips — `assets/clips/`

| File | Poster | Shows |
| --- | --- | --- |
| `phase1.mp4` | `phase1.jpg` | Phase 1 · live build, unedited |
| `phase2.mp4` | `phase2.jpg` | Phase 2 · live build, unedited |
| `phase3.mp4` | `phase3.jpg` | Phase 3 · live build, unedited |

Each clip has a poster frame so the section paints before any video loads.

## 3. Product mockups — `assets/mockups/`

| File | Product | Used in |
| --- | --- | --- |
| `swipe-file.png` | The Best-Performing Cold Email Copy swipe file, with annotated real emails | **OB1** |
| `field-manual.png` | The 78-page Outbound Field Manual with 25 sections | **OB2** |
| `copywriting-frameworks.png` | The outbound copywriting skill and its email frameworks | **Bonus 2** |
| `vip-community.png` | The private VIP community | **Bonus 5** |

## 4. Illustrations — `assets/art/`

Rendered from HTML sources in `micro-offer-funnel/design/`, for things with no capturable
UI worth screenshotting.

| File | Source | Depicts | Used in |
| --- | --- | --- | --- |
| `bonus-icp-engine.png` | `design/bonus-icp-engine.html` | An unfiltered market narrowing through a filter into a handful of defined customer profiles | **Bonus 1** |
| `bonus-roi-calculator.png` | `design/bonus-roi-calculator.html` | Input rows on the left resolving into a rising return on the right | **Bonus 4** |
| `bump-linkedin.png` | `design/bump-linkedin.html` | One contact list feeding two parallel sequences that converge | **OB3** |
| `guarantee-seal.png` | `design/guarantee-seal.html` | The 30-day campaign-ready guarantee seal | Guarantee section |

> **Why illustrations rather than screenshots:** a Claude skill file has no UI. The ROI
> calculator was never screen-captured. The LinkedIn bump deliberately carries **no
> LinkedIn brand mark**.

Rendered by `scripts/render-art.mjs`.

## 5. Campaign proof — `assets/proof/`

### Headline results

| File | Shows | Label |
| --- | --- | --- |
| `inbox1.jpg` | A real reply inbox filled with green "Call Booked" tags from a live campaign | Reply inbox · live client campaign |
| `analytics1.png` | Instantly analytics: **247.8K emails sent, 918 opportunities worth $68,011** | Instantly · live client campaign |
| `analytics2.png` | Instantly analytics dashboard for a live client outbound campaign | Instantly · campaign analytics |
| `skool-win.png` | A student posting their first booked meetings inside the community | Community · student win |

### Campaign stat tiles

| File | Shows |
| --- | --- |
| `small1.png` | **6,785 contacted · 97.9% delivery · 26.5% reply rate** |
| `small2.png` | Live campaign stats from a client cold email sequence |
| `small3.png` | Live campaign stats showing delivery, open and reply rates |
| `small4.png` | Live campaign stats across a multi-step outbound sequence |
| `small5.png` | Live campaign stats for a high-volume sending account |
| `small6.png` | Live campaign stats showing interested replies and opt-out rate |

### LinkedIn recommendations

| File | From |
| --- | --- |
| `testimonial1.png` | A client, on the outbound system built for them |
| `testimonial2.png` | A B2B client |
| `testimonial3.png` | A client, on lead generation results |
| `testimonial4.png` | An agency owner |
| `testimonial5.png` | A SaaS founder |
| `testimonial6.png` | A consulting client |

## 6. 1:1 session proof — `assets/calls/`

Used on the OTO page to show the sessions actually happen.

| File | Session |
| --- | --- |
| `call-ceejay.jpg` | Ceejay & Bhushan — a founder and their operations lead |
| `call-gangel.jpg` | Lilla, Gábor & Sebastian — a founding team reviewing their outbound |
| `call-saeed.jpg` | Saeed — going through a client setup |
| `call-shrey.jpg` | Shrey — reviewing a live email sequence |

## 7. Written reviews — `assets/words/`

| File | From | About |
| --- | --- | --- |
| `words-shuvasree.jpg` | Shuvasree Bhadra | The LinkedIn outbound automation session |
| `words-nihal.jpg` | Nihal Prasad | Outbound strategies bringing in service enquiries; recommends the 1:1 call |
| `words-anant.jpg` | Anant Kumar Maurya | The outbound strategies and tools covered |
| `words-firstmeeting.jpg` | A client team | First booked meeting from the campaign, on day one |

## 8. Video testimonials — `public/testimonials/`

| Video | Poster | Student | Result |
| --- | --- | --- | --- |
| `ankit.mp4` | `ankit.jpg` | **Ashutosh** | "16 booked calls in my first 30 days — outreach finally runs without me." |
| `arjun.mp4` | `arjun.jpg` | **Arjun** | "Went from 0 to 11 qualified meetings in 3 weeks — first client signed in week 4." |
| `pritham.mp4` | `pritham.jpg` | **Pritham** | "18 booked calls in 21 days — ROI paid back in the first week." |

Carried over verbatim from the main course's testimonial set. Re-encoded copies, each with
a poster frame.

> **Filename note:** Ashutosh's clip is stored as `ankit.mp4` / `ankit.jpg`. The filename
> and the on-page name differ — the file names are historical.

## 9. Brand — `assets/brand/`

| File | Use |
| --- | --- |
| `anirudh-portrait.jpg` | Mentor section portrait |
| `anirudh-wide.jpg` | Wide crop |
| `anirudh.jpg` | General |
| `logo.png` | IntentLedSales wordmark |
| `icon.png` | Favicon / mark |

## 10. Video slots — currently empty on purpose

`VIDEOS` in `src/data/copy.js` has six Loom slots, **all blank**:

| Slot | For |
| --- | --- |
| `feSalesPage` | FE sales page hero VSL |
| `feIntroduction` | FE "Introducing" section VSL |
| `mentor` | FE mentor / "who am I" video |
| `otoSalesPage` | OTO 1 hero VSL |
| `otoThankYou` | OTO 1 call-booking welcome video |
| `otoNoThanks` | OTO 1 no-thanks page VSL |

> ⚠️ **These slots must never point at the training itself.** Those Looms **are** the
> product, and embedding one on a public page gives the whole ₹997 offer away for free.
> They previously did, which is why every id is blank until purpose-made VSLs exist.

An empty slot renders a marked editor placeholder, never a player. Until they are filled,
the hero shows **real proof instead**.

## 11. Reference material — not shipped

Held in `Micro offer Funnel/INPUT (Raw Documentation and references)/`:

| File | What it is |
| --- | --- |
| `Landing Page and Flow Copy/Anirudh Funnel Copy.pdf` | The source copy document. Every word in `src/data/copy.js` is transcribed verbatim from it |
| `IntentLedSales_Brand_Assets.pdf` | Brand system v1.0 — colours, type, tokens |
| `Example Structure and References for Design and UI/FE - Structure.pdf` | Front-end page structure reference |
| `Example Structure and References for Design and UI/OB - Structure.pdf` | Order bump structure reference |
| `Example Structure and References for Design and UI/OTO - Structure.pdf` | OTO page structure reference |
| `Profile Photo.PNG` | Source portrait |
| `Screenshots/` | Raw captures used to produce the proof assets |
