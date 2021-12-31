"""
Univariate Descriptive Statistics Program

By: Jack Nickelson

This program is used to automate the calcualtion of univariate descriptive statistics. The user enters data separated by a comma. 
The program then return useful univariate statistics. This program is an attempt at using classes
"""

from tkinter import *
import tkinter as tk
import numpy as np
import statistics

class Univariate:
    """class for univariate exploration"""
    def __init__(self, userdata):
        self.userdata = []
        self.mean = int(sum(int(x) for x in userdata))/len(userdata)
        self.sort = sorted(userdata)
        self.length = len(userdata)
        self.midpoint = (self.length -1) // 2 
        if (self.length % 2): 
            self.median = (self.sort[self.midpoint]) 
        else: 
            self.median = (self.sort[self.midpoint] + self.sort[self.midpoint +1])/2 
        self.mode = statistics.multimode(userdata)
        self.var = statistics.variance(userdata)
        self.std = statistics.stdev(userdata)
        self.first_quantile_in = np.quantile(userdata, .25)
        self.third_quantile_in = np.quantile(userdata, .75)
        self.iqr_in = self.third_quantile_in - self.first_quantile_in
        self.upper = self.third_quantile_in + (self.iqr_in * 1.5)
        self.lower = self.first_quantile_in - (self.iqr_in * 1.5)
        self.outliers = "The outliers are below {} or above {}.".format(self.lower,self.upper)

def calculate_stats():
    x_var = [int(x) for x in x_values.get().split(',')]
    x_var = Univariate(x_var)
    # clear entry boxes of text with each click
    meanvalue.delete(0,END)
    medianvalue.delete(0,END)
    modevalue.delete(0,END)
    variancevalue.delete(0,END)
    standarddev.delete(0,END)
    quartilevalues_in.delete(0,END)
    iqr_in.delete(0,END)
    outliers.delete(0,END)
    # insert values into entry boxes
    meanvalue.insert(0,"Mean = {}".format(x_var.mean))
    medianvalue.insert(0, "Median = {}".format(x_var.median))
    modevalue.insert(0, "Mode = {}".format(x_var.mode))
    variancevalue.insert(0, "Variance = {}".format(x_var.var))
    standarddev.insert(0, "Standard Deviation = {}".format(x_var.std))
    quartilevalues_in.insert(0, "Inclusive Quartiles: Q1 = {}, Q2 = {}, Q3 = {}".format(x_var.first_quantile_in, x_var.median, x_var.third_quantile_in))
    iqr_in.insert(0, "Inclusive IQR = {}".format(x_var.iqr_in))
    outliers.insert(0, "{}".format(x_var.outliers))
    print(type(x_var))
    print(x_var)
    

# main window information
main_win = tk.Tk()
main_win.title("Univariate Descriptive Statistics")
main_win.geometry("450x425")
main_win['bg']= '#7b9cd1'

# Frame
#main_frame=Frame(main_win,bg="#000614")
#main_frame.grid(row=0, column=0, sticky="NESW")
#main_frame.grid_rowconfigure(0, weight=1)
#main_frame.grid_columnconfigure(0, weight=1)
#main_win.grid_rowconfigure(0, weight=1)
#main_win.grid_columnconfigure(0, weight=1)

# Welcome label
welcome_label = tk.Label(main_win, text="Welcome to the univariate descriptive statistics generator!", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fee3b5')
# execution button
calc_button=tk.Button(main_win, text="Calculate Univariate Statistics (Click Here)", command=calculate_stats)

# entry box for user input
x_values=StringVar()
x_values = tk.Entry(main_win, width=45)
meanvalue= tk.Entry(main_win, width=45)
medianvalue= tk.Entry(main_win, width=45)
modevalue= tk.Entry(main_win, width=45)
variancevalue= tk.Entry(main_win, width=45)
standarddev= tk.Entry(main_win, width=45)
quartilevalues_in= tk.Entry(main_win, width=45)
iqr_in= tk.Entry(main_win, width=45)
outliers= tk.Entry(main_win, width=45)
x_values.insert(0,"Enter values for descriptive stats (separate with a comma)")
meanvalue.insert(0,"The mean will appear here!")
medianvalue.insert(0,"The median value will appear here!")
modevalue.insert(0,"The mode will appear here!")
variancevalue.insert(0,"The variance will appear here!")
standarddev.insert(0,"The standard deviation will appear here!")
quartilevalues_in.insert(0,"The inclusive quartiles will appear here!")
iqr_in.insert(0,"The inclusive IQR will appear here!")
outliers.insert(0,"The outliers using IQR*1.5 will appear here!")
# placement
welcome_label.grid(row=0)
x_values.grid(row=1)
calc_button.grid(row=2)
meanvalue.grid(row=3)
medianvalue.grid(row=4)
modevalue.grid(row=5)
variancevalue.grid(row=6)
standarddev.grid(row=7)
quartilevalues_in.grid(row=8)
iqr_in.grid(row=9)
outliers.grid(row=10)

# open main window
main_win.mainloop()