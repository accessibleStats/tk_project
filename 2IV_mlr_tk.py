"""

2 Independent Variables (with decimals)

Tkinter multiple regression using numpy

Jack Nickelson

"""


from tkinter import *
import tkinter as tk
import numpy as np

####### Multiple Regression##########
#def multiple_regression():
# Estimating regression model using numpy linear algebra

def userinputx():
    x1 = [float(x) for x in x_varnum.get().split(' ')]
    x1 = np.array(x1)
    x1 = x1.astype(np.float64)
    x1 = x1[...,None]
    x2 = [float(x) for x in x2_varnum.get().split(' ')]
    x2 = np.array(x2)
    x2 = x2.astype(np.float64)
    x2 = x2[...,None]
    x_matrix = np.concatenate((x1, x2), axis=1)
    return x_matrix
##### Y variable
def userinputy():    
    y = [float(y) for y in y_varnum.get().split(' ')]
    y = np.array(y)
    y = y.astype(np.float64)
    y = y[...,None]
    return y
    #y_float = y_array.astype(np.float64)

# function calls userinput function, transforms concatenated arrays into np.matrix
def xmatrix():
    xmatrix = userinputx()
    xmatrix = np.matrix(xmatrix)
    return xmatrix

# function calls userinput function, transforms concatenated arrays into np.matrix
def ymatrix():
    ymatrix = userinputy()
    ymatrix = np.matrix(ymatrix)
    return ymatrix

# main function calls x and y matrix functions, calculates the transpose of X matrix for linear algebra derrivation of predicted beta values
def multiple_reg():
    X = xmatrix()
    Y = ymatrix()
    X = np.insert(X, 0, 1, axis=1)
    xtranspose = X.getT()
    beta_hat = np.linalg.inv(xtranspose.dot(X)).dot(xtranspose).dot(Y)
    beta_hat=np.array(beta_hat)
    beta_hat=beta_hat[None,...]
    beta_zero=beta_hat[0,0]
    beta_one=beta_hat[0,1]
    beta_two=beta_hat[0,2]
    print(type(beta_hat))
    print(beta_zero)
    print(beta_one)
    print(beta_two)
    display.insert(0, "Y = {}+ {}X_1 + {}X_2".format(beta_zero,beta_one,beta_two))


# main window information
mlwindow=tk.Tk()
mlwindow.title("Multiple Linear Regression")
mlwindow.geometry("800x800")
mlwindow['bg']= "#cfe2f3"

"""
# menu for different number independent variables
#num_ind_vars=StringVar(mlwindow)
#num_ind_vars.set("Two")
#, num_ind_vars, 'One', 'Two', 'Three', 'Four', 'Five', 'Six')
drop_menu=tk.Menu(mlwindow)
mlwindow.config(menu=drop_menu)
menu_ops=Menu(drop_menu, tearoff=0)
drop_menu.add_cascade(label="Num Independent Variables", menu=menu_ops)
drop_menu.add_cascade(label="File", menu=menu_ops)
"""

# Labels for user input
welcome_label=tk.Label(mlwindow, text="Welcome to the Multiple Linear Relationship estimator: Input the values for X and Y (separate with spacebar)", pady=10, padx=30, relief=RAISED, borderwidth=15)
x_varLabel=tk.Label(mlwindow, text="Enter the values for X1:", pady=10, padx=30, relief=RAISED, borderwidth=15)
x2_varLabel=tk.Label(mlwindow, text="Enter the values for X2:", pady=10, padx=30, relief=RAISED, borderwidth=15)    
y_varLabel=tk.Label(mlwindow, text="Enter the values for Y:", pady=10, padx=30, relief=RAISED, borderwidth=15)
display_Label=tk.Label(mlwindow, text="The estimated relationship is:", pady=10, padx=30, relief=RAISED, borderwidth=15, width=25)

# Entry boxes for user input
x_varnum=StringVar()
x2_varnum=StringVar()

y_varnum=StringVar()
# Entry boxes for user input
x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=15)
x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=15)
y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=15)

# Button to generate Z score
simplebtn=tk.Button(mlwindow, text="Calculate Linear Relationship", command=multiple_reg, relief=RAISED, borderwidth=15, highlightbackground="blue")
# Display box
display=tk.Entry(mlwindow, relief=RAISED, bd=5, borderwidth=10, highlightbackground="blue", width=70)
# Locations
welcome_label.grid(row=0, columnspan=2)
x_varLabel.grid(row=1, column=0)
x_varnum.grid(row=1, column=1)
x2_varLabel.grid(row=2, column=0)
x2_varnum.grid(row=2, column=1) 
y_varLabel.grid(row=7, column=0)
y_varnum.grid(row=7, column=1)
simplebtn.grid(row=8, column=1)
display_Label.grid(row=8, column=0)
display.grid(row=9, columnspan=2)
##########################################

mlwindow.mainloop()