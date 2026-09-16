# Open Source Verse-by-Verse Bible Commentary

A collaborative, open source commentary on the Hebrew Bible (Torah), organized verse by verse. The goal is to bring together every layer of interpretation — from the plain text through rabbinic tradition to modern scholarship — in one accessible place.

## Verse Page Template

Each verse file follows a standard template. Sections are meant to be filled in over time; empty sections indicate areas waiting for contributions.

### Text
The raw textual layer.

- **Masoretic Notes** — Ketiv/qeri readings, unusual spellings (*plene* vs. *defective*), significant cantillation marks (*taamei hamikra*), paragraph divisions (*petuchot* and *stumot*).
- **Textual Variants** — Differences in the Samaritan Pentateuch, Dead Sea Scrolls, and other manuscript traditions.

### Language
Understanding the Hebrew.

- **Words** — Key terms: roots, semantic range, cognates in other Semitic languages, *hapax legomena*, and how the same word is used elsewhere in Tanakh.
- **Grammar and Syntax** — Verb forms (*binyanim*), construct chains, word order, and syntactic ambiguities that affect meaning.

### Translations
Translations are themselves interpretations. Each translation choice reflects a reading tradition.

- **Targum Onkelos** — The standard Aramaic translation of the Torah, closely literal, reflecting early rabbinic understanding. Used liturgically in Babylonian communities.
- **Tafsir Rasag** — Rav Saadia Gaon's 10th-century Arabic translation. Presented in both the original Judeo-Arabic (Hebrew script) and a transliteration into Arabic script.
- **Targum Jerusalem** — The Fragmentary Targum (*Targum Yerushalmi*). Covers selected verses with expansive Aramaic paraphrase. Present on ~840 verses.
- **Septuagint** — The Greek translation (3rd–2nd century BCE). Important for understanding how Hellenistic Jews read the text, and as a witness to textual variants.
- **Vulgate** — Jerome's Latin translation (4th century CE), often reflecting Hebrew readings that differ from the Septuagint.

### Structure
Literary and poetic form.

Chiastic structures, parallelism, strophic patterns, inclusio, word-counting patterns, acrostics, and how the verse fits into larger structural units (pericope, parashah, book).

### Rabbinic Interpretation
The classical rabbinic reading of the verse.

- **Midrash** — Midrash aggada (narrative expansions) and midrash halacha (legal derivations). Sources include Bereishit Rabbah, Mechilta, Sifra, Sifrei, Tanchuma, and others.
- **Talmud** — References in Bavli and Yerushalmi, whether for legal derivation, homiletical use, or incidental citation.

### Halacha
For legal passages: tracing the development of law from the verse through the tradition.

The chain typically runs: **verse → midrash halacha → Mishna → Talmud → Geonim → Rambam (Mishneh Torah) → Shulchan Aruch** and later authorities. For narrative verses this section will be empty.

### Medieval Commentators
Links to a companion commentaries file (`XX_verse_commentaries.md`) containing the full text of classical commentators. Currently populated with:

- **Rashi** (Public Domain) — 11th century. The most widely-read commentary, weaving *peshat* and *derash*.
- **Ibn Ezra** (Public Domain) — 12th century. Emphasis on grammar, *peshat*, and scientific reasoning.
- **Ramban** (CC-BY) — 13th century. Synthesizes *peshat*, philosophy, *kabbalah*, and law.
- **Rashbam** (CC-BY-SA) — 12th century. Rashi's grandson, committed to strict *peshat*.
- **Sforno** (CC-BY) — 16th century. Philosophical and ethical readings.
- **Chizkuni** (Public Domain) — 13th century. Draws on earlier French commentators.

Source texts from [Sefaria](https://www.sefaria.org).

### Modern Scholarship
Academic and critical approaches.

- **Source Analysis** — Documentary hypothesis (J, E, P, D) and its successors. Which source is this verse attributed to and why? Where are the seams?
- **Ancient Near Eastern Context** — Parallels in Mesopotamian, Egyptian, Ugaritic, and other ANE literature. Shared motifs, legal parallels, and points of divergence.

### Cross-References
Inner-biblical allusions, parallel passages, and significant intertextual connections.

## Project Structure

```
1_Genesis/
  01_chapter/
    01_verse.md                  # verse page (template + translations)
    01_verse_commentaries.md     # companion: medieval commentators
    02_verse.md
    02_verse_commentaries.md
    ...
    README.md                    # chapter index
  ...
  README.md                      # book index
2_Exodus/
...
```

## Contributing

Pick a verse, pick a section, and add what you know. Cite your sources.

### Research standards

- **Cite refs a reader can open**, and quote Hebrew and Aramaic sources verbatim with the reference, not from memory or paraphrase.
- **Keep three things apart**: what a source says, what the tradition as a whole holds (including its internal disputes), and what the text most plausibly means.
- **Test claims about the Hebrew.** When a reading depends on grammar or word usage, check it against the whole of Tanakh and report the count. Compare like with like: the same construction, the same verb stem.
- **Treat parallel passages together.** Many laws appear in more than one place (e.g. Exodus 21, Leviticus 25 and Deuteronomy 15 on slaves), and both the rabbinic and the critical readings depend on how they fit.
- **Mark what you did not verify**, and record corrections openly rather than silently rewriting.

A worked example of the method, and the tools used, is described in `CLAUDE.md` under "Research and writing process".
