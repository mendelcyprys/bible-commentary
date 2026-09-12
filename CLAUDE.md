# Bible Commentary Project

Verse-by-verse open source commentary on the Torah (five books of Moses). Each verse has a main page and optionally a companion commentaries page.

## Project layout

- `{N}_{Book}/{NN}_chapter/{NN}_verse.md` — main verse page with template sections (text, language, translations, structure, rabbinic, halacha, scholarship, cross-references)
- `{N}_{Book}/{NN}_chapter/{NN}_verse_commentaries.md` — companion page with medieval commentators (Rashi, Ibn Ezra, Ramban, Rashbam, Sforno, Chizkuni)
- `{N}_{Book}/{NN}_chapter/README.md` — chapter index linking to verses
- `{N}_{Book}/README.md` — book index linking to chapters
- `scripts/` — gitignored; Python scripts for template application and data injection
- `tmp/` — gitignored; source JSON files from Sefaria export

Books: 1_Genesis, 2_Exodus, 3_Leviticus, 4_Numbers, 5_Deuteronomy.

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

## Conventions

- All text content is in Hebrew, Aramaic, or Arabic — this is a primary-source commentary, not a translation project.
- Commentary files use `##` for commentator names (Rashi, Ibn Ezra, etc.), not `###`.
- Verse files use `##` for major sections and `###` for subsections.
- Cite sources when adding content.
- Licenses for included texts: Rashi/Ibn Ezra/Chizkuni/Onkelos/Targum Jerusalem/Rasag are Public Domain. Ramban/Sforno are CC-BY. Rashbam is CC-BY-SA.
