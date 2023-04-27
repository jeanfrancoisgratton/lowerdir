#!/usr/bin/env bash

OUTPUT=/opt/bin
MANPAGE=README.md

if [ "$#" -gt 0 ]; then
    OUTPUT=$1
fi

if [ "$#" -gt 1 ]; then
  MANPAGE=$2
fi

go build -o ${OUTPUT}/lowerdir .
sudo ronn -r ${MANPAGE} --pipe > /usr/share/man/man1/lowerdir.1
sudo mandb

