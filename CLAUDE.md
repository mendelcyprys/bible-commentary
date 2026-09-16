# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Verse-by-verse open source commentary on the Torah (five books of Moses). 5,846 verse pages and 5,077 companion commentary pages. Each verse has a main page and optionally a companion commentaries page.

## Project layout

- `{N}_{Book}/{NN}_chapter/{NN}_verse.md` — main verse page with template sections (text, language, translations, structure, rabbinic, halacha, scholarship, cross-references)
- `{N}_{Book}/{NN}_chapter/{NN}_verse_commentaries.md` — companion page with medieval commentators (Rashi, Ibn Ezra, Ramban, Rashbam, Sforno, Chizkuni)
- `{N}_{Book}/{NN}_chapter/README.md` — chapter index linking to verses
- `{N}_{Book}/README.md` — book index linking to chapters
- `scripts/` — gitignored; Python scripts for template application and data injection; `scripts/research/` holds the research tools described below
- `tmp/` — gitignored; source JSON files from Sefaria export, research drafts (`tmp/*_rabbinic_analysis.md`, `tmp/*_hebrew.md`), and fetched sources (`tmp/sources/`)
- `.venv/` — gitignored; Python 3.11 venv with Text-Fabric, for the BHSA corpus

Books: 1_Genesis, 2_Exodus, 3_Leviticus, 4_Numbers, 5_Deuteronomy.

## Navigating to a verse

To find a verse by reference (e.g., Genesis 1:1): `1_Genesis/01_chapter/01_verse.md`. Chapter and verse numbers are zero-padded to two digits.

## Content already populated

These sections are machine-populated from Sefaria data and present on every verse:
- Targum Onkelos (Aramaic)
- Tafsir Rasag (Judeo-Arabic + Arabic script transliteration)

Present on ~840 verses:
- Targum Jerusalem (fragmentary by nature)

Commentary files contain Hebrew-language text from: Rashi, Ibn Ezra, Ramban, Rashbam, Sforno, Chizkuni. HTML tags from the source have been converted to markdown bold/italic.

All other template sections are empty and awaiting contribution.

## Working with verse files

- The first line of each verse file is the Hebrew text as a `#` heading with full cantillation marks (taamei hamikra) and vowel points (nikkud).
- Section headers (`##` and `###`) define the template structure. Do not remove or rename them.
- When adding content to a section, write below its header and above the next header.
- The "Medieval Commentators" section on the main page contains only a link to the companion file — do not inline commentary there.
- Empty sections are intentional; they mark areas for future contribution.

## Scripts (in scripts/, gitignored)

Run from project root with `python3 scripts/<name>.py`. All are idempotent.

1. `apply_template.py` — applies the section template to bare verse files (skips files that already have `##` headers)
2. `inject_onkelos.py` — reads `tmp/Onkelos/*.json`, writes Aramaic text under `### Targum Onkelos`
3. `inject_rasag.py` — reads `tmp/Tafsir Rasag - he - merged.json`, writes Judeo-Arabic + Arabic transliteration under `### Tafsir Rasag`
4. `inject_commentaries.py` — reads `tmp/downloads/*.json`, creates `*_commentaries.md` files and links them from the main verse page

## Rasag transliteration notes

The Arabic script conversion in `inject_rasag.py` uses a mapping derived from analysis of the Sefaria transcription:
- **Gimel is reversed** from some reference grammars: ג̇ (dotted) = ج (jim), ג (plain) = غ (ghayn). Confirmed by word frequency analysis.
- All other dotted pairs are standard: ד̇=ذ, ת̇=ث, כ̇=خ, ט̇=ظ, צ̇=ض.
- Ta marbuta (ة) and ha (ه) are not distinguished — both map from ה.
- Hamza variants are not distinguished — all map from א to ا.
- ~13 inconsistencies exist in the Sefaria source itself.

## Research and writing process

This is how verse content is researched. The model case is Exodus 21:1–11: `tmp/exodus_21_1-11_rabbinic_analysis.md` (what the tradition says and how likely it is) and `tmp/exodus_21_1-11_hebrew.md` (the Hebrew itself, with every grammatical claim tested). Read both before starting a new unit; match their depth and format.

