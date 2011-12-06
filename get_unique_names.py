"""script to get unique genes by name from Genepop Fst file"""
import argparse

parser = argparse.ArgumentParser(description="""Script to get unique set of genes in list""")
parser.add_argument('infile', help = "file formatted as from R write.table() output")
parser.add_argument('outfile', help = "file listing unique genes only")
arguments = parser.parse_args()

genes_complete = []
with open(arguments.infile, 'r') as infile:
	for line in infile.readlines()[1:]:
		k = line.split("\t")
		genes_complete.append(k[5].strip('\n'))

genes = set(genes_complete)
with open(arguments.outfile, 'w') as gl:
	for item in genes:
		gl.write("%s\n" % item)
