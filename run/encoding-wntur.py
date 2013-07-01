#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

#dd = {'\xe7': 'ç',
      #'\xc7': 'Ç',
      #'\xe7': 'ü',
      #'\xf0': 'ğ',
      #'\xfe': 'ş',
      #'\xfd': 'ı',
      #'\xdc': 'Ü',
    #}

from_enc = 'iso-8859-9'
to_enc = 'utf-8'

for line in open('wntur.xml').readlines():
    print line.decode('iso-8859-9').encode('utf-8'),
