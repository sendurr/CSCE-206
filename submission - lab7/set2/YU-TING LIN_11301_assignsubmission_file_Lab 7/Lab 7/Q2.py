infile=open("votes.txt",'r')

lines=infile.readlines()
print lines
import numpy as np
a = np.array([John, jimmy, Lilly
John, linda, Lilly
John, Lilly, linda
John, John, linda
Lilly, John, Lilly
Lilly, linda, Lilly
John, linda, John
John, John, Lilly
John, linda, John
Lilly, John, John
John, linda, Lilly
John, John, linda
John, John, John
John, Lilly, John
John, linda, John
John, Lilly, Lilly
Lilly, linda, Lilly])
np.votescount(a)