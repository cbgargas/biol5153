#! /usr/bin/python

import argparse

#create and argumentparser object('parser') that will hold all info to parse the cmd line
parser = argparse.ArgumentParser(description = 'Returns the Fibonacci number at a specified position in the Fibbonaci sequence')

#positional arguments
#number argument to input
parser.add_argument('input_number', help='the position in the Fibbonacci sequence that you wish to know the number for', type=int)

#optional arguments, the group makes these options mutually exclusive
group = parser.add_mutually_exclusive_group()
group.add_argument('-s','--simple', action='store_true', help='print simple output (default)')
group.add_argument('-v','--verbose', action='store_true', help='print verbose output')

#parse the cmd line arguments
args = parser.parse_args()

#Calculate the Fibbonacci number, the below sets a =0 and b =1
a,b = 0,1 

for i in range(int(args.input_number)):
    a,b = b, a+b

#test for if the user has selected vcerbose or simple output, putting verbose first makes simple poutput the defualt
if args.verbose:
    #verbose output
    print('for position', str(args.input_number), "the Fibbonacci number is", a)
else:
    #simple output
    print(str(args.input_number), a)