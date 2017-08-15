#!/usr/bin/python 

from WordBaseConverter import WordBaseConverter
import sys
import random
import argparse

defaultBits=40
defaultWordSets=['3letter']
defaultDelim="-" 
defaultCase="upper"

argsParser=argparse.ArgumentParser()
argsParser.add_argument("-v", "--verbose", help="Enable Verbose Messages", action="store_true")
argsParser.add_argument("-c", "--case", help="Enable word case randomization", action="store_true")
argsParser.add_argument("-d", "--delim", help="Enable delimiter randomization", action="store_true")
argsParser.add_argument("-b", "--bits", help="Specify number of bits in password to be generated, default={0}".format(defaultBits), type=int, default=defaultBits)
#argsParser.add_argument("-w", "--wordsets", help="Specify word set(s) to use, default={0}".format(defaultWordSets), type=str, default=defaultWordSets, choices=WordBaseConverter.WORDS_DICT.keys(), action='append')
for wordDict in WordBaseConverter.WORDS_DICT.keys():
    argsParser.add_argument("--{0}".format(wordDict), help="Add {0} word dictionary to base".format(wordDict), \
        const="{0}".format(wordDict), action='append_const', dest='wordSets')
argsParser.add_argument("-q", "--quantity", help="Specify quantity of passwords to generate, default=1", type=int, default=1)
argsParser.add_argument("-f", "--wordsfile", help="Specify a input file containing whitespace delimited list of unique words to use as base", type=str)
argsParser.add_argument("-n", "--randomnum", help="Append or Prepend a random number of the specified length", type=int, default=0)
args=argsParser.parse_args()


rando = random.SystemRandom()

for q in range(0,args.quantity):
    passwdBitsFrom=(2**(args.bits-1))+1
    passwdBitsTo=(2**(args.bits+1))-1
    myRandInt = rando.randint(passwdBitsFrom,passwdBitsTo)
    myDelim=defaultDelim
    if args.delim:
        myDelim=rando.choice("-_^:,.?$%+=;")
    myCase=defaultCase
    if args.case:
        myCase=rando.choice(tuple("upper lower title".split(" ")))
    if args.verbose:
        print "      args.bits[{0}]".format(args.bits)
        print "        myDelim[{0}]".format(myDelim)
        print "         myCase[{0}]".format(myCase)
        print " passwdBitsFrom[{0}]".format(passwdBitsFrom)
        print "   passwdBitsTo[{0}]".format(passwdBitsTo)
        print "      myRandInt[{0}]".format(myRandInt)

    if args.wordsfile:
        if args.verbose:
            print "     wordsFile[{0}]".format(args.wordsfile)
        wordConv = WordBaseConverter(delim=myDelim,wordsFile=args.wordsfile)
    else:
        if args.wordSets:
            wordConv = WordBaseConverter(wordSets=sorted(args.wordSets),delim=myDelim)
            if args.verbose:
                print "  args.wordSets[{0}]".format(",".join(sorted(args.wordSets)))
        else:
            wordConv = WordBaseConverter(wordSets=sorted(defaultWordSets),delim=myDelim)
            if args.verbose:
                print "defaultWordSets[{0}]".format(",".join(sorted(defaultWordSets)))
            
    wordOut = wordConv.encode(myRandInt)
    if args.randomnum:
        ranDigits=""
        for ranDigitCtr in (range(args.randomnum)):
            ranDigits=ranDigits+str(rando.choice([0,1,2,3,4,5,6,7,8,9]))
        if ranDigits:
            if rando.choice([True,False]):
                # Prepend
                wordOut="{0}{1}{2}".format(ranDigits,myDelim,wordOut)
            else:
                # Append
                wordOut="{0}{1}{2}".format(wordOut,myDelim,ranDigits)
            
    if args.verbose:
        print "  wordBaseCount[{0}]".format(len(wordConv.WORD_BASE_DIGITS))
    if myCase == "upper":
        wordOut=wordOut.upper()
    elif myCase == "lower":
        wordOut=wordOut.lower()
    elif myCase == "title":
        wordOut=wordOut.title()
    print "{0}".format(wordOut)




