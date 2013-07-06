#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

import sys
import gzip

data = sys.argv[1]
n = int(sys.argv[2])

subs = gzip.open(data).readlines()
for sub in subs:
    sub = sub.split()
    print ','.join(sub[1:n*2+1:2])
