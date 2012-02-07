#cut up sequences by length

from collections import defaultdict
from operator import itemgetter
import argparse


test, motifs = [], []
def motif_finder(motif, count, n):
    s = 0
    for x in range(len(motif)):
        k = motif[s:s+n]
        if len(k) == n:
            print k, count
            s += 1
            test.append(list([k,count]))
            motifs.append(k)
            

def main():
    parser = argparse.ArgumentParser(description= """Script to split aa motifs by
        length and group by count""")
    parser.add_argument('infile', help = "Input file with motif and count in col1 & 2""")
    parser.add_argument('length', help = "Motif length")
    parser.add_argument('outfile', help = "Outfile to write summary stats to")
    args = parser.parse_args()


