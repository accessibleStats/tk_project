"""

Statistics Application with tkinter graphical user interface
Find Z scores, X values for given Z scores, simple, and multiple regression estimation

Jack Nickelson
"""

from tkinter import *
import tkinter as tk
import numpy as np
from numpy import sqrt

####### Simple linear regression ##########
def simple_linear():
# Calculating simple linear regression
    def simple_linear():
        x_var = [float(x) for x in x_varnum.get().split(',')]
        y_var = [float(y) for y in y_varnum.get().split(',')]
        x_array = np.array([x_var])
        y_array = np.array([y_var])
        x_mean = x_array.mean()
        y_mean = y_array.mean()
        x_distfrommean = x_array - x_mean
        y_distfrommean = y_array - y_mean
        ssx = np.sum(np.power(x_distfrommean,2))
        ssy = np.sum(np.power(y_distfrommean,2))
        sumxyproducts = np.sum(x_distfrommean * y_distfrommean)    
        beta1 = round(sumxyproducts / ssx,4)
        beta0 = round(y_mean - (beta1*x_mean),4)
        correlationcoefficient = round(sumxyproducts / np.sqrt(ssx*ssy),4)
        r_squared=round(correlationcoefficient**2,4)
        # clear display text box with each click and then display results
        display_reg_eq.delete(0,END)
        display_r.delete(0,END)
        display_r_sq.delete(0,END)
        display_reg_eq.insert(0, "Y = {} + {}X".format(beta0, beta1))
        display_r.insert(0, "Correlation r = {}".format(correlationcoefficient))
        display_r_sq.insert(0, "R Squared = {}".format(r_squared))
    slwindow=tk.Toplevel()
    slwindow.title("Simple Linear Regression")
    slwindow.geometry("800x500")
    slwindow['bg']= "#cfe2f3"
    # Labels for user input
    welcome_label=tk.Label(slwindow, text="Welcome to the Simple Linear Relationship estimator: Input the values for X and Y (separate with a comma)", pady=10, padx=30, relief=RAISED, borderwidth=10, bg='#fff2cc')
    # Entry boxes for user input
    x_varnum=tk.Entry(slwindow, relief=RAISED, bd=5, width=30)
    y_varnum=tk.Entry(slwindow, relief=RAISED, bd=5, width=30)
    x_varnum.insert(0, "Enter the values for X")
    y_varnum.insert(0,"Enter values for Y")
    # Button to generate Z score
    simplebtn=tk.Button(slwindow, text="Estimate Regression Equation (Click Here)", command=simple_linear, highlightbackground="gray")
    # Display box
    display_reg_eq=tk.Entry(slwindow, highlightbackground="gray", width=40)
    display_r=tk.Entry(slwindow, highlightbackground="gray", width=40)
    display_r_sq=tk.Entry(slwindow, highlightbackground="gray", width=40)
    display_reg_eq.insert(0,"The estimated regression equation will appear here!")
    display_r.insert(0,"The estimated correlation r will appear here!")
    display_r_sq.insert(0,"The estimated r-squared will appear here!")
    # Locations
    welcome_label.grid(row=0)
    x_varnum.grid(row=1)
    y_varnum.grid(row=2)
    simplebtn.grid(row=3)
    display_reg_eq.grid(row=4)
    display_r.grid(row=5)
    display_r_sq.grid(row=6)
##########################################

