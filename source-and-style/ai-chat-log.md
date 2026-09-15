# AI Chat Log: Source and Style

Tool used: Claude (Anthropic)

I used Claude to clarify the assignment requirements, choose a site and object
relevant to my project topic, interpret what I was seeing in Chrome DevTools, and
scaffold the HTML file. I did the browser inspection and GitHub research myself, and
I reviewed and edited the HTML before committing it.

---

## Clarifying the assignment

**Me:** [shared the assignment URL] explain the homework

**Claude:** This is "Source and Style" — two assignments, both go in a new
`source-and-style` folder in your `is310-coding-assignments` repo, then post the
folder link to discussion thread #3.

Assignment 1: Pick one digital library, archive, collection, or cultural website
related to your focus. Open DevTools and figure out how it was built. Write your
findings in `README.md`. Answer: what tech built it (HTML/CSS/JS)? Any `.html`,
`.css`, `.js` files? Anything you don't recognize? Who built it? How many people?
How can you tell? Include a link to the site and to its GitHub repo if you can find
one. Screenshots go in an `images` folder.

Assignment 2: Build an `index.html` from scratch presenting ONE digitized cultural
object related to your project. Structural requirements: doctype, html, head, body,
at least one heading, one div, one paragraph, one link, one list, and some style or
script. Content requirements: object title, relevant images, description of what it
represents, links to the original collection and object, and metadata you consider
relevant.

## Choosing a topic and target

**Me:** Group A4. Suggested focus: Analytics & Culture: Sports analytics,
film/television, gaming, and social media.

**Claude:** My pick for you: chess. It's the cleanest fit and the one where you have
real domain knowledge, which matters since the grade rests on defending your
interpretive choices.

Audit half: the Lichess open database. Millions of games, fully downloadable, and a
good audit target because what it captures is thin: Elo, moves, time control, opening
ECO code, result. What it erases is everything that makes a game a game. Why someone
resigned in a drawn position. Whether they were tilting. Whether a "blunder" was time
pressure or misevaluation.

Creation half: 50 to 100 games annotated by hand with the fields no chess database
has. Emotional state, time pressure, why each key decision was made, whether the
engine eval matches the subjective experience.

**Me:** step by step, lets go i need explicit steps

**Claude:** Decisions made for you so you're not stuck picking. Assignment 1 target:
Lichess. It's fully open source with a public GitHub org, so "who built it and how
many people" is answerable with hard evidence instead of guessing. Assignment 2
object: the Lewis Chessmen king, British Museum number 1831,1101.83. Real accession
record, real metadata, real collection page.

## Interpreting the DevTools output

**Me:** [uploaded three DevTools screenshots] these good for step2?

**Claude:** Yes, these work. Screenshot 1 covers Elements, 2 covers CSS, 3 covers JS.

What your screenshots actually show:

From the Elements panel: there's an HTML comment right at the top of `<body>` saying
Lichess is open source and linking to lichess.org/source. The `<html>` tag carries
inline CSS custom properties (`--ui-roundness`, `--bg-opacity`), and `<body>` carries
more (`--board-opacity`, `--board-brightness`, `--board-contrast`, `--board-hue`).
User display settings are injected as CSS variables at render time. `<body>` has a
`data-socket-domains` attribute listing six separate socket subdomains (socket0
through socket5), which is websocket infrastructure for real-time play, load-balanced
across hosts. `data-asset-url="https://lichess1.org"` means static assets are served
from a completely different domain than the app. `data-nonce` appears on `<body>` and
on every `<script>` tag, which is a Content Security Policy nonce. The final script is
`site.asset.loadEsmPage('lobby')`, so pages load as ES modules on demand.

From the Network panel: only 4 CSS files versus roughly 25 JS files. This is a
JavaScript-heavy application, not a document-style site. Every filename has a hash in
it (`site.0d8f6420.css`, `lib.3OSM6MH3.js`), which is an automated build pipeline
doing cache-busting, not hand-written files. The JS is code-split: shared `lib.*`
chunks plus page-specific bundles (`lobby.*`, `dasher.*`, `cli.*`). Page weight: 93
requests, 1,081 kB of resources, DOMContentLoaded at 648ms, load at 854ms.

One thing worth calling out: `injection-topics.js` has "content-scripts.js" as its
initiator and shows as a redirect. That file is not Lichess. It's one of your own
browser extensions injecting into the page. The assignment asks "what about files you
don't recognize," and correctly identifying that one file isn't part of the site at
all is exactly the kind of observation that earns credit.

## Interpreting the contributor data

**Me:** [uploaded contributors screenshot, 3-month period]

**Claude:** One thing to catch before you write it up: the period dropdown is set to
Last 3 months, so those commit counts are not all-time. Either note that in your
README or switch it to a wider range and re-screenshot. Don't present 1,691 as a
lifetime number.

**Me:** [uploaded contributors screenshot, all-time period]

**Claude:** Much better. All-time numbers: ornicar 60,556 commits, niklasf 3,128,
jonbgamble 2,965, lenguyenthanh 980. History runs Feb 18, 2012 to Sep 12, 2026.

ornicar has roughly 19x the #2 contributor. That's not "a small team," that's one
person with a support cast, sustained across 14 years.

Note the #2 slot changed between views (Simek in 3 months, niklasf all-time), which is
worth a sentence: recent activity and lifetime activity produce different pictures of
who "built" the site, which is itself an argument about how commit counts represent
labor.

## Building the HTML

**Me:** [asked for the next step]

**Claude:** [provided the full index.html scaffold, including the doctype, head with
a style block defining `.header`, `.metadata`, and an img max-width rule, and a body
containing an h1 inside a div, the object image, two paragraphs of description, a
metadata list inside a styled div, and a sources list with two anchor tags pointing to
the British Museum object record and collection.]

This hits every structural requirement: doctype, html, head, body, headings, a div,
paragraphs, links, lists, and a style block. Read it before you move on. You need to
be able to explain what each tag does if asked, per the AI policy.

## Debugging

**Me:** `open index.html` returned "Command 'open' not found"

**Claude:** You're on WSL, not Mac. My mistake, `open` is macOS-only. Use
`explorer.exe index.html` instead, which hands the file to your default Windows
browser. If that doesn't work, run `python3 -m http.server 8000` and go to
`http://localhost:8000/index.html`.