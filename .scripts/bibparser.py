#!/usr/bin/env python3

import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

complete_entries = []
all_bibs = ['conf-papers.bib', 'articles.bib', 'journal-issues.bib', 'reports.bib']

for filename in all_bibs:
    parser = bibtexparser.bparser.BibTexParser(common_strings=True)
    with open(filename, encoding='utf-8') as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file, parser=parser)

    entries = bib_database.entries

    for entry in entries:
        if(filename == 'conf-papers.bib'):
            entry['category'] = 'Conference'
        elif(filename == 'articles.bib' or filename == 'journal-issues.bib'):
            entry['category'] = 'Journal'
        elif(filename == 'reports.bib'):
            entry['category'] = 'Report'
        else:
            print("Unknown filename!")
            break

    complete_entries.extend(entries)

db = BibDatabase()
db.entries = complete_entries

writer = BibTexWriter()
writer.order_entries_by = ('author')

with open('publications.bib', 'w', encoding='utf-8') as bibfile:
    bibtexparser.dump(db, bibfile, writer)