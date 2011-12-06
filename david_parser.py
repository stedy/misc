"""
Script to format output from DAVID gene ontology (http://david.abcc.ncifcrf.gov/) 
and write out textfile with similar ontology
"""

import string
import argparse

#TODO make lookup to GO ID number

def main():
    parser = argparse.ArgumentParser(description = """Parse DAVID output file for later loading into R""")
    parser.add_argument('infile', help = 'input file from DAVID output')
    args = parser.parse_args()

    infile = open(args.infile, 'r').readlines()
    
    for i in infile:
        if i[0:6] == "GOTERM":
            k = i.split('\t')
            container = k[5].split(",")
            container = [x.lstrip(' ') for x in container]
            GO = k[1].split("~")

            #outfile includes ontology type in name
            filename = str(GO[1].replace(' ', '_')) + ".txt"
            with(open(filename, 'w')) as fn:
                for x in container:
                    fn.write("%s \n" % x)

if __name__ == "__main__":
    main()