######## Multiple Linear Regression (2 independent variables)
# Estimating regression model using numpy linear algebra
def multiple_regression2():
    def userinputx():
        x1 = [float(x) for x in x_varnum.get().split(',')]
        x1 = np.array(x1)
        x1 = x1.astype(np.float64)
        x1 = x1[...,None]
        x2 = [float(x) for x in x2_varnum.get().split(',')]
        x2 = np.array(x2)
        x2 = x2.astype(np.float64)
        x2 = x2[...,None]
        x_matrix = np.concatenate((x1, x2), axis=1)
        return x_matrix
    ##### Y variable
    def userinputy():    
        y = [float(y) for y in y_varnum.get().split(',')]
        y = np.array(y)
        y = y.astype(np.float64)
        y = y[...,None]
        return y

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
        # store estimated coefficients
        beta_zero=beta_hat[0,0]
        beta_one=beta_hat[0,1]
        beta_two=beta_hat[0,2]
        # round coefficients to 4 decimal places
        beta_zero=np.float64(beta_zero)
        beta_zero=round(beta_zero,4)
        beta_one=np.float64(beta_one)
        beta_one=round(beta_one,4)
        beta_two=np.float64(beta_two)
        beta_two=round(beta_two,4)
        # clear display text box with each click and then display results
        display.delete(0,END)
        display.insert(0, "Y = {}+ {}X_1 + {}X_2".format(beta_zero,beta_one,beta_two))


    # main window information
    mlwindow=tk.Toplevel()
    mlwindow.title("Multiple Linear Regression")
    mlwindow.geometry("800x400")
    mlwindow['bg']= "#cfe2f3"

    # Labels for user input
    welcome_label=tk.Label(mlwindow, text="Welcome to the Multiple Linear Relationship estimator: Input the values for X and Y (separate with comma)", pady=10, padx=30, relief=RAISED, borderwidth=10, bg='#fff2cc')
    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=5)
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=5)
    y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=5)
    x_varnum.insert(0, "Enter values for X_1")
    x2_varnum.insert(0, "Enter values for X_2")
    y_varnum.insert(0, "Enter values for Y")

    # Button to regression coefficients
    simplebtn=tk.Button(mlwindow, text="Estimate the regression equation (Click Here)", command=multiple_reg, borderwidth=5)
    # Display box
    display=tk.Entry(mlwindow, relief=RAISED, bd=5, borderwidth=5, highlightbackground="#cfe2f3", width=70)
    display.insert(0,"The estimated regression equation will appear here!")
    # Locations
    welcome_label.grid(row=0)
    x_varnum.grid(row=1)
    x2_varnum.grid(row=2) 
    y_varnum.grid(row=7)
    simplebtn.grid(row=8)
    display.grid(row=9)
##########################################

######## Multiple Linear Regression (3 independent variables)
# Estimating regression model using numpy linear algebra
def multiple_regression3():
    def userinputx():
        x1 = [float(x) for x in x_varnum.get().split(',')]
        x1 = np.array(x1)
        x1 = x1.astype(np.float64)
        x1 = x1[...,None]
        x2 = [float(x) for x in x2_varnum.get().split(',')]
        x2 = np.array(x2)
        x2 = x2.astype(np.float64)
        x2 = x2[...,None]
        x3 = [float(x) for x in x3_varnum.get().split(',')]
        x3 = np.array(x3)
        x3 = x3.astype(np.float64)
        x3 = x3[...,None]
        x_matrix = np.concatenate((x1, x2, x3), axis=1)
        return x_matrix
    ##### Y variable
    def userinputy():    
        y = [float(y) for y in y_varnum.get().split(',')]
        y = np.array(y)
        y = y.astype(np.float64)
        y = y[...,None]
        return y

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
        beta_three=beta_hat[0,3]
        # round coefficients to 4 decimal places
        beta_zero=np.float64(beta_zero)
        beta_zero=round(beta_zero,4)
        beta_one=np.float64(beta_one)
        beta_one=round(beta_one,4)
        beta_two=np.float64(beta_two)
        beta_two=round(beta_two,4)
        beta_three=np.float64(beta_three)
        beta_three=round(beta_three,4)
        # clear display text box with each click and then display results
        display.delete(0,END)
        display.insert(0, "Y = {}+ {}X_1 + {}X_2 + {}X_3".format(beta_zero,beta_one,beta_two,beta_three))

    # main window information
    mlwindow=tk.Toplevel()
    mlwindow.title("Multiple Linear Regression")
    mlwindow.geometry("800x400")
    mlwindow['bg']= "#cfe2f3"

    # Labels for user input
    welcome_label=tk.Label(mlwindow, text="Welcome to the Multiple Linear Relationship estimator: Input the values for X and Y (separate a comma)", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    x3_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=5)
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=5)
    x3_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=5)
    y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=5)
    # text inside of entry boxes
    x_varnum.insert(0,"Enter the values for X1")
    x2_varnum.insert(0,"Enter the values for X2")
    x3_varnum.insert(0,"Enter the values for X3")
    y_varnum.insert(0,"Enter the values for Y")
    # Button to estimate regression equation
    simplebtn=tk.Button(mlwindow, text="Estimate Regression Equation (Click Here)", command=multiple_reg, relief=RAISED, borderwidth=10)
    # Display box
    display=tk.Entry(mlwindow, relief=RAISED, bd=5, borderwidth=5, highlightbackground="#cfe2f3", width=70)
    display.insert(0,"The estimated regression equation will appear here!")
    # Locations
    welcome_label.grid(row=0)
    x_varnum.grid(row=1)
    x2_varnum.grid(row=2) 
    x3_varnum.grid(row=3) 
    y_varnum.grid(row=7)
    simplebtn.grid(row=8)
    display.grid(row=9)
