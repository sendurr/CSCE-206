# Author: Daniel Harper
# Assignment: Homework4 - P1.py
# Original Date: 03/24/2016
# Last Updated:  03/25/2016
# Written using Python 3.4.3.7
# All rights reserved
#####################################################################
# Importation Section################################################
#from math import * # basic math functions
#from cmath import * # complex math (solve for algebra equations)
#import random # random number generator
#import matplotlib.pyplot as plt # plotting library
#from numpy import * # arrays, linspaces, most math functions
#import operator # used in sorting dictionaries
#import sys # take input from command line
#import argparse # store input from command line
from Tkinter import * # import the Tkiter (tool box) library
# Body Section#######################################################
#--------------------------------------------------------------------

# Develop a simple calculator using Tkinter package with the 
# following requirement (check the guitest.py example code for
# reference) It allows users to input 2 number. It has 4 buttons
# corresponding to +, -,*,/. When the user input 2 number, and click
# one of the button, the result should be shown on the screen

class Calculator:
	def __init__(self, master):
		self.master = master
		master.title("Calculator")

		self.total = 0 # number that is printed on the screen
		self.first_number = 0.0 # variable for the first number
		self.second_number = 0.0 # variable for the second number

		# ITEM DECLARATION///////////////////////////////////////////
		# Wrap the validation functions
		vcmd1 = master.register(self.validate1)

		vcmd2 = master.register(self.validate2)

		# Text/Number input fields
		self.input1 = Entry(master, validate="key", validatecommand=(vcmd1, "%P")) # input for the first number
        
		self.input2 = Entry(master, validate="key", validatecommand=(vcmd2, "%P")) # input for the second number
		# '%P' is the regex code for new input, if changed the calculator inputs get a bit wacky
        
        # Buttons
		self.button_add = Button(master, text ="+", command = lambda: self.add())
        
		self.button_sub = Button(master, text ="-", command = lambda: self.sub())
        
		self.button_mul = Button(master, text ="*", command = lambda: self.mul())
        
		self.button_div = Button(master, text ="/", command = lambda: self.div())

		# Total Line and Label
		self.label = Label(master, text="Result = ")
		self.total_text = IntVar()
		self.total_text.set(self.total)
		self.total_label = Label(master, textvariable=self.total_text)

		# ITEM LAYOUT////////////////////////////////////////////////
		self.input1.grid(row=0, column=0, columnspan=5)
		self.input2.grid(row=0, column=5, columnspan=5)
		self.button_add.grid(row=1, column=0)
		self.button_sub.grid(row=1, column=3)
		self.button_mul.grid(row=1, column=5)
		self.button_div.grid(row=1, column=9)
		self.label.grid(row=2, column=0, sticky=W)
		self.total_label.grid(row=2, column=9, columnspan=2, sticky=E)

	# INTERNAL FUNCTION DECLARATION//////////////////////////////////

	def greet(self):
		print("Greetings!")

	def add(self):
		self.total = self.first_number + self.second_number
		self.total_text.set(self.total)
		# print("total:",self.total)
		# print("first:",self.first_number)
		# print("second:",self.second_number)

	def sub(self):
		self.total = self.first_number - self.second_number
		self.total_text.set(self.total)
		# print("total:",self.total)
		# print("first:",self.first_number)
		# print("second:",self.second_number)

	def mul(self):
		self.total = self.first_number * self.second_number
		self.total_text.set(self.total)
		# print("total:",self.total)
		# print("first:",self.first_number)
		# print("second:",self.second_number)

	def div(self):
		if self.second_number == 0:
			self.total = 0
			self.total_text.set(self.total)
		else:
			self.total = self.first_number / self.second_number
			self.total_text.set(self.total)
		# print("total:",self.total)
		# print("first:",self.first_number)
		# print("second:",self.second_number)

	def validate1(self, new_text):
		if not new_text: # the field is being cleared
			self.first_number = 0.0
			return True
		
		try:
			self.first_number = float(new_text)
			return True
		except ValueError:
			return False

	def validate2(self, new_text):
		if not new_text: # the field is being cleared
			self.second_number = 0.0
			return True

		try:	
			self.second_number = float(new_text)
			return True
		except ValueError:
			return False
#--------------------------------------------------------------------
root = Tk()
my_gui = Calculator(root)
root.mainloop()