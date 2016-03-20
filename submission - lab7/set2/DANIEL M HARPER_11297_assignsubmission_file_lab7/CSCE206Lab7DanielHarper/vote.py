# Author: Daniel Harper
# Assignment: Lab 7 - vote.py
# Original Date: 3/1/2016
# Last Updated:  3/1/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import *
#import random
#import sys
#import argparse
#import matplotlib.pyplot as plt
#from numpy import *
import operator


# Body Section#######################################################
#--------------------------------------------------------------------
# Write a vote counting program that reads a vote file and print out 
# the ranked list of candidates
# Create a vote file votes.txt as below
# John, jimmy, Lilly
# Joseph, linda
# John, linda
# John
# …
# Essentially each line contains votes from one voter with 1-3 
# candidates.
# Name your code as vote.py. Then when you run:
# python vote.py votes.txt
# Assume the vote filename is votes.txt. The output of your program
# should be like:
# john 25
# Lilly 15
# Linda 10
# GRADER NOTE: my votes.txt included with the project will replicate
# this example

inputFile = open("votes.txt", 'r')
votes = inputFile.readlines()
inputFile.close()

registry = dict()

for v in votes:
	line = v.strip().split(",") # strip only does front and back of a string, not the body
	for x in line:
		try:
			registry[x.strip()] += 1 # if key exists, increment
		except:
			registry[x.strip()] = 1 # add key if needed, increment to 1

sorted_registry = sorted(registry.items(), key=operator.itemgetter(1), reverse=True)
for x in sorted_registry:
 	print(x[0], "\t", x[1])

