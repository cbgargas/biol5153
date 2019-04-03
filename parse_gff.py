#! /usr/bin/python 

# Specify the input files
fasta_file = "/home/cbg/2019s/biol5153/watermelon_files/watermelon.fsa"
gff_file = "/home/cbg/2019s/biol5153/watermelon_files/watermelon.gff"

# open the fasta file
genome = open(fasta_file, "r")

# open the gff file
gff=open(gff_file, "r")

# read the gff file line by line
for line in gff:
	#skip blank lines
	
	#removing line breaks
	line = line.rstrip('\n')
	#print(line)
	#split each line on the tab character
	sequence, source, feature, start, end, length, strand, phase, attributes = line.split('\t')
	print(start, end)
	
	#extract the DNA seq from the genome
	#.gff files are from 1, so we need to either add or subtract one to get it to grab the right seq bits
	for char in genome:	
		substring=genome[(int(start)-1):(int(end)+1)]
		print(substring)
	
	#print the DNA seq of this feature
	
	# calculate the GC content for this feature
	
#gff.close()