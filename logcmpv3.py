#!/usr/bin/env python
import sys
import gzip
import os

def getfilename(path):
    files = os.listdir(path)
    for file in files:
        if not os.path.isdir(file):
            if os.path.splitext(file)[0].startswith('tlog'):
                logcmp(file)

def logcmp(fname):
    outputfname = './logcmp.txt'
    outputf = open(outputfname,'a')
    refline = ''
    i = 1
    if fname.endswith('.gz'):
        f = gzip.open(fname)
    else:
        f = open(fname)
    
    for eachline in f:
        if eachline == refline:
            print "%s : duplicated %d" % (fname, i)
            print refline,
            print eachline,
            print "."*100
            outputf.write(fname+ ": duplicated " + str(i) + '\n')
            outputf.write(refline)
            outputf.write(eachline)
            outputf.write("."*100 + '\n')
            i = i + 1
        else:
            refline = eachline

    f.close()
    outputf.close()

if __name__ == '__main__':
    path = './'
    getfilename(path)

