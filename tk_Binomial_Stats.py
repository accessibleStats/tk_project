"""
Binomial Statistics Program

By: Jack Nickelson

"""

from tkinter import *
import tkinter as tk
#import numpy as np
#import statistics

class Univariate:
    """class for univariate exploration"""
    def __init__(self, trials, probability, successes):
        return

def calculate_stats():
    return

# main window information

main_win = tk.Tk()
main_win.title("Binomial Statistics")
main_win.geometry("600x700")
main_win['bg']= '#7b9cd1'

# Welcome label
welcome_label = tk.Label(main_win, text="Binomial Statistics", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',17))
# execution button
calc_button=tk.Button(main_win, text="Calculate Binomial Statistics (Click Here)", command=calculate_stats, font=('Helvetica',17))

# entry box for user input
trials=StringVar()
prob_success=StringVar()
num_success=StringVar()
trials = tk.Entry(main_win, width=45, font=('Helvetica',17))
prob_success = tk.Entry(main_win, width=45, font=('Helvetica',17))
num_success = tk.Entry(main_win, width=45, font=('Helvetica',17))
# labels
trials_lab=tk.Label(text='Enter Trials:')
prob_success_lab=tk.Label(text='Enter Prob of Success:')
num_success_lab=tk.Label(text='Enter Num of Successes:')

# placement
welcome_label.grid(row=0, padx=50, pady=10)
trials_lab.grid(row=1, pady=10)
trials.grid(row=2, padx=50, pady=10)
prob_success_lab.grid(row=3, pady=10)
prob_success.grid(row=4, pady=10)
num_success_lab.grid(row=5, pady=10)
num_success.grid(row=6, pady=10)
calc_button.grid(row=10, padx=50, pady=10)


# open main window
main_win.mainloop()