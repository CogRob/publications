import bibtexparser
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

complete_entries = []
all_bibs = ['conf-papers.bib', 'articles.bib', 'journal-issues.bib', 'reports.bib']

for filename in all_bibs:
    with open(filename) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)

    entries = bib_database.entries

    for entry in entries:
        if(filename == 'conf-papers.bib'):
            entry[unicode('type')] = unicode('Conference')
        elif(filename == 'articles.bib' or filename == 'journal-issues.bib'):
            entry[unicode('type')] = unicode('Journal')
        elif(filename == 'reports.bib'):
            entry[unicode('type')] = unicode('Report')
        else:
            print("Unknown filename!")
            break

    complete_entries.extend(entries)

db = BibDatabase()
db.entries = complete_entries

writer = BibTexWriter()
# writer.order_entries_by = ('year', 'month', 'type')
writer.order_entries_by = ('author')

with open('publications.bib', 'w') as bibfile:
    bibtexparser.dump(db, bibfile, writer)