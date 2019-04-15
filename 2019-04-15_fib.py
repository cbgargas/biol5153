#! /usr/bin/python

import argparse

def get_args():

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
    return parser.parse_args()

def fib(n):
    #Calculate the Fibbonacci number, the below sets a =0 and b =1
    a,b = 0,1 

    for i in range(int(n)):
        a,b = b, a+b
    return (a)

def print_output(position, fib_num):
    #test for if the user has selected vcerbose or simple output, putting verbose first makes simple poutput the defualt
    if args.verbose:
        #verbose output
        print('for position', position, "the Fibbonacci number is", fib_num)
    else:
        #simple output
        print(position, fib_num)

def main():
    fib_num = fib(args.input_number)
    print_output(args.input_number, fib_num)

#get the arguments before calling main
args = get_args()

#execute the program by calling main. __ __allow you to call these functions in other scripts and not just through this one

if __name__ == '__main__':
    main() 