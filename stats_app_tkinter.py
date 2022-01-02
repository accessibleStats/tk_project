"""
Statistics program with tkinter graphical user interface
Find univariate statistics, Z scores, X values for given Z scores, 
correlation r, simple regression equation estimation, multiple regression 
equation estimation, statistics using a binomial and Poisson distribution.

Jack Nickelson
"""

from tkinter import *
import tkinter as tk
import numpy as np
from numpy import sqrt
import statistics as statistics


######## Univariate Descriptie Statistics #########
 ## create a class with univariate descriptive stat attributes
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
###### function to generate secondary window from primary program window
def univarstats():
    # grab user input from entry window and assign to Univariate class
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
    # main window information
    main_win = tk.Toplevel()
    main_win.title("Univariate Descriptive Statistics")
    main_win.geometry("550x650")
    main_win['bg']= '#7b9cd1'
    # Welcome label
    welcome_label = tk.Label(main_win, text="Univariate Descriptive Statistics!", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',22))
    # execution button
    calc_button=tk.Button(main_win, text="Calculate Univariate Statistics (Click Here)", command=calculate_stats, font=('Helvetica',17))
    # entry box for user input.
    # create entry boxes
    x_values=StringVar()
    x_values = tk.Entry(main_win, width=45, font=('Helvetica',17))
    meanvalue= tk.Entry(main_win, width=45, font=('Helvetica',17))
    medianvalue= tk.Entry(main_win, width=45, font=('Helvetica',17))
    modevalue= tk.Entry(main_win, width=45, font=('Helvetica',17))
    variancevalue= tk.Entry(main_win, width=45, font=('Helvetica',17))
    standarddev= tk.Entry(main_win, width=45, font=('Helvetica',17))
    quartilevalues_in= tk.Entry(main_win, width=45, font=('Helvetica',17))
    iqr_in= tk.Entry(main_win, width=45, font=('Helvetica',17))
    outliers= tk.Entry(main_win, width=45, font=('Helvetica',17))
    # insert initial text into boxes. the text is cleared whenever the user presses the calculation button
    x_values.insert(0,"Enter Values; separate with , (example: 1, 2, 3 or 1,2,3)")
    meanvalue.insert(0,"The mean will appear here!")
    medianvalue.insert(0,"The median value will appear here!")
    modevalue.insert(0,"The mode will appear here!")
    variancevalue.insert(0,"The variance will appear here!")
    standarddev.insert(0,"The standard deviation will appear here!")
    quartilevalues_in.insert(0,"The inclusive quartiles will appear here!")
    iqr_in.insert(0,"The inclusive IQR will appear here!")
    outliers.insert(0,"Outlier information using IQR*1.5 will appear here!")
    # placement
    welcome_label.grid(row=0, pady=10, padx=50)
    x_values.grid(row=1, pady=10)
    calc_button.grid(row=2, pady=10)
    meanvalue.grid(row=3, pady=10)
    medianvalue.grid(row=4, pady=10)
    modevalue.grid(row=5, pady=10)
    variancevalue.grid(row=6, pady=10)
    standarddev.grid(row=7, pady=10)
    quartilevalues_in.grid(row=8, pady=10)
    iqr_in.grid(row=9, pady=10)
    outliers.grid(row=10, pady=10)
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
    slwindow.title("Two Variable Relationship")
    slwindow.geometry("600x500")
    slwindow['bg']= "#7b9cd1"
    # Labels for user input
    welcome_label=tk.Label(slwindow, text="Input X and Y (separate values with , )", pady=10, padx=30, relief=RAISED, borderwidth=10, bg='#fee3b5', font=('Helvetica',22))
    # Entry boxes for user input
    x_varnum=tk.Entry(slwindow, bd=5, width=30, font=('Helvetica',17))
    y_varnum=tk.Entry(slwindow, bd=5, width=30, font=('Helvetica',17))
    x_varnum.insert(0, "Enter X Values")
    y_varnum.insert(0,"Enter Y Values")
    # Button to generate Z score
    simplebtn=tk.Button(slwindow, text="Estimate Regression Equation (Click Here)", command=simple_linear, highlightbackground="gray", font=('Helvetica',17))
    # Display box
    display_reg_eq=tk.Entry(slwindow, highlightbackground="gray", width=40, font=('Helvetica',17))
    display_r=tk.Entry(slwindow, highlightbackground="gray", width=40, font=('Helvetica',17))
    display_r_sq=tk.Entry(slwindow, highlightbackground="gray", width=40, font=('Helvetica',17))
    display_reg_eq.insert(0,"The estimated regression equation will appear here!")
    display_r.insert(0,"The estimated correlation r will appear here!")
    display_r_sq.insert(0,"The estimated r-squared will appear here!")
    # Locations
    welcome_label.grid(row=0, pady=10, padx=50)
    x_varnum.grid(row=1, pady=10)
    y_varnum.grid(row=2, pady=10)
    simplebtn.grid(row=3, pady=10)
    display_reg_eq.grid(row=4, pady=10)
    display_r.grid(row=5, pady=10)
    display_r_sq.grid(row=6, pady=10)
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
    # main function calls x and y matrix functions, calculates the transpose of X matrix for linear algebra derrivation of 
    # predicted beta values
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
    mlwindow.geometry("600x400")
    mlwindow['bg']= "#7b9cd1"
    # Labels for user input
    welcome_label=tk.Label(mlwindow, text="Input values for X and Y (separate with , )", pady=10, padx=30, relief=RAISED, borderwidth=10, bg='#fee3b5', font=('Helvetica',22))
    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x_varnum.insert(0, "Enter X_1 values")
    x2_varnum.insert(0, "Enter X_2 values")
    y_varnum.insert(0, "Enter Y values")
    # Button to regression coefficients
    simplebtn=tk.Button(mlwindow, text="Estimate the regression equation (Click Here)", command=multiple_reg, borderwidth=5, font=('Helvetica',17))
    # Display box
    display=tk.Entry(mlwindow, relief=RAISED, bd=5, borderwidth=5, highlightbackground="#cfe2f3", width=50, font=('Helvetica',17))
    display.insert(0,"The estimated regression equation will appear here!")
    # Locations
    welcome_label.grid(row=0, pady=10, padx=50)
    x_varnum.grid(row=1, pady=10)
    x2_varnum.grid(row=2, pady=10) 
    y_varnum.grid(row=7, pady=10)
    simplebtn.grid(row=8, pady=10)
    display.grid(row=9, pady=10)
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
    mlwindow.geometry("800x600")
    mlwindow['bg']= "#7b9cd1"
    # Labels for user input
    welcome_label=tk.Label(mlwindow, text="Input values for X and Y (separate with , )", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',22))
    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    x3_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x3_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    # text inside of entry boxes
    x_varnum.insert(0,"Enter the values for X1")
    x2_varnum.insert(0,"Enter the values for X2")
    x3_varnum.insert(0,"Enter the values for X3")
    y_varnum.insert(0,"Enter the values for Y")
    # Button to estimate regression equation
    simplebtn=tk.Button(mlwindow, text="Estimate Regression Equation (Click Here)", command=multiple_reg, borderwidth=5, font=('Helvetica',17))
    # Display box
    display=tk.Entry(mlwindow, relief=RAISED, bd=5, borderwidth=5, highlightbackground="#cfe2f3", width=70, font=('Helvetica',17))
    display.insert(0,"The estimated regression equation will appear here!")
    # Locations
    welcome_label.grid(row=0, pady=10, padx=50)
    x_varnum.grid(row=1, pady=10)
    x2_varnum.grid(row=2, pady=10) 
    x3_varnum.grid(row=3, pady=10) 
    y_varnum.grid(row=7, pady=10)
    simplebtn.grid(row=8, pady=10)
    display.grid(row=9, pady=10, padx=50)
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
    mlwindow.geometry("800x600")
    mlwindow['bg']= "#7b9cd1"
    # Labels for welcome label
    welcome_label=tk.Label(mlwindow, text="Input values for X and Y (separate with , )", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc', font=('Helvetica',22))
    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    x3_varnum=StringVar()
    x4_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x3_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x4_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    # text inside of entry boxes
    x_varnum.insert(0,"Enter the values for X1")
    x2_varnum.insert(0,"Enter the values for X2")
    x3_varnum.insert(0,"Enter the values for X3")
    x4_varnum.insert(0,"Enter the values for X4")
    y_varnum.insert(0,"Enter the values for Y")
    # Button to estimate regression equation
    simplebtn=tk.Button(mlwindow, text="Estimate Regression Equation (Click Here)", command=multiple_reg, relief=RAISED, borderwidth=5, font=('Helvetica',17))
    # Display box
    display=tk.Entry(mlwindow, relief=RAISED, bd=5, borderwidth=10, highlightbackground="#cfe2f3", width=70, font=('Helvetica',17))
    display.insert(0,"The estimated regression equation will appear here!")
    # Locations
    welcome_label.grid(row=0, pady=10, padx=50)
    x_varnum.grid(row=1, pady=10)
    x2_varnum.grid(row=2, pady=10) 
    x3_varnum.grid(row=3, pady=10) 
    x4_varnum.grid(row=4, pady=10) 
    y_varnum.grid(row=7, pady=10)
    simplebtn.grid(row=8, pady=10)
    display.grid(row=9, pady=10, padx=50)
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
    mlwindow.geometry("800x600")
    mlwindow['bg']= "#7b9cd1"
    # Label for welcome
    welcome_label=tk.Label(mlwindow, text="Input the values for X and Y (separate with spacebar)", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',22))
    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    x3_varnum=StringVar()
    x4_varnum=StringVar()
    x5_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x3_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x4_varnum=tk.Entry(mlwindow, textvariable=x4_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    x5_varnum=tk.Entry(mlwindow, textvariable=x5_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=5, font=('Helvetica',17))
    # text inside of entry boxes
    x_varnum.insert(0,"Enter values for X1")
    x2_varnum.insert(0,"Enter values for X2")
    x3_varnum.insert(0,"Enter values for X3")
    x4_varnum.insert(0,"Enter values for X4")
    x5_varnum.insert(0,"Enter values for X5")
    y_varnum.insert(0,"Enter values for Y")
    # Button to regression coefficients
    simplebtn=tk.Button(mlwindow, text="Estimate Regression Equation (Click Here)", command=multiple_reg, borderwidth=5, highlightbackground="#cfe2f3", font=('Helvetica',17))
    # Display box
    display=tk.Entry(mlwindow, relief=RAISED, bd=5, borderwidth=10, width=70, font=('Helvetica',17))
    display.insert(0,"The estimated regression equation will appear here!")
    # Locations
    welcome_label.grid(row=0, pady=10, padx=50)
    x_varnum.grid(row=1, pady=10)
    x2_varnum.grid(row=2, pady=10) 
    x3_varnum.grid(row=3, pady=10)   
    x4_varnum.grid(row=4, pady=10)  
    x5_varnum.grid(row=5, pady=10)   
    y_varnum.grid(row=7, pady=10)
    simplebtn.grid(row=8, pady=10)
    display.grid(row=9, pady=10, padx=50)
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
        display.insert(0, "Z score = {}".format(z_score))
        x_barnum.delete(0,END)
        mu_num.delete(0,END)
        pop_standard_num.delete(0,END)
        obs_num.delete(0,END)
        x_barnum.insert(0,"Enter sample mean")
        mu_num.insert(0,"Enter population mean")
        pop_standard_num.insert(0,"Enter population sigma")
        obs_num.insert(0,"Enter # of observations")
    ### open window for Z score calculation
    zwindow=tk.Toplevel()
    zwindow.geometry("450x450")
    zwindow.title("Z Score")
    zwindow['bg']="#7b9cd1"    
    # Labels for welcome label
    welcomelabel=tk.Label(zwindow, text="Z Score (Sample Mean)", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',22))
    # Entry boxes for user input
    x_barnum=tk.Entry(zwindow, relief=RAISED, bd=5, font=('Helvetica',17))
    mu_num=tk.Entry(zwindow, relief=RAISED, font=('Helvetica',17))
    pop_standard_num=tk.Entry(zwindow, relief=RAISED, font=('Helvetica',17))
    obs_num=tk.Entry(zwindow, relief=RAISED, font=('Helvetica',17))
    x_barnum.insert(0,"Enter sample mean")
    mu_num.insert(0,"Enter population mean")
    pop_standard_num.insert(0,"Enter population sigma")
    obs_num.insert(0,"Enter # of observations")
    # Button to generate Z score
    Zbtn=tk.Button(zwindow, text="Calculate Z (Click Here)", command=findzscore, font=('Helvetica',17))
    # Display Box
    display=tk.Entry(zwindow, width=30, font=('Helvetica',17))
    display.insert(0,"The Z score will appear here!")
    #Locations
    welcomelabel.grid(row=0, pady=10, padx=50)
    x_barnum.grid(row=1, pady=10)
    mu_num.grid(row=2, pady=10)
    pop_standard_num.grid(row=3, pady=10)
    obs_num.grid(row=4, pady=10)
    Zbtn.grid(row=5, pady=10)
    display.grid(row=6, pady=10)
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
        Zscorenum.delete(0,END)
        mu_num.delete(0,END)
        pop_standard_num.delete(0,END)
        # reinsert the text for next calculation
        Zscorenum.insert(0,"Enter Z score")
        mu_num.insert(0,"Enter population mean")
        pop_standard_num.insert(0,"Enter population sigma")
    # open window for calculating X for a particular Z, pop mean, and pop standard deviation
    window=tk.Toplevel()
    window.title("Find X Given Z, mu, sigma")
    window.geometry("450x400")
    window['bg']="#7b9cd1"
    # Labels for welcome label
    welcomelabel=tk.Label(window, text="X value for given Z score", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',22))
    # Entry boxes for user input
    Zscorenum=tk.Entry(window, relief=RAISED, bd=5, font=('Helvetica',17))
    mu_num=tk.Entry(window, relief=RAISED, bd=5, font=('Helvetica',17))
    pop_standard_num=tk.Entry(window, relief=RAISED, bd=5, font=('Helvetica',17))
    Zscorenum.insert(0,"Enter Z score")
    mu_num.insert(0,"Enter population mean")
    pop_standard_num.insert(0,"Enter population sigma")
    # Button to find X
    Xbtn=tk.Button(window, text="Calculate X Value (Click Here)", command=findxvalue, font=('Helvetica',17))
    # Display Box
    display=tk.Entry(window, width=30, font=('Helvetica',17))
    display.insert(0,"The value for X will appear here!")
    #Locations
    welcomelabel.grid(row=0, pady=10, padx=50) 
    Zscorenum.grid(row=1, pady=10)
    mu_num.grid(row=2, pady=10)
    pop_standard_num.grid(row=3, pady=10)
    Xbtn.grid(row=4, pady=10)
    display.grid(row=5, pady=10)
##############################################

########## Binomial Statistics #################
def binomial_calc():
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
            results.delete(0, END) 
            results.insert(0, "In {} trials, the probability of at least {} win(s) is: {}".format(n, k, solution_at_least))
        elif calculation ==  'Exactly K successes':
            results.delete(0, END)
            results.insert(0, "In {} trials, the probability of exactly {} win(s) is: {}".format(n, k, solution_exact))
        elif calculation == 'At most K successes':
            results.delete(0, END)
            results.insert(0, "In {} trials, the probability of at most {} win(s) is: {}".format(n, k, solution_at_most))
        elif calculation == 'Less than K successes':
            results.delete(0, END)
            results.insert(0, "In {} trials, the probability of less than {} win(s) is: {}".format(n, k, solution_less_than))
        elif calculation == 'More than K successes':
            results.delete(0, END)
            results.insert(0, "In {} trials, the probability of more than {} win(s) is: {}".format(n, k, solution_more_than))
        else:
            return

    # window information
    bi_win = tk.Toplevel()
    bi_win.title("Binomial Statistics")
    bi_win.geometry("800x410")
    bi_win['bg']= '#7b9cd1'
    # Welcome label
    welcome_label = tk.Label(bi_win, text="Binomial Statistics", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',17))
    # execution button
    calc_button=tk.Button(bi_win, text="Calculate Binomial Statistics (Click Here)", command=run_program, font=('Helvetica',17), border=3)
    # entry box for user input
    trials=StringVar()
    prob_success=StringVar()
    num_success=StringVar()
    trials = tk.Entry(bi_win, width=5, font=('Helvetica',17), border=3)
    prob_success = tk.Entry(bi_win, width=5, font=('Helvetica',17), border=3)
    num_success = tk.Entry(bi_win, width=5, font=('Helvetica',17), border=3)
    results = tk.Entry(bi_win, width=65, font=('Helvetica',17), border=3)
    trials.insert(0, " ")
    prob_success.insert(0, " ")
    num_success.insert(0, " ")
    results.insert(0, "The results will appear here!")
    # labels
    trials_lab=tk.Label(bi_win, text='Events: N', font=('Helvetica',17), relief=RAISED, bg='#fee3b5')
    prob_success_lab=tk.Label(bi_win, text='Prob of Success: P', font=('Helvetica',17), relief=RAISED, bg='#fee3b5')
    num_success_lab=tk.Label(bi_win, text='Num of Successes: K', font=('Helvetica',17), relief=RAISED, bg='#fee3b5')
    # options drop down menu
    selection_1=StringVar()
    selection_1.set('At least K successes')
    option_sel = tk.OptionMenu(bi_win, selection_1, 'At least K successes', 'Exactly K successes', 'At most K successes', 'Less than K successes', 'More than K successes')
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


########## Poisson Statistics #################
#### modeling rare events ######
def poisson_calc():
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
    bi_win = tk.Toplevel()
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



# Main program tk window. Functions are launched from the main window.
# options for main window
statsapp=tk.Tk()
statsapp.title("Statistics Program")
statsapp.geometry("500x650")
statsapp['bg']= '#7b9cd1'

# buttons
zbtn=tk.Button(statsapp, text="Z Score (sample mean)", command=zscorefun, font=('Helvetica',17))
findxbtn=tk.Button(statsapp, text="X value for given Z score", command=findxvaluefromz, font=('Helvetica',17))
simp_line_btn=tk.Button(statsapp, text="Two Variable Statistics", command=simple_linear, font=('Helvetica',17))
multiple_2iv_btn=tk.Button(statsapp, text="Regression Equation Estimator (2 regressors)", command=multiple_regression2, font=('Helvetica',17))
multiple_3iv_btn=tk.Button(statsapp, text="Regression Equation Estimator (3 regressors)", command=multiple_regression3, font=('Helvetica',17))
multiple_4iv_btn=tk.Button(statsapp, text="Regression Equation Estimator (4 regressors)", command=multiple_regression4, font=('Helvetica',17))
multiple_5iv_btn=tk.Button(statsapp, text="Regression Equation Estimator (5 regressors)", command=multiple_regression5, font=('Helvetica',17))
univarbtn=tk.Button(statsapp, text="Univariate Statistics", command=univarstats, font=('Helvetica',17))
binomialbtn=tk.Button(statsapp, text="Binomial Statistics (n,p,k)", command=binomial_calc, font=('Helvetica',17))
poissonbtn=tk.Button(statsapp, text="Poisson Statistics (lambda, x, e)", command=poisson_calc, font=('Helvetica',17))
# Labels for welcome label
welcome=tk.Label(statsapp, text="Select your calculation!", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fee3b5', font=('Helvetica',22))

# place labels and buttons in main window
welcome.grid(row=0, pady=10, padx=50)
univarbtn.grid(row=1, pady=10, padx=30)
binomialbtn.grid(row=2, pady=10, padx=30)
zbtn.grid(row=3, pady=10, padx=30)
findxbtn.grid(row=4, pady=10, padx=30)
simp_line_btn.grid(row=5, pady=10, padx=30)
poissonbtn.grid(row=6, pady=10, padx=30)
multiple_2iv_btn.grid(row=7, pady=10, padx=30)
multiple_3iv_btn.grid(row=8, pady=10, padx=30)
multiple_4iv_btn.grid(row=9, pady=10, padx=30)
multiple_5iv_btn.grid(row=10, pady=10, padx=30)
# run program
statsapp.mainloop()


