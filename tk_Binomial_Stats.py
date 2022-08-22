"""
Binomial Stats Program
"""


import tkinter as tk



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
    n = int(trials.get())
    p = float(prob_success.get())
    k = int(num_success.get())
    def p_exact(n,p,k):
        return round(fact(n) / (fact(k) * fact(n - k)) * (p**k) * (1-p)**(n - k),6)
    def at_least(n,p,k):
        sol = 0
        while k <= n:
            sol += p_exact(n,p,k)
            k += 1
        return round(sol,6)
    def more_than(n,p,k):
        n = n
        p = p
        k = k+1
        sol = 0
        while k <= n:
            sol += p_exact(n,p,k)
            k += 1
        return round(sol,6)   
    def at_most(n,p,k):
        n = n
        p = p
        k = k
        sol = 0
        while k >= 0:
            sol += p_exact(n,p,k)
            k -= 1
        return round(sol,6)
    def less_than(n,p,k):
        n = n
        p = p
        k = k-1
        sol = 0
        while k >= 0:
            sol += p_exact(n,p,k)
            k -= 1
        return round(sol,6)


    # calculate and store solutions
    solution_exact = p_exact(n,p,k)
    solution_at_least = at_least(n,p,k)
    solution_more_than = more_than(n,p,k)
    solution_at_most = at_most(n,p,k)
    solution_less_than = less_than(n,p,k)

    # print solutions in display box
    calculation = selection_1.get()
    if calculation == 'At least K successes':
        results.delete(0, tk.END) 
        results.insert(0, "In {} trials, the probability of at least {} win(s) is: {}".format(n, k, solution_at_least))
    elif calculation ==  'Exactly K successes':
        results.delete(0, tk.END)
        results.insert(0, "In {} trials, the probability of exactly {} win(s) is: {}".format(n, k, solution_exact))
    elif calculation == 'At most K successes':
        results.delete(0, tk.END)
        results.insert(0, "In {} trials, the probability of at most {} win(s) is: {}".format(n, k, solution_at_most))
    elif calculation == 'Less than K successes':
        results.delete(0, tk.END)
        results.insert(0, "In {} trials, the probability of less than {} win(s) is: {}".format(n, k, solution_less_than))
    elif calculation == 'More than K successes':
        results.delete(0, tk.END)
        results.insert(0, "In {} trials, the probability of more than {} win(s) is: {}".format(n, k, solution_more_than))
    else:
        return


# main window information

main_win = tk.Tk()
main_win.title("Binomial Statistics")
main_win.geometry("800x700")
main_win['bg']= '#7b9cd1'

# Welcome label
welcome_label = tk.Label(main_win, text="Binomial Statistics", pady=10, padx=30, relief=tk.RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',17))
# execution button
calc_button=tk.Button(main_win, text="Calculate Binomial Statistics (Click Here)", command=run_program, font=('Helvetica',17), border=3)

# entry box for user input
trials=tk.StringVar()
prob_success=tk.StringVar()
num_success=tk.StringVar()
trials = tk.Entry(main_win, width=5, font=('Helvetica',17), border=3)
prob_success = tk.Entry(main_win, width=5, font=('Helvetica',17), border=3)
num_success = tk.Entry(main_win, width=5, font=('Helvetica',17), border=3)
results = tk.Entry(main_win, width=65, font=('Helvetica',17), border=3)
trials.insert(0, " ")
prob_success.insert(0, " ")
num_success.insert(0, " ")
results.insert(0, "The results will appear here!")

# labels
trials_lab=tk.Label(text='Events: N', font=('Helvetica',17), relief=tk.RAISED, bg='#fee3b5')
prob_success_lab=tk.Label(text='Prob of Success: P', font=('Helvetica',17), relief=tk.RAISED, bg='#fee3b5')
num_success_lab=tk.Label(text='Num of Successes: K', font=('Helvetica',17), relief=tk.RAISED, bg='#fee3b5')

# options drop down menu
selection_1=tk.StringVar()
selection_1.set('At least K successes')
option_sel = tk.OptionMenu(main_win, selection_1, 'At least K successes', 'Exactly K successes', 'At most K successes', 'Less than K successes', 'More than K successes')

# placement
welcome_label.grid(row=0, columnspan=2, padx=50, pady=10)
option_sel.grid(row=1, columnspan=2, pady=5)
trials_lab.grid(row=2, column=0, pady=5)
trials.grid(row=3, column=0, pady=5)
prob_success_lab.grid(row=2, column=1, pady=5)
prob_success.grid(row=3, column=1, pady=5)
num_success_lab.grid(row=4, column=1, pady=5)
num_success.grid(row=5, column=1, pady=5)
calc_button.grid(row=6, columnspan=2, padx=50, pady=10)
results.grid(row=7, columnspan=2, pady=10, padx=50)


# open main window
main_win.mainloop()








