"""
Univariate Descriptive Statistics Program

This program is used to generate univariate descriptive statistics. The user enters data separated by a comma. 
The program then return useful information.
"""

import tkinter as tk
import numpy as np
from statistics import multimode, variance, stdev

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
        self.mode = multimode(userdata)
        self.var = variance(userdata)
        self.std = stdev(userdata)
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
    meanvalue.delete(0,tk.END)
    medianvalue.delete(0,tk.END)
    modevalue.delete(0,tk.END)
    variancevalue.delete(0,tk.END)
    standarddev.delete(0,tk.END)
    quartilevalues_in.delete(0,tk.END)
    iqr_in.delete(0,tk.END)
    outliers.delete(0,tk.END)
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
main_win.geometry("600x700")
main_win['bg']= '#7b9cd1'

# Welcome label
welcome_label = tk.Label(main_win, text="Univariate Descriptive Statistics", pady=10, padx=30, relief=tk.RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',17))
# execution button
calc_button=tk.Button(main_win, text="Calculate Univariate Statistics (Click Here)", command=calculate_stats, font=('Helvetica',17))

# entry box for user input
x_values=tk.StringVar()
x_values = tk.Entry(main_win, width=45, font=('Helvetica',17))
meanvalue= tk.Entry(main_win, width=45, font=('Helvetica',17))
medianvalue= tk.Entry(main_win, width=45, font=('Helvetica',17))
modevalue= tk.Entry(main_win, width=45, font=('Helvetica',17))
variancevalue= tk.Entry(main_win, width=45, font=('Helvetica',17))
standarddev= tk.Entry(main_win, width=45, font=('Helvetica',17))
quartilevalues_in= tk.Entry(main_win, width=45, font=('Helvetica',17))
iqr_in= tk.Entry(main_win, width=45, font=('Helvetica',17))
outliers= tk.Entry(main_win, width=45, font=('Helvetica',17))
x_values.insert(0,"Enter values for descriptive stats (separate with , )")
meanvalue.insert(0,"The mean will appear here!")
medianvalue.insert(0,"The median value will appear here!")
modevalue.insert(0,"The mode will appear here!")
variancevalue.insert(0,"The variance will appear here!")
standarddev.insert(0,"The standard deviation will appear here!")
quartilevalues_in.insert(0,"The inclusive quartiles will appear here!")
iqr_in.insert(0,"The inclusive IQR will appear here!")
outliers.insert(0,"The outliers using IQR*1.5 will appear here!")
# placement
welcome_label.grid(row=0, padx=50, pady=10)
x_values.grid(row=1, padx=50, pady=10)
calc_button.grid(row=2, padx=50, pady=10)
meanvalue.grid(row=3, padx=50, pady=10)
medianvalue.grid(row=4, padx=50, pady=10)
modevalue.grid(row=5, padx=50, pady=10)
variancevalue.grid(row=6, padx=50, pady=10)
standarddev.grid(row=7, padx=50, pady=10)
quartilevalues_in.grid(row=8, padx=50, pady=10)
iqr_in.grid(row=9, padx=50, pady=10)
outliers.grid(row=10, padx=50, pady=10)

# open main window
main_win.mainloop()
