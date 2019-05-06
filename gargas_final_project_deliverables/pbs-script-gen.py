#! /usr/bin/python
import argparse

#create and argumentparser object('parser') that will hold all info to parse the cmdline
parser = argparse.ArgumentParser(description = 'generates a PBS job script for razor, or trestles, depending on the queue specified')

#add positional arguments, i.e., the required input
parser.add_argument('job', help='The name of the job', type=str)
parser.add_argument('module', help='module needed for script', type=str)
parser.add_argument('command', help='command line input needed for script')

#add optional arguments (- or -- identifies it as an optional argument. giving both - and -- allows a short cut (-) to be added for that flag)
parser.add_argument('-q', '--queue', help='name of the razor, or trestles, queue (default=tiny16core)', type=str, default='tiny16core')
parser.add_argument('-n', '--nodes', help='# of nodes required for job (default=1)', type=int, default=1)
parser.add_argument('-p', '--ppn', help='# of processors desired (default=16)', type=int, default=16)
parser.add_argument('-w', '--walltime', help='amount of time required for job (deafault=6)', type=int, default=6)


#parse the cmd line arguments
args = parser.parse_args()


print('#PBS -N '+args.job)
print('#PBS -q '+args.queue)
print('#PBS -j oe')
print('#PBS -m abe')
print('#PBS -M cbgargas@uark.edu')
print('#PBS -o '+args.job+'.$PBS_JOBID')
print('#PBS -l nodes='+str(args.nodes)+':ppn='+str(args.ppn))
print('#PBS -l walltime='+str(args.walltime)+":00:00")
print()

print('cd $PBS_O_WORKDIR')
print()

print('module purge')
print('module load '+args.module)
print(args.command)