### Workflow

1. **Draft in `tmp/`, never straight into verse files.** Write the research up as `tmp/<book>_<ch>_<verses>_rabbinic_analysis.md` and `tmp/<book>_<ch>_<verses>_hebrew.md`. Populate the verse files only when the user explicitly asks, and commit that as its own commit.
2. **Define the unit by the paragraph markers** (*setumot*/*petuchot*), not by chapter.
3. **Find the parallel passages the unit depends on and treat them as part of the job.** The tradition reads the corpora together, and so does critical scholarship. Ex 21:2–11 cannot be analysed without Lev 25:35–55, Deut 15:12–18 and Jer 34. Use `api/links` (below) to find them.
4. **Iterate in passes, and keep a changelog at the top of each draft**: what changed in each pass and which earlier claims were corrected. Never silently rewrite a verdict.
5. **Pull out and test the grammar.** For each rabbinic derivation or commentator argument that rests on a claim about the Hebrew, number the claim and test it against the corpus (see "Grammar layer").
6. **End each draft with**: a ranked summary (most strained → most defensible, with explicit "moved" notes), open questions, and a map of which findings go into which verse-template section.

### Sources and tools

- **dyprys** (local hybrid search over book-length texts):
  - Invocation: `cd /Users/mendelcyprys/Documents/dyprys-app && source .venv/bin/activate && dyp ask "<query>" --model gemma -k 14 -q`.
  - Put global flags (`-L sefaria`) **before** the command. `--model gemma` or `--model jina` is mandatory.
  - The `sefaria` library has Bible, Mishnah, Talmud and Mishneh Torah (see `/Users/mendelcyprys/Documents/sefaria/NOTES.md`; it stops at Rambam). The `neuro` library has Elon's *Jewish Law* and Bible translations.
- **Sefaria API** — `scripts/research/sefaria_fetch.py OUT.md "<ref>" ...` dumps Hebrew and English. Its docstring lists the naming gotchas.
  - `api/texts/<ref>?context=0` — a single text.
  - `api/v3/texts/<Book>?version=hebrew|Tanach with Ta'amei Hamikra` — a whole book in one call.
  - `api/links/<ref>?with_text=0` — every work that cites a verse, with exact ref strings. Use it before guessing a title.
  - `api/index/<Title>` — the schema for complex works (Mekhilta, Sifra, Sefer HaChinukh reject book-level refs).
  - Hebrew-only works (Mekhilta d'Rashbi, Midrash Tannaim, Malbim, Torah Temimah, Hoffmann) must be read in Hebrew. Verse mapping is sometimes loose (Abarbanel's blocks; Malbim's paragraph numbers). Check the lemma, not the label.
- **Hebrew Tanakh for plain-text searches**: `tmp/sources/tanakh/tanakh_heb.json` (rebuild with `python3 scripts/research/sefaria_tanakh.py`). Helpers in `scripts/research/tanakh_text.py`: `verses()`, `cons()`, `pointed()`, `accents()`.
- **ETCBC BHSA** — the whole Hebrew Bible tagged for grammar (stem, tense, person/gender/number, phrase function, clause type, ketiv/qere):
  - Loaded with Text-Fabric: `.venv/bin/python` + `from tf.app import use; A = use("ETCBC/bhsa", silent="deep")`. Data is in `~/text-fabric-data`.
  - Examples in `scripts/research/bhsa_*.py`.
  - **Pitfall**: `F.lex.s(lex)` returns lexeme nodes as well as word nodes. Filter with `F.otype.v(n) == "word"`.
  - **Pitfall**: the article is a separate word (lex `H`).
  - Licence: CC BY-NC. Cite counts and parses; do not copy its data into this repo.
- **Grammar**: Gesenius–Kautzsch–Cowley (1909), public domain on Wikisource, pages named `Gesenius'_Hebrew_Grammar/<§>._<Title>`.
- **Ancient translations**: Onkelos, Rasag and Targum Jerusalem are in the verse files. LXX (Rahlfs): blueletterbible.org/lxx. Vulgate: drbo.org/lvb. Targum Pseudo-Jonathan: Sefaria ("Targum Jonathan on Exodus"). Note that Sefaria's English translations sometimes err (e.g. "his" for "her").
- **Modern scholarship**: TheTorah.com often pairs a source-critical essay with a traditional one on the same law (open access). Open-access journal PDFs can be text-extracted with `pypdf`. Scholarship behind paywalls may be cited only "as reported"; say so explicitly.
- **Save what you fetch** under `tmp/sources/<unit>/` so the draft can be re-checked without refetching.

### Research standards

- **Every claim must be traceable to a ref the reader can open.** Quote Hebrew/Aramaic verbatim from the fetched text, with the ref. Never quote from memory.
- **Read commentators in full on the whole unit**, not just the famous lemma: Mekhilta d'R. Yishmael *and* d'Rashbi, Sifra/Sifrei, Tosefta, Yerushalmi and Bavli, Rambam, Malbim, Torah Temimah, Hoffmann, Hirsch, Abarbanel, Shadal, Cassuto, Netziv, Rashbam, Bekhor Shor. Malbim and Torah Temimah are the best internal test of "how likely": Malbim claims stated linguistic rules, and Torah Temimah flags *asmachta* and marks derivations צ"ע.
- **Check a commentator's citations before relying on them.** In Ex 21, Hirsch's attributions were reliable but his paraphrases and linguistic arguments often were not.
- **Keep three things separate:** what a source says; what the tradition as a whole holds (list the disputes and reversed attributions across parallel texts); and what the text most plausibly means. Grade "how likely" with explicit reasons.
- **Date the sources.** Ask what an author could have known (Malbim d. 1879 could not see Midrash Tannaim, published 1908–09).
- **Don't overclaim negatives.** Say "not noted in any of the sources checked (list them)", never "nobody has noticed".
- **When a correction is needed, state it plainly in the changelog and in place.** Do not bury it.

### Grammar layer (the `*_hebrew.md` file)

Per verse:
- **Accents table** — the Masoretes' parse (conjunctive/disjunctive, main divisions)
- **Words** — each key word's attested uses with counts
- **Grammar and syntax** — BHSA clause analysis where relevant
- **Structure** — place in the paragraph, frames, parallels
- **Ancient translations** — only where they bear on the grammar
- **Claims tested** — a numbered ledger with columns *claim · source · verdict*
- **What this changes** — edits needed in the rabbinic draft, applied there with a pointer back

Testing rules learned the hard way:
- **Give n for every count**, and say whether a search was complete (BHSA) or pattern-based.
- **Make sure the comparison set has the same construction as the verse.** Verb before vs. after a compound subject; suffixed vs. unsuffixed noun; the same stem. Malbim's agreement examples were all verb-first; Ex 21:4 is verb-after.
- **List the competing explanations** (proximity, a pair treated as one unit, orthography, differences between legal collections). Separate "the grammar permits" from "the grammar requires", and "supports the base case" from "supports the extension".
- **Look for parallels across books** (e.g. 1 Chr 11:20 // 2 Sam 23:18 settled the לא/לו spelling question).
- **Use a translation as evidence only when its language could have shown the contrast.** Arabic forces a plural verb after a compound subject; a Greek neuter plural takes a singular verb.
- **Check dictionary claims against the stem actually used.** Hirsch's "mutual" sense of יעד is niphal; Ex 21:8 is qal.

### Writing

- **Plain, direct prose.** Verbatim quotations in `>` blocks with refs. Tables for side-by-side texts, dispute maps and claim ledgers.
- **Put the verdict first**, then the evidence.
- **Content language.** Verse files hold primary-source content (see Conventions). The `tmp/` drafts are written in English with Hebrew quotations.

## Conventions

- All text content is in Hebrew, Aramaic, or Arabic — this is a primary-source commentary, not a translation project.
- Commentary files use `##` for commentator names (Rashi, Ibn Ezra, etc.), not `###`.
- Verse files use `##` for major sections and `###` for subsections.
- Cite sources when adding content.
- Licenses for included texts: Rashi/Ibn Ezra/Chizkuni/Onkelos/Targum Jerusalem/Rasag are Public Domain. Ramban/Sforno are CC-BY. Rashbam is CC-BY-SA.
