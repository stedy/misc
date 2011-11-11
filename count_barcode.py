#script to count barcodes within a selection of target sequences

#barcode, sum of seq_counts, length of counts

import string
import argparse


def main():
    parser = argparse.ArgumentParser(description = """Generate summary stats
    for barcodes within sequences""")
    parser.add_argument('input_seqs', help = """input seq file as a raw .txt""")
    #parser.add_argument('barcode_name', help = """barcode_name""")
    parser.add_argument('barcode_in', help = """paired barcode primer name file""")
    args = parser.parse_args()
    
    #then start main argument
    #read in sequence files
    seqs = []
    seq_counts = []    
    infile = file(args.input_seqs).readlines()
    for line in infile:
        k = line.split()
        seqs.append(k[0])
        seq_counts.append(k[1])
    fullseqs = zip(seqs, seq_counts)
    print "This is the number of sequences %s" % len(fullseqs)
    
    #then read in barcode files
    barcode = file(args.barcode_in).readlines()
    barcode_name = []
    actual_barcode = []
    for bline in barcode:
        v = bline.split()
        barcode_name.append(v[0])
        actual_barcode.append(v[1])
    for bn,bc in zip(barcode_name, actual_barcode):
        count = 0
        ss_sum = []
        for x,y in fullseqs:
            k = string.find(x, bc)
            if k != -1:
                count += 1
                ss_sum.append(int(y))
        print bn, bc, sum(ss_sum), count

if __name__ == '__main__':
    main()
