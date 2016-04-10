# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 20:57:50 2016

@author: Tret Burdette
"""

from Tkinter import *
root = Tk()
n1_entry=Entry(root,width=4)
n1_entry.pack(side='left')
n2_entry=Entry(root,width=4)
n2_entry.pack(side='left')
def add():
	n1=float(n1_entry.get())
	n2=float(n2_entry.get())
	Result=n1+n2
	Result_label.configure(text='%g'%Result)
add=Button(root,text='+',command=add)
add.pack(side='left',padx=4)
def sub():
	n1=float(n1_entry.get())
	n2=float(n2_entry.get())
	Result=n1-n2
	Result_label.configure(text='%g'%Result)
sub=Button(root,text='-',command=sub)
sub.pack(side='left',padx=4)
def mult():
	n1=float(n1_entry.get())
	n2=float(n2_entry.get())
	Result=n1*n2
	Result_label.configure(text='%g'%Result)
mult=Button(root,text='*',command=mult)
mult.pack(side='left',padx=4)
def div():
	n1=float(n1_entry.get())
	n2=float(n2_entry.get())
	Result=n1/n2
	Result_label.configure(text='%g'%Result)
div=Button(root,text='/',command=div)
div.pack(side='left',padx=4)

Result_label=Label(root,width=4)
Result_label.pack(side='right')
Resultunit_label=Label(root,text='Result=')
Resultunit_label.pack(side='left')
root.mainloop()