#! /usr/bin/python

import argparse
import csv
from collections import defaultdict
from Bio import SeqIO
import re

def get_args():


    #create and argumentparser object('parser') that will hold all info to parse the cmd line
    parser = argparse.ArgumentParser(description = 'parses a file and extracts sequences by feature')

    #positional arguments
    #number argument to input
    parser.add_argument('gff_file', help='GFF3 formatted file')
    parser.add_argument('fasta_file', help='Fasta file corresponding to the GFF3 file')

    #parse the cmd line arguments
    return parser.parse_args()

def parse_fasta():
    genome_object = SeqIO.read(args.fasta_file, 'fasta')
    return genome_object.seq
    
def parse_gff(genome):
    #
    with open(args.gff_file, 'r') as gff:

        #dictionary to hold cds seqs. key = gene_name, value = dictionary2 where key = exon#, value = sequence.

        coding_seqs = defaultdict(dict)

        #
        reader = csv.reader(gff, delimiter='\t')

        for line in reader:

            #skip commented lines
            if not line:
                continue
            
            #elif re.match('^#', line)
            #    continue

            else:
                #extract the start and end coordinates for this feature
                start   = int(line[3])-1
                end     = int(line[4])
                strand  = line[6]
                feature_type = line[2]
                attributes = line[8]
                species = line[0]

                #extract the seq for this feature
                feature_seq = genome[start:end]
                
                #print(len(feature_sequence), line[5])

                #reverse complement the seq if necessary
                if(strand == '-'):
                    feature_seq = rev_comp(feature_seq)

                # calculate the gc content of feature
                gc_content = gc(feature_seq)

                if(feature_type == 'CDS'):
                    
                    #split the attributes field into its separate parts, to get the gene info
                    exon_info=attributes.split(' ; ')
                    
                    #extract the gene name
                    gene_name = exon_info[0].split()[1]

                    #test whether there is or isn't an entry in index 2, which holds the value 'exon for genes that have introns. If there is no calu in index 2 then the gene doesn't have an intron, and we can just print it
                    if len(exon_info[0].split()) > 2:
                        #extract the exon number
                        exon_number = exon_info[0].split()[-1]

                        #check that the key exists, if not then the value will be a dictionary. 
                        if gene_name in coding_seqs:
                            #store the coding sequence for this exon
                            coding_seqs [gene_name] [exon_number] = feature_seq 
                        else: 
                            # first time encountering this gene so declare this dictionary for it.
                            coding_seqs [gene_name] = {}

                            #store the coding sequence for this exon.
                            coding_seqs [gene_name] [exon_number] = feature_seq

                    else: 
                        #print the sequence in FASTA format
                        print('>'+species.replace(' ', '_')+'_'+gene_name)
                        print(feature_seq)

    # done reading the GFF file, loop over coding_seqs to print the cds sequences 
    # gene = gene name, exons = dict of exon sequences (key = exon_num, value = exon_seq)
    for gene, exons in coding_seqs.items():
        
        # make a variable that will hold the concatenated CDS seqeunce
        cds_for_this_gene = ''

        #print the FASTA header for this gene
        print('>'+species.replace('\t', '_')+'_'+gene)

        # loop over all the exons for this particular gene
        # IMPORTANT: need to sort the exons first
        
        for exon_num, exon_seq in sorted(exons.items()):
            #print(gene, exon_num, exon_seq)               
            cds_for_this_gene += exon_seq
            
        #print 
        print(cds_for_this_gene)

def rev_comp(seq):
    return seq.reverse_complement() 
    #print('1- ', seq)
    #print('2- 'seq_revcomp)

def gc(seq):
    seq = seq.upper()
    count_of_g = seq.count('G')
    count_of_c = seq.count('C')

    return ((count_of_g + count_of_c)/len(seq))*100

    #print(gc_content)

def main():
    genome = parse_fasta()
    parse_gff(genome)

#get the arguments before calling main
args = get_args()

#execute the program by calling main. __ __allow you to call these functions in other scripts and not just through this one
if __name__ == '__main__':
    main() 


