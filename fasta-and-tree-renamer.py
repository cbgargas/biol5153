#! /usr/bin/python

import argparse
import csv
from collections import defaultdict
import re
from Bio import SeqIO



#create and argumentparser object('parser') that will hold all info to parse the cmd line
parser = argparse.ArgumentParser(description = 'This script removes false frequency-code pairs from telemetry data')
#positional arguments
#number argument to input
#parser.add_argument('csv', help='csv input file')
parser.add_argument('fasta', help='fasta input file')
#parser.add_argument('tree_file', help='LTP tree input file')
#parser.add_argument('out_file', help='output fastafile')
#parse the cmd line arguments
args = parser.parse_args()


# next we use Seq.IO to extract the accession #s as dict keys and the genus_species_etc as the value to rename the fasta file headers and the tree file
# code dictionary: key = frequency, value = list of real code
code = defaultdict(dict)
with SeqIO.parse(args.fasta, 'fasta') as fas:
    #gives available options for an object
    print(dir(fas))
    #for line in fas:
        


# opening and reading csv file as dict object
#with open(args.csv, 'r') as chars:   
#    #create a csv reader object
#    reader = csv.reader(chars, delimiter='\t')
#    #skip the header line
#    #header = next(reader)
#    # read in file line by line
#    for line in reader:
#        #skip blank lines
#        if not line:
#            continue
#        else:
#            # need to ask if key exists already
#            # if line[0] in code:
#            #     # same as appending to a regular list
#            code[line[0]] = line[1]
#            #print(line)
#    #         else:
#    #             code[line[0]] = []
#    #             code[line[0]].append(line[1])
#

#opening and reading fasta file to extract accession numbers and species names
##works as of now
#with open(args.tree_file, 'r') as tree:
#
#    for line in tree:
#        row=line.rstrip('\n')
#        #tree_match = re.search('(\s{2}\s{1}\d{1:} {1})', row)
#        if re.search("\s+\d+\s'", row):
#            m = re.search("(\s+)(\d+)(\s)'", row)
#            print(m.group(1)+m.group(2)+m.group(3))
#        else:
#            #continue
#            print(row)
#
##check our work
## for key,value in code.items():
##      print(key, value)
#        
#with open(args.fasta, 'r') as fas:
#
#    for line in fas:
#
#        row = line.rstrip('\n')
#
#        for key,name in code.items():
#  
#            if re.search(key, row):
#                row='>'+str(name)
#
#            else:
#                continue
#
#        print(row)
#    