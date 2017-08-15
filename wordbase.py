#!/usr/bin/python 

from WordBaseConverter import WordBaseConverter
import sys
import random
import argparse

defaultWordSets=['3letter']

argsParser=argparse.ArgumentParser()
argsParser.add_argument("-v", "--verbose", help="Enable Verbose Messages", action="store_true")
for wordDict in WordBaseConverter.WORDS_DICT.keys():
    argsParser.add_argument("--{0}".format(wordDict), help="Add {0} word dictionary to base".format(wordDict), \
        const="{0}".format(wordDict), action='append_const', dest='wordSets')
argsParser.add_argument("-f", "--wordsfile", help="Specify a input file containing whitespace delimited list of unique words to use as base", type=str)
argsParser.add_argument("items", help="List of items to encode/decode", type=str, nargs='+')
args=argsParser.parse_args()

if args.wordsfile:
    if args.verbose:
        print "     wordsFile[{0}]".format(args.wordsfile)
    wordConv = WordBaseConverter(wordsFile=args.wordsfile)
else:
    if args.wordSets:
        wordConv = WordBaseConverter(wordSets=sorted(args.wordSets))
        if args.verbose:
            print "  args.wordSets[{0}]".format(",".join(sorted(args.wordSets)))
    else:
        wordConv = WordBaseConverter(wordSets=sorted(defaultWordSets))
        if args.verbose:
            print "defaultWordSets[{0}]".format(",".join(sorted(defaultWordSets)))
if args.verbose:
    print "  wordBaseCount[{0}]".format(len(wordConv.WORD_BASE_DIGITS))

for item in args.items:
    if item.isdigit():
        wordOut = wordConv.encode(int(item)).upper()
        print "{0} \t{1}".format(item, wordOut)
    else:
        intOut = wordConv.decode(item.upper())
        print "{0} \t{1}".format(intOut, item.upper())




