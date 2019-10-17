#!/usr/bin/env bash
bibtex-tidy "$@" \
    --curly \
    --numeric \
    --space 2 \
    --align \
    --sort \
        type \
    --sort-fields \
        address \
        author \
        booktitle \
        category \
        copyright \
        day \
        doi \
        editor \
        isbn \
        issn \
        journal \
        location \
        metadata \
        month \
        note \
        number \
        on \
        organization \
        pages \
        publisher \
        series \
        shorttitle \
        title \
        url \
        urldate \
        volume \
        year \
    --strip-comments \
    --omit \
        date-added \
        date-modified \
    ./sort_bib.py "$@"