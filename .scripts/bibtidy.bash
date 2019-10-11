#!/usr/bin/env bash
bibtex-tidy "$@" \
    --curly \
    --numeric \
    --space 4 \
    --align \
    --sort \
    --strip-enclosing-braces \
    --sort-fields \
        address \
        author \
        booktitle \
        category \
        copyright \
        day \
        doi \
        isbn \
        issn \
        journal \
        location \
        metadata \
        month \
        note \
        number \
        on \
        pages \
        publisher \
        series \
        shorttitle \
        title \
        url \
        urldate \
        volume \
        year \
    --strip-comments