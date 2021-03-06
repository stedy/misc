#cut up sequences by length

from collections import defaultdict
from operator import itemgetter
import argparse

test, motifs, counts = [], [], []
forbidden = ['CAS', 'ASS', 'CASS']
def motif_finder(motif, count, n):
    s = 0
    n = int(n)
    for x in range(len(motif)):
        k = motif[s:s+n]
        if k not in forbidden:
            if len(k) == n:
                #print k, count
                s += 1
                test.append(list([k,count]))
                motifs.append(k)
                counts.append(count)
            

def main():
    parser = argparse.ArgumentParser(description= """Script to split aa motifs by
        length and group by count""")
    parser.add_argument('infile', help = "Input file with motif and count in col1 & 2""")
    parser.add_argument('length', help = "Motif length (currently setup for 3 or 4)")
    parser.add_argument('outfile', help = "Outfile to write summary stats to")
    args = parser.parse_args()
    
    with open(args.infile, 'rb') as infile:
        lines = infile.readlines()[1:]
        for x in lines:
            vals = x.split("\t")
            motif_finder(vals[0], int(vals[3]), args.length)
        d = defaultdict(int)
        for x in test:
            d[x[0]] += int(x[1])

    p= sorted(d.iteritems(), key = itemgetter(1), reverse = True)
    count_sum = sum(counts)
    with open(args.outfile, 'wb') as ao:
        for k, v in p:
             ao.write("%s %g \n" % (k, float(v)/count_sum))

if __name__ == "__main__":
    main()


