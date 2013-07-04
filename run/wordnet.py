#! /usr/bin/python
# -*- coding: utf-8 -*-

__author__ = "Osman Baskaya"

from bs4 import BeautifulSoup
from collections import defaultdict as dd
import sys
import gzip
import codecs

words = dd(list)

class Synset(object):

    def __init__(self, literals, ilrs, pos):
        self.literals = literals
        self.ilrs = ilrs
        self.pos = pos

    def __str__(self):
        return ' '.join([word for word, sense in self.literals])

    #def __repr__(self):
        #return ' '.join([word for word, sense in self.literals])
        
def preprocess():
    soup = BeautifulSoup(open('wntur-utf8.xml'), 'xml')
    synsets = soup.findAll('SYNSET')
    return soup, synsets


def construct():
    soup, synsets = preprocess()
    for synset in synsets:
        pos = synset.findAll('POS')[0].next
        ltrs_soup = synset.findAll('LITERAL')
        ilrs_soup = synset.findAll('ILR')

        # word - sense_id pair
        literals = [(ltr.next, ltr.next.next.next) for ltr in ltrs_soup]

        # ilr_id - ilr_type pair
        ilrs = dict((ilr.next, ilr.next.next.next) for ilr in ilrs_soup)
        s = Synset(literals, ilrs, pos)

        # adding word->[synset1, synset2]
        for ltr in literals:
            try: 
                words[ltr[0]].append(s)
            except KeyError:
                print ltr
                break


def find_word(word):
    return words[word]


def write2file(all_synsets, target_words):
    f = codecs.open('train.wn.synset', 'w', 'utf-8')
    for word_synsets, w in zip(all_synsets, target_words):
        #f.write(w.decode('utf-8'))
        if len(word_synsets) != 0:
            for synset in word_synsets:
                literals = [d[0] for d in synset.literals]
                f.write("{}|".format(synset.pos))
                f.write(','.join(literals))
                f.write(';')
        f.write('\n')
    f.close()

def create_synset_file():
    construct()
    target_words = [word.strip().decode('utf-8') for word in gzip.open('train.root.gz')]
    synsets = map(find_word, target_words)
    write2file(synsets, target_words)


def main():
    construct()
    word = sys.argv[1]
    synsets = find_word(word)
    for synset in synsets:
        literals = [d[0] for d in synset.literals]
        print "{}|".format(synset.pos),
        print ','.join(literals),
        print ';',

if __name__ == "__main__":
    create_synset_file()







