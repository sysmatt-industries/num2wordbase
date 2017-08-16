# Convert integers to/from numeric bases generated from english words
# Also, Generate random passwords based on above


(tested on python 2.6+) 

```
cd /tmp
git clone https://github.com/sysmatt-industries/num2namebase.git

cd num2namebase
```

## Demo Programs

Convert integer numbers to/from word bases:

```

$ ./wordbase.py -h
usage: wordbase.py [-h] [-v] [--names4] [--names5] [--names3] [--word5]
                   [--word4] [--word3] [-f WORDSFILE]
                   items [items ...]

positional arguments:
  items                 List of items to encode/decode

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Enable Verbose Messages
  --names4              Add names4 word dictionary to base
  --names5              Add names5 word dictionary to base
  --names3              Add names3 word dictionary to base
  --word5               Add word5 word dictionary to base
  --word4               Add word4 word dictionary to base
  --word3               Add word3 word dictionary to base
  -f WORDSFILE, --wordsfile WORDSFILE
                        Specify a input file containing whitespace delimited
                        list of unique words to use as base

$ ./wordbase.py 22 9 8237492873492 2384279349827398401823708347
22      AID
9       ACY
8237492873492   ABBY-VOS-SOU-KACY-AUS
2384279349827398401823708347    BEY-TEI-OTA-NONA-CUE-LIZA-ROM-DEB-SIA


$ ./wordbase.py BEY-TEI-OTA-NONA-CUE-LIZA-ROM-DEB-SIA  ABBY-VOS-SOU-KACY-AUS ACY AID 
2384279349827398401823708347    BEY-TEI-OTA-NONA-CUE-LIZA-ROM-DEB-SIA
8237492873492   ABBY-VOS-SOU-KACY-AUS
9       ACY
22      AID

$ ./wordbase.py --names5 9837492347 ALTOM-FLEIG-GRECO 
9837492347      ALTOM-FLEIG-GRECO
9837492347      ALTOM-FLEIG-GRECO

```

Generate random passwords using name/word bases:

```


$ ./randomWordBasePassword.py  -h
usage: randomWordBasePassword.py [-h] [-v] [-c] [-d] [-b BITS] [-q QUANTITY]
                                 [-f WORDSFILE] [-n RANDOMNUM] [--names4]
                                 [--names5] [--names3] [--word5] [--word4]
                                 [--word3]

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         Enable Verbose Messages
  -c, --case            Enable word case randomization
  -d, --delim           Enable delimiter randomization
  -b BITS, --bits BITS  Specify number of bits in password to be generated,
                        default=40
  -q QUANTITY, --quantity QUANTITY
                        Specify quantity of passwords to generate, default=1
  -f WORDSFILE, --wordsfile WORDSFILE
                        Specify a input file containing whitespace delimited
                        list of unique words to use as base
  -n RANDOMNUM, --randomnum RANDOMNUM
                        Append or Prepend a random number of the specified
                        length

Dictionaries:
  Select which word sets compose the base dictionary, Select between 3,4 and
  5 letter english names and english words. Default: names3,names4

  --names4              Add names4 word dictionary to base
  --names5              Add names5 word dictionary to base
  --names3              Add names3 word dictionary to base
  --word5               Add word5 word dictionary to base
  --word4               Add word4 word dictionary to base
  --word3               Add word3 word dictionary to base

$ ./randomWordBasePassword.py --quantity 5 --randomnum 2 
71-LIDA-AMY-SHAE-CHY
31-EHL-LOS-LYM-DEON
EIS-UDY-BIR-TAJ-36
LENA-AKE-ZAM-HOE-26
13-KEE-ALIX-BUCK-BREE


$ ./randomWordBasePassword.py --quantity 5 --randomnum 2  --names4 
BARB-KENT-MANA-LINO-LUPE-62
ANDY-EVON-LEIA-ETHA-ALVA-74
00-BIBI-ELSE-KARY-RENE-DION
ALIX-OMER-SARI-AURA-TOBI-07
12-ARIE-DAWN-VERA-OLIN-LULA


$ ./randomWordBasePassword.py --quantity 5 --randomnum 2 --case --delim 
81=KEW=LYM=KOK=MAR
LARA;LING;ROBT;ORD;97
LEIF%LAX%YEM%BIO%66
78.DOI.SIM.HONG.EMO
37,ken,ella,ava,lane




```

