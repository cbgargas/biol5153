#! /usr/bin/python

import argparse
#import csv
from collections import defaultdict
import re
from Bio import SeqIO
import datetime

date = datetime.datetime.now()

#create and argumentparser object('parser') that will hold all info to parse the cmd line
parser = argparse.ArgumentParser(description = 'Takes names from Silva LTP fasta files and cleans them up, then cleans up the matching names in the tree using matching accession numbers')

#positional arguments
parser.add_argument('fasta', help='fasta input file')
parser.add_argument('tree_file', help='LTP tree input file')

#optional arguments
parser.add_argument('-fo', '--fasta_output', help='output fasta file', type=str, default=str(date).replace(' ', '_')+'_'+'fasta_output'+'.fixed.fsa')
parser.add_argument('-to', '--tree_output', help='output tree file', type=str, default=str(date).replace(' ', '_')+'_'+'tree_output'+'.fixed.tree')

#parse the cmd line arguments
args = parser.parse_args()


# next we use Seq.IO to extract the accession #s as dict keys and the accession#+genus_species_etc as the value to rename the fasta file headers and the tree file

with open(args.fasta, 'r') as fasta:

    with open(args.fasta_output, 'w') as fasta_out:
        # code dictionary: key = accession number, value = desired name
        accession_names = defaultdict(dict)

        #opens fasta file
        for record in SeqIO.parse(fasta, 'fasta'):
            #gives available options for an object
            #print(dir(record))
            #['annotations', 'dbxrefs', 'description', 'features', 'format', 'id', 'letter_annotations', 'lower', 'name', 'reverse_complement', 'seq', 'translate', 'upper']
            name_split = record.name.split('_')
            #print(name_split[5:])
            accession = name_split[0]
            name = '_'.join(name_split[5:])
            sequence = str(record.seq)                
            
            # need to ask if key exists already
            if name_split[0] in accession_names:
                # same as appending to a regular list
                accession_names[name_split[0]].append(accession+'_'+name)
            else:
                accession_names[name_split[0]] = []
                accession_names[name_split[0]].append(accession+'_'+name)

            #check our work
            #for key,value in accession_names.items():
            #    print(key, value)

            # prints the accession number and taxoonomy of the record, then prints the sequence for that record
            fasta_out.write('>'+accession+'_'+name+'\n')
            fasta_out.write(sequence+'\n')
        

#opening and reading tree file to apply names from accession_names dictionary
#works as of now
with open(args.tree_file, 'r') as tree:

    with open(args.tree_output, 'w') as tree_out:

        for line in tree:
            row = line.rstrip('\n')
            #tree_match = re.search('(\s{2}\s{1}\d{1:} {1})', row)
            if re.search("\s+\d+\s'", row):
                m = re.search("(\s+)(\d+)(\s)'", row)
                for key,value in accession_names.items():
                    if re.search(key, row):
                        tree_out.write(m.group(1)+m.group(2)+m.group(3)+(str(value).replace("'", '').replace(']', '').replace('[', '')+'\n')) 
                    else:
                        continue
            else:
                #continue
                tree_out.write(row+'\n')


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