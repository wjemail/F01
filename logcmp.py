#!/usr/bin/env python
import sys
import gzip
refline = ''
i = 1
fname = sys.argv[1]
if fname.endswith('.gz'):
    f = gzip.open(fname)
else:
    f = open(fname)
    
for eachline in f:
    if eachline == refline:
        print "duplicated %d" % i
        print refline,
        print eachline,
        print "."*100
        i = i + 1
    else:
        refline = eachline


