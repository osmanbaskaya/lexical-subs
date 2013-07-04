#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys
import gzip
from itertools import count

t = sys.argv[1]

#indexes = map(int, gzip.open(t + ".index.gz").readlines())
indexes = gzip.open(t + ".index.gz").read().split()

for line, i in zip(sys.stdin, count()):
    line = line.strip()
    line = line.split()
    try:
        index = int(indexes[i])
    except ValueError:
        print >> sys.stderr, line, indexes[i]
        exit()
    start = max(0, index-3)
    #print start, index+4, line[index]
    right = line[start:index]
    context = ' '.join(right) + " __XX__ "
    left = line[index+1:index+4]
    context += ' '.join(left)
    print context
