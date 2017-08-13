#!/bin/bash 

cd `dirname $0`

INFILE=words_alpha.txt

cat "${INFILE}" |sort |uniq |sort |./wordFilter.pl $@ |tr '\n' '\t' |fold -w 130 -s 