##########################################
##########################################

######## Multiple Linear Regression (4 independent variables)
# Estimating regression model using numpy linear algebra
def multiple_regression4():
    def userinputx():
        x1 = [float(x) for x in x_varnum.get().split(',')]
        x1 = np.array(x1)
        x1 = x1.astype(np.float64)
        x1 = x1[...,None]
        x2 = [float(x) for x in x2_varnum.get().split(',')]
        x2 = np.array(x2)
        x2 = x2.astype(np.float64)
        x2 = x2[...,None]
        x3 = [float(x) for x in x3_varnum.get().split(',')]
        x3 = np.array(x3)
        x3 = x3.astype(np.float64)
        x3 = x3[...,None]
        x4 = [float(x) for x in x4_varnum.get().split(',')]
        x4 = np.array(x4)
        x4 = x4.astype(np.float64)
        x4 = x4[...,None]
        x_matrix = np.concatenate((x1, x2, x3, x4), axis=1)
        return x_matrix
##### Y variable
    def userinputy():    
        y = [float(y) for y in y_varnum.get().split(',')]
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
        beta_three=beta_hat[0,3]
        beta_four=beta_hat[0,4]
        # round coefficients to 4 decimal places
        beta_zero=np.float64(beta_zero)
        beta_zero=round(beta_zero,4)
        beta_one=np.float64(beta_one)
        beta_one=round(beta_one,4)
        beta_two=np.float64(beta_two)
        beta_two=round(beta_two,4)
        beta_three=np.float64(beta_three)
        beta_three=round(beta_three,4)
        beta_four=np.float64(beta_four)
        beta_four=round(beta_four,4)
        # clear display text box with each click and then display results
        display.delete(0,END)
        display.insert(0, "Y = {}+ {}X_1 + {}X_2 + {}X_3 + {}X_4".format(beta_zero,beta_one,beta_two,beta_three,beta_four))

    # main window information
    mlwindow=tk.Toplevel()
    mlwindow.title("Multiple Linear Regression")
    mlwindow.geometry("800x400")
    mlwindow['bg']= "#cfe2f3"

    # Labels for welcome label
    welcome_label=tk.Label(mlwindow, text="Welcome to the Multiple Linear Relationship estimator: Input the values for X and Y (separate with a comma)", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    x3_varnum=StringVar()
    x4_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=5)
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=5)
    x3_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=5)
    x4_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=5)
    y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=5)
    # text inside of entry boxes
    x_varnum.insert(0,"Enter the values for X1")
    x2_varnum.insert(0,"Enter the values for X2")
    x3_varnum.insert(0,"Enter the values for X3")
    x4_varnum.insert(0,"Enter the values for X4")
    y_varnum.insert(0,"Enter the values for Y")

    # Button to generate Z score
    simplebtn=tk.Button(mlwindow, text="Estimate Regression Equation (Click Here)", command=multiple_reg, relief=RAISED, borderwidth=5)
    # Display box
    display=tk.Entry(mlwindow, relief=RAISED, bd=5, borderwidth=10, highlightbackground="#cfe2f3", width=70)
    display.insert(0,"The estimated regression equation will appear here!")
    # Locations
    welcome_label.grid(row=0)
    x_varnum.grid(row=1)
    x2_varnum.grid(row=2) 
    x3_varnum.grid(row=3) 
    x4_varnum.grid(row=4) 
    y_varnum.grid(row=7)
    simplebtn.grid(row=8)
    display.grid(row=9)
##########################################
##########################################

