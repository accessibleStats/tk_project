"""
Statistics using Poisson Distribution

Jack Nickelson

"""


from tkinter import *
import tkinter as tk

########## Poisson Statistics #################
#### modeling rare events ######
def fact(x):
    x = float(x)
    if x < 0:
        return 1
    elif x == 0:
        return 1
    else:
        return x * fact(x-1)
# run the program, collect variable information
def run_program():
    ex_lam = float(ex_success.get())
    x_ = float(x_var.get())
    base_e = 2.71828
    # functions to calculate probability of an occurance
    def p_exact(ex_lam,x_,base_e):
        return round((base_e**-ex_lam*ex_lam**x_)/fact(x_),6)
    def at_least_one(ex_lam,x_,base_e):
        x_ = 0
        return round(1 - p_exact(ex_lam,x_,base_e),6)
    # Store the solution
    solution_exact = p_exact(ex_lam,x_,base_e)
    solution_at_least_one = at_least_one(ex_lam,x_,base_e)
    # display the solution in the results box
    calculation = selection_1.get()   
    if calculation ==  'Exactly X Occurances':
        results.delete(0, END)
        results.insert(0, "The probability of exactly {} successes (failures) with a likelihood of {} occurance is: {}".format(x_, ex_lam, solution_exact))
    if calculation ==  'At least 1 Occurance':
        results.delete(0, END)
        results.insert(0, "The probability of at least one occurance with a likelihood of {} occurance is: {}".format(ex_lam, solution_at_least_one))
 
# window information
bi_win = tk.Tk()
bi_win.title("Poisson Statistics")
bi_win.geometry("1100x410")
bi_win['bg']= '#7b9cd1'
# Welcome label
welcome_label = tk.Label(bi_win, text="Poisson Statistics", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',17))
# execution button
calc_button=tk.Button(bi_win, text="Calculate Poisson Statistics (Click Here)", command=run_program, font=('Helvetica',17), border=3)
# entry box for user input
ex_success=StringVar()
x_var=StringVar()
ex_success = tk.Entry(bi_win, width=5, font=('Helvetica',17), border=3)
x_var = tk.Entry(bi_win, width=5, font=('Helvetica',17), border=3)
results = tk.Entry(bi_win, width=95, font=('Helvetica',17), border=3)
ex_success.insert(0, " ")
x_var.insert(0, " ")
results.insert(0, "The results will appear here!")
# labels
ex_success_lab=tk.Label(bi_win, text='Prob of X Success(Failure) (lambda)', font=('Helvetica',17), relief=RAISED, bg='#fee3b5')
x_var_lab=tk.Label(bi_win, text='Occurances of X', font=('Helvetica',17), relief=RAISED, bg='#fee3b5')

# options drop down menu
selection_1=StringVar()
selection_1.set('Exactly X Occurances')
option_sel = tk.OptionMenu(bi_win, selection_1, 'Exactly X Occurances', 'At least 1 Occurance')

# placement
welcome_label.grid(row=0, padx=50, pady=10)
option_sel.grid(row=1, pady=5)
ex_success_lab.grid(row=2, pady=5)
ex_success.grid(row=3, pady=5)
x_var_lab.grid(row=4, pady=5)
x_var.grid(row=5, pady=5)
calc_button.grid(row=6, padx=50, pady=10)
results.grid(row=7, pady=10, padx=50)

#run program
bi_win.mainloop()

