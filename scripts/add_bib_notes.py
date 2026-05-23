#!/usr/bin/env python3

from pathlib import Path
import re
import yaml
import bibtexparser

BIB_FILE = Path("publications-academic.bib")
PUB_DIR = Path("content/publication")

def academic_slug(key):

    s = key.strip()

    # Replace separators with dash

    s = re.sub(r"[^A-Za-z0-9]+", "-", s)

    # Split lowercase-uppercase

    s = re.sub(r"([a-z])([A-Z])", r"\1-\2", s)

    # Split letter-digit

    s = re.sub(r"([A-Za-z])([0-9])", r"\1-\2", s)

    # Split digit-letter

    s = re.sub(r"([0-9])([A-Za-z])", r"\1-\2", s)

    # Collapse repeated dashes

    s = re.sub(r"-+", "-", s)

    return s.strip("-").lower()

def clean_bibtex_text(s):
    if not s:
        return ""
    return (
        s.replace("{", "")
         .replace("}", "")
         .replace("\n", " ")
         .strip()
    )

with BIB_FILE.open(encoding="utf-8") as f:
    bib = bibtexparser.load(f)

for entry in bib.entries:
    key = entry.get("ID")
    if not key:
        continue

    index_md = PUB_DIR / academic_slug(key) / "index.md"
    if not index_md.exists():
        print(f"Skipping {key}: no index.md")
        continue


    text = index_md.read_text(encoding="utf-8")

    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        print(f"Skipping {key}: no YAML front matter")
        continue

    frontmatter, body = m.groups()
    data = yaml.safe_load(frontmatter) or {}


    doi = data.pop("doi", None)

    if doi:
     if "hugoblox" not in data:
        data["hugoblox"] = {}

     if "ids" not in data["hugoblox"]:
        data["hugoblox"]["ids"] = {}

     data["hugoblox"]["ids"]["doi"] = doi

    note = clean_bibtex_text(entry.get("note", ""))
    annote = clean_bibtex_text(entry.get("annote", ""))

   # Migrate deprecated url_pdf
    url_pdf = data.pop("url_pdf", None)

    if url_pdf:

     # Ensure links exists
     links = data.setdefault("links", [])

     # Avoid duplicate pdf links
     already_has_pdf = any(
        isinstance(link, dict) and link.get("type") == "pdf"
        for link in links
     )

     if not already_has_pdf:
        links.append({
            "type": "pdf",
            "url": url_pdf
        })

    visible_notes = []

    if note:
        data["note"] = note
        visible_notes.append(note)

    if annote:
        data["annote"] = annote
        visible_notes.append(annote)

    if visible_notes:
        data["summary"] = " ".join(visible_notes)

    new_frontmatter = yaml.safe_dump(
        data,
        sort_keys=False,
        allow_unicode=True,
        width=1000,
    )

    index_md.write_text(f"---\n{new_frontmatter}---\n{body}", encoding="utf-8")
    print(f"Updated {index_md}")