######## Multiple Linear Regression (5 independent variables)
# Estimating regression model using numpy linear algebra
def multiple_regression5():
    def userinputx():
        x1 = [float(x) for x in x_varnum.get().split(',')]
        x1 = np.array(x1)
        x1 = x1.astype(np.float64)
        x1 = x1[...,None]
        x2 = [float(x) for x in x2_varnum.get().split(',')]
        x2 = np.array(x2)
        x2 = x2.astype(np.float64)
        x2 = x2[...,None]
        x3 = [float(x) for x in x3_varnum.get().split(',')]
        x3 = np.array(x3)
        x3 = x3.astype(np.float64)
        x3 = x3[...,None]
        x4 = [float(x) for x in x4_varnum.get().split(',')]
        x4 = np.array(x4)
        x4 = x4.astype(np.float64)
        x4 = x4[...,None]
        x5 = [float(x) for x in x5_varnum.get().split(',')]
        x5 = np.array(x5)
        x5 = x5.astype(np.float64)
        x5 = x5[...,None]
        x_matrix = np.concatenate((x1, x2, x3, x4, x5), axis=1)
        return x_matrix
    ##### Y variable
    def userinputy():    
        y = [float(y) for y in y_varnum.get().split(',')]
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
        beta_three=beta_hat[0,3]
        beta_four=beta_hat[0,4]
        beta_five=beta_hat[0,5]
        # round coefficients to 4 decimal places
        beta_zero=np.float64(beta_zero)
        beta_zero=round(beta_zero,4)
        beta_one=np.float64(beta_one)
        beta_one=round(beta_one,4)
        beta_two=np.float64(beta_two)
        beta_two=round(beta_two,4)
        beta_three=np.float64(beta_three)
        beta_three=round(beta_three,4)
        beta_four=np.float64(beta_four)
        beta_four=round(beta_four,4)
        beta_five=np.float64(beta_five)
        beta_five=round(beta_five,4)
        # clear display text box with each click and then display results
        display.delete(0,END)
        display.insert(0, "Y = {}+ {}X_1 + {}X_2 + {}X_3 + {}X_4 + {}X_5".format(beta_zero,beta_one,beta_two,beta_three,beta_four,beta_five))


    # main window information
    mlwindow=tk.Toplevel()
    mlwindow.title("Multiple Linear Regression")
    mlwindow.geometry("800x400")
    mlwindow['bg']= "#cfe2f3"

    # Label for welcome
    welcome_label=tk.Label(mlwindow, text="Welcome to the Multiple Linear Relationship estimator: Input the values for X and Y (separate with spacebar)", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    x3_varnum=StringVar()
    x4_varnum=StringVar()
    x5_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=5)
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=5)
    x3_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=5)
    x4_varnum=tk.Entry(mlwindow, textvariable=x4_varnum, relief=RAISED, bd=5, borderwidth=5)
    x5_varnum=tk.Entry(mlwindow, textvariable=x5_varnum, relief=RAISED, bd=5, borderwidth=5)
    y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=5)
    # text inside of entry boxes
    x_varnum.insert(0,"Enter the values for X1")
    x2_varnum.insert(0,"Enter the values for X2")
    x3_varnum.insert(0,"Enter the values for X3")
    x4_varnum.insert(0,"Enter the values for X4")
    x5_varnum.insert(0,"Enter the values for X5")
    y_varnum.insert(0,"Enter the values for Y")
    # Button to regression coefficients
    simplebtn=tk.Button(mlwindow, text="Estimate Regression Equation (Click Here)", command=multiple_reg, relief=RAISED, borderwidth=15, highlightbackground="#cfe2f3")
    # Display box
    display=tk.Entry(mlwindow, relief=RAISED, bd=5, borderwidth=10, width=70)
    display.insert(0,"The estimated regression equation will appear here!")
    # Locations
    welcome_label.grid(row=0)
    x_varnum.grid(row=1)
    x2_varnum.grid(row=2) 
    x3_varnum.grid(row=3)   
    x4_varnum.grid(row=4)  
    x5_varnum.grid(row=5)   
    y_varnum.grid(row=7)
    simplebtn.grid(row=8)
    display.grid(row=9)
###########################################

