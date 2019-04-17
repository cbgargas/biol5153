#! /usr/bin/python

import argparse
import csv
from collections import defaultdict

def get_args():

    #create and argumentparser object('parser') that will hold all info to parse the cmd line
    parser = argparse.ArgumentParser(description = 'This script removes false frequency-code pairs from telemetry data')

    #positional arguments
    #number argument to input
    parser.add_argument('tags_file', help='The list of real telemetry frequencies and codes')
    parser.add_argument('data_file', help='Tlemetry data')

    #parse the cmd line arguments
    return parser.parse_args()

def parse_tags():
    # codes dictionary: key = frequency, value = list of real codes
    codes = defaultdict(dict)

    # opening and reading tags file
    with open(args.tags_file, 'r') as tags:   
        #create a csv reader object
        reader = csv.reader(tags, delimiter='\t')

        #skip the header line
        header = next(reader)

        # read in file line by line
        for line in reader:

            #skip blank lines
            if not line:
                continue
            
            else:
                # need to ask if key exists already
                if line[0] in codes:
                    # same as appending to a regular list
                    codes[line[0]].append(line[1])
                else:
                    codes[line[0]] = []
                    codes[line[0]].append(line[1])

        #check our work
        for freq,code in codes.items():
            print(freq, code)
        
    return codes

def parse_data(code_dict):

    # open, read, and parse the telemetry data file
    with open(args.data_file, 'r') as data:
        for line in data:

            # by default, .split works on white space no matter how many characters
            row = line.split()

            #skip the header, could make the value an optional input
            if row[0] == 'Date':
                print(line, end=' ')
                continue
            
            else:
                if row[5] in code_dict[row[4]]:
                    print(line, end=' ')
                else:
                    continue

def main():
    code_dict = parse_tags()
    parse_data(code_dict)

#get the arguments before calling main
args = get_args()

#execute the program by calling main. __ __allow you to call these functions in other scripts and not just through this one
if __name__ == '__main__':
    main() 


