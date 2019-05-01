#! /usr/bin/python

import argparse
import csv
from collections import defaultdict
import re
from Bio import SeqIO
import datetime
import io

#object conatining current date:time to use in naming output files
date = datetime.datetime.now()

#create and argumentparser object('parser') that will hold all info to parse the cmd line
parser = argparse.ArgumentParser(description = 'Takes names from Silva LTP fasta files and cleans them up, then cleans up the matching names in the tree using matching accession numbers')

#positional arguments
parser.add_argument('fasta', help='fasta input file')
parser.add_argument('tree_file', help='LTP tree input file')

#optional arguments
parser.add_argument('-fo', '--fasta_output', help='output fasta file in 2line-fasta format', type=str, default=str(date).replace(' ', '_')+'_'+'fasta_output'+'.fixed.fsa')
parser.add_argument('-to', '--tree_output', help='output tree file', type=str, default=str(date).replace(' ', '_')+'_'+'tree_output'+'.fixed.tree')
parser.add_argument('-co', '--csv_out', help='Output csv file, contains accession #, genus_species, higher taxonomy, start pos, end pos, seq length', type=str, default=str(date).replace(' ', '_')+'_'+'seq_info'+'.csv')

#parse the cmd line arguments
args = parser.parse_args()


# next we use Seq.IO to extract the accession #s as dict keys and the accession#+genus_species_etc as the value to rename the fasta file headers and the tree file

#open input fasta in read mode
with open(args.fasta, 'r') as fasta:

    # open output fasta file in write mode
    with open(args.fasta_output, 'w') as fasta_out:
        
        # create dictionary object to store accessions and names: key = accession number, value = desired name
        accession_names = defaultdict(dict)

        #  open csv file to export accession # and other header info into a .csv file so that you don't have to find this shit later
        with open(args.csv_out, 'w') as csv_out:

            #create csv.writer object
            writer = csv.writer(csv_out)
            
            #write header row for csv file
            writer.writerow(['accession','genus_species','family','seq_length','start_pos', 'end_pos'])

            #parses fasta file by each record (sequence)
            for record in SeqIO.parse(fasta, 'fasta'):
                
                #gives available options for an object
                #print(dir(record))
                
                #split the record.name by '_' since biopython won't do it
                name_split = record.name.split('_')
                
                #create string objects to erite to output fasta file and output csv file
                accession = name_split[0]
                name = '_'.join(name_split[5:])
                sequence = str(record.seq)                
                
                #these are just for the csv file
                genus_species = '_'.join(name_split[5:7])
                family = name_split[-1]
                seq_length = name_split[3].replace('bp','')
                start_pos = name_split[1]
                end_pos = name_split[2]

                # need to ask if key exists already, if it does, append the name that goes with it
                if name_split[0] in accession_names:
                    # same as appending to a regular list
                    accession_names[name_split[0]].append(accession+'_'+name)
                #if the key doesn't exist, add it to the dict, then append the associated name
                else:
                    accession_names[name_split[0]] = []
                    accession_names[name_split[0]].append(accession+'_'+name)

                #check our work with the following code
                #for key,value in accession_names.items():
                #    print(key, value)

                # prints the fasta header (accession number and taxoonomy of the record), then prints the sequence for that record. 
                # end fasta format is 2line-fasta
                fasta_out.write('>'+accession+'_'+name+'\n')
                fasta_out.write(sequence+'\n')
                
                #write info to output csv from each record to it's own row
                writer.writerow([accession,genus_species,family,seq_length,start_pos,end_pos])


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

#def main():
#    genome = parse_fasta()
#    parse_gff(genome)
#
##get the arguments before calling main
#args = get_args()
#
##execute the program by calling main. ____allows you to call these functions in other #scripts and not just through this one
#if __name__ == '__main__':
#    main() 