####### Z scores (solve for Z) ##########
def zscorefun():
    # Finding z score from sample mean, pop mean, pop standard deviation, and number of observations
    def findzscore():
        x_bar = float(x_barnum.get())
        mu = float(mu_num.get())
        standard = float(pop_standard_num.get())
        obs = float(obs_num.get())
        # round z score
        z_score = round((x_bar - mu) / (standard/sqrt(obs)),4)
        # clear display box with each click
        display.delete(0, END)
        display.insert(0, z_score)
    ### open window for Z score calculation
    zwindow=tk.Toplevel()
    zwindow.geometry("300x300")
    zwindow['bg']="#cfe2f3"    
    # Labels for welcome label
    welcomelabel=tk.Label(zwindow, text="Welcome to the Z score finder!", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    # Entry boxes for user input
    x_barnum=tk.Entry(zwindow, relief=RAISED, bd=5)
    mu_num=tk.Entry(zwindow, relief=RAISED, bd=5)
    pop_standard_num=tk.Entry(zwindow, relief=RAISED, bd=5)
    obs_num=tk.Entry(zwindow, relief=RAISED, bd=5)
    x_barnum.insert(0,"Enter the sample mean")
    mu_num.insert(0,"Enter the population mean")
    pop_standard_num.insert(0,"Enter the population sigma")
    obs_num.insert(0,"Enter the # of observations")
    # Button to generate Z score
    Zbtn=tk.Button(zwindow, text="Calculate Z (Click Here)", command=findzscore, highlightbackground="#cfe2f3")
    # Display Box
    display=tk.Entry(zwindow, width=30)
    display.insert(0,"The Z score will appear here!")
    #Locations
    welcomelabel.grid(row=0)
    x_barnum.grid(row=1)
    mu_num.grid(row=2)
    pop_standard_num.grid(row=3)
    obs_num.grid(row=4)
    Zbtn.grid(row=5)
    display.grid(row=6)
##########################################

####### Z scores (solve for X) ##########
def findxvaluefromz():
    # Finding z score from sample mean, pop mean, pop standard deviation
    def findxvalue():
        z_score = float(Zscorenum.get())
        mu = float(mu_num.get())
        standard = float(pop_standard_num.get())
        # round to four decimal places
        x_value = round((mu + standard*z_score),4)
        # clear display box with each click
        display.delete(0, END)
        display.insert(0, x_value)
    # open window for calculating X for a particular Z, pop mean, and pop standard deviation
    window=tk.Toplevel()
    window.title("Find X Given Z, mu, sigma")
    window.geometry("400x400")
    window['bg']="#cfe2f3"
    # Labels for welcome label
    welcomelabel=tk.Label(window, text="Welcome to the X finder!", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    # Entry boxes for user input
    Zscorenum=tk.Entry(window, relief=RAISED, bd=5)
    mu_num=tk.Entry(window, relief=RAISED, bd=5)
    pop_standard_num=tk.Entry(window, relief=RAISED, bd=5)
    Zscorenum.insert(0,"Enter the Z score")
    mu_num.insert(0,"Enter the population mean")
    pop_standard_num.insert(0,"Enter the population sigma")
    # Button to find X
    Xbtn=tk.Button(window, text="Calculate X Value (Click Here)", command=findxvalue, highlightbackground="#cfe2f3")
    # Display Box
    display=tk.Entry(window, width=30)
    display.insert(0,"The value for X will appear here!")
    #Locations
    welcomelabel.grid(row=0, columnspan=2) 
    Zscorenum.grid(row=1, column=1)
    mu_num.grid(row=2, column=1)
    pop_standard_num.grid(row=3, column=1)
    Xbtn.grid(row=4, column=1)
    display.grid(row=5, column=1)
##############################################

# Main program tk window. Functions are launched from the main window.
# options for main window
statsapp=tk.Tk()
statsapp.title("Statistics Application")
statsapp.geometry("500x450")
statsapp['bg']= '#fff2cc'
# buttons
zbtn=tk.Button(statsapp, text="Find Z Scores, sample mean (click here)", command=zscorefun, pady=10, padx=30, relief=RAISED, borderwidth=15)
findxbtn=tk.Button(statsapp, text="Find X Given Z, mu, sigma (click here)", command=findxvaluefromz, pady=10, padx=30, relief=RAISED, borderwidth=15)
simp_line_btn=tk.Button(statsapp, text="Simple Linear Regression (click here)", command=simple_linear, pady=10, padx=30, relief=RAISED, borderwidth=15)
multiple_2iv_btn=tk.Button(statsapp, text="Multiple Linear Regression 2 IV (click here)", command=multiple_regression2, pady=10, padx=30, relief=RAISED, borderwidth=15)
multiple_3iv_btn=tk.Button(statsapp, text="Multiple Linear Regression 3 IV (click here)", command=multiple_regression3, pady=10, padx=30, relief=RAISED, borderwidth=15)
multiple_4iv_btn=tk.Button(statsapp, text="Multiple Linear Regression 4 IV (click here)", command=multiple_regression4, pady=10, padx=30, relief=RAISED, borderwidth=15)
multiple_5iv_btn=tk.Button(statsapp, text="Multiple Linear Regression 5 IV (click here)", command=multiple_regression5, pady=10, padx=30, relief=RAISED, borderwidth=15)

# Labels for welcome label
welcome=tk.Label(statsapp, text="Welcome to the StatsApp: Select your calculation!", bg="#cfe2f3", pady=10, padx=30, relief=RAISED, borderwidth=15)

# place labels and buttons in main window
welcome.grid(row=0)
zbtn.grid(row=1)
findxbtn.grid(row=2)
simp_line_btn.grid(row=3)
multiple_2iv_btn.grid(row=4)
multiple_3iv_btn.grid(row=5)
multiple_4iv_btn.grid(row=6)
multiple_5iv_btn.grid(row=7)
# run program
statsapp.mainloop()
