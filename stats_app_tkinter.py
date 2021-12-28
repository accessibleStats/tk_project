"""

Statistics Application with tkinter graphical user interface
Find Z scores, X values for given Z scores, simple, and multiple regression

Jack Nickelson
"""

from tkinter import *
import tkinter as tk
import numpy as np

####### Simple linear regression ##########
def simple_linear():
# Calculating simple linear regression
    def simple_linear():
        x_var = [float(x) for x in x_varnum.get().split(' ')]
        y_var = [float(y) for y in y_varnum.get().split(' ')]
        x_array = np.array([x_var])
        y_array = np.array([y_var])
        x_mean = x_array.mean()
        y_mean = y_array.mean()
        #x_std = x_array.std()
        #y_std = y_array.std()
        x_distfrommean = x_array - x_mean
        y_distfrommean = y_array - y_mean
        ssx = np.sum(np.power(x_distfrommean,2))
        ssy = np.sum(np.power(y_distfrommean,2))
        sumxyproducts = np.sum(x_distfrommean * y_distfrommean)    
        beta1 = sumxyproducts / ssx
        beta0 = y_mean - (beta1*x_mean)
        correlationcoefficient = sumxyproducts / np.sqrt(ssx*ssy)
        display.insert(0, "Y = {} + {}X".format(beta0, beta1))
    slwindow=tk.Toplevel()
    slwindow.title("Simple Linear Regression")
    slwindow.geometry("800x500")
    slwindow['bg']= "#cfe2f3"
    # Labels for user input
    welcome_label=tk.Label(slwindow, text="Welcome to the Simple Linear Relationship estimator: Input the values for X and Y (separate with spacebar)", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    x_varLabel=tk.Label(slwindow, text="Enter the values for X:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    y_varLabel=tk.Label(slwindow, text="Enter the values for Y:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    display_Label=tk.Label(slwindow, text="The estimated regression equation is:", pady=10, padx=30, relief=RAISED, borderwidth=15, width=25)
    # Entry boxes for user input
    x_varnum=tk.Entry(slwindow, relief=RAISED, bd=5)
    y_varnum=tk.Entry(slwindow, relief=RAISED, bd=5)
    # Button to generate Z score
    simplebtn=tk.Button(slwindow, text="Calculate Linear Relationship", command=simple_linear, highlightbackground="blue")
    # Display box
    display=tk.Entry(slwindow, highlightbackground="blue")
    # Locations
    welcome_label.grid(row=0, columnspan=2)
    x_varLabel.grid(row=1, column=0)
    x_varnum.grid(row=1, column=1)
    y_varLabel.grid(row=2, column=0)
    y_varnum.grid(row=2, column=1)
    simplebtn.grid(row=3, column=1)
    display_Label.grid(row=4, column=0)
    display.grid(row=4, column=1)
##########################################

######## Multiple Linear Regression (2 independent variables)
# Estimating regression model using numpy linear algebra
def multiple_regression2():
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
    mlwindow=tk.Toplevel()
    mlwindow.title("Multiple Linear Regression")
    mlwindow.geometry("800x800")
    mlwindow['bg']= "#cfe2f3"

    # Labels for user input
    welcome_label=tk.Label(mlwindow, text="Welcome to the Multiple Linear Relationship estimator: Input the values for X and Y (separate with spacebar)", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    x_varLabel=tk.Label(mlwindow, text="Enter the values for X1:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    x2_varLabel=tk.Label(mlwindow, text="Enter the values for X2:", pady=10, padx=30, relief=RAISED, borderwidth=15)    
    y_varLabel=tk.Label(mlwindow, text="Enter the values for Y:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    display_Label=tk.Label(mlwindow, text="The estimated regression equation is:", pady=10, padx=30, relief=RAISED, borderwidth=15, width=25)

    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()

    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=15)
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=15)
    y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=15)

    # Button to regression coefficients
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

######## Multiple Linear Regression (3 independent variables)
# Estimating regression model using numpy linear algebra
def multiple_regression3():
    def userinputx():
        x1 = [float(x) for x in x_varnum.get().split(' ')]
        x1 = np.array(x1)
        x1 = x1.astype(np.float64)
        x1 = x1[...,None]
        x2 = [float(x) for x in x2_varnum.get().split(' ')]
        x2 = np.array(x2)
        x2 = x2.astype(np.float64)
        x2 = x2[...,None]
        x3 = [float(x) for x in x3_varnum.get().split(' ')]
        x3 = np.array(x3)
        x3 = x3.astype(np.float64)
        x3 = x3[...,None]
        x_matrix = np.concatenate((x1, x2, x3), axis=1)
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
        beta_three=beta_hat[0,3]
        print(type(beta_hat))
        print(beta_zero)
        print(beta_one)
        print(beta_two)
        display.insert(0, "Y = {}+ {}X_1 + {}X_2 + {}X_3".format(beta_zero,beta_one,beta_two,beta_three))


    # main window information
    mlwindow=tk.Toplevel()
    mlwindow.title("Multiple Linear Regression")
    mlwindow.geometry("800x800")
    mlwindow['bg']= "#cfe2f3"

    # Labels for user input
    welcome_label=tk.Label(mlwindow, text="Welcome to the Multiple Linear Relationship estimator: Input the values for X and Y (separate with spacebar)", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    x_varLabel=tk.Label(mlwindow, text="Enter the values for X1:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    x2_varLabel=tk.Label(mlwindow, text="Enter the values for X2:", pady=10, padx=30, relief=RAISED, borderwidth=15)    
    x3_varLabel=tk.Label(mlwindow, text="Enter the values for X3:", pady=10, padx=30, relief=RAISED, borderwidth=15) 
    y_varLabel=tk.Label(mlwindow, text="Enter the values for Y:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    display_Label=tk.Label(mlwindow, text="The estimated regression equation is:", pady=10, padx=30, relief=RAISED, borderwidth=15, width=25)

    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    x3_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=15)
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=15)
    x3_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=15)
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
    x3_varLabel.grid(row=3, column=0)
    x3_varnum.grid(row=3, column=1) 
    y_varLabel.grid(row=7, column=0)
    y_varnum.grid(row=7, column=1)
    simplebtn.grid(row=8, column=1)
    display_Label.grid(row=8, column=0)
    display.grid(row=9, columnspan=2)
##########################################
##########################################

######## Multiple Linear Regression (4 independent variables)
# Estimating regression model using numpy linear algebra
def multiple_regression4():
    def userinputx():
        x1 = [float(x) for x in x_varnum.get().split(' ')]
        x1 = np.array(x1)
        x1 = x1.astype(np.float64)
        x1 = x1[...,None]
        x2 = [float(x) for x in x2_varnum.get().split(' ')]
        x2 = np.array(x2)
        x2 = x2.astype(np.float64)
        x2 = x2[...,None]
        x3 = [float(x) for x in x3_varnum.get().split(' ')]
        x3 = np.array(x3)
        x3 = x3.astype(np.float64)
        x3 = x3[...,None]
        x4 = [float(x) for x in x4_varnum.get().split(' ')]
        x4 = np.array(x4)
        x4 = x4.astype(np.float64)
        x4 = x4[...,None]
        x_matrix = np.concatenate((x1, x2, x3, x4), axis=1)
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
        beta_three=beta_hat[0,3]
        beta_four=beta_hat[0,4]
        print(type(beta_hat))
        print(beta_zero)
        print(beta_one)
        print(beta_two)
        display.insert(0, "Y = {}+ {}X_1 + {}X_2 + {}X_3 + {}X_4".format(beta_zero,beta_one,beta_two,beta_three,beta_four))

    # main window information
    mlwindow=tk.Toplevel()
    mlwindow.title("Multiple Linear Regression")
    mlwindow.geometry("800x800")
    mlwindow['bg']= "#cfe2f3"

    # Labels for user input
    welcome_label=tk.Label(mlwindow, text="Welcome to the Multiple Linear Relationship estimator: Input the values for X and Y (separate with spacebar)", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    x_varLabel=tk.Label(mlwindow, text="Enter the values for X1:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    x2_varLabel=tk.Label(mlwindow, text="Enter the values for X2:", pady=10, padx=30, relief=RAISED, borderwidth=15)    
    x3_varLabel=tk.Label(mlwindow, text="Enter the values for X3:", pady=10, padx=30, relief=RAISED, borderwidth=15) 
    x4_varLabel=tk.Label(mlwindow, text="Enter the values for X4:", pady=10, padx=30, relief=RAISED, borderwidth=15)  
    y_varLabel=tk.Label(mlwindow, text="Enter the values for Y:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    display_Label=tk.Label(mlwindow, text="The estimated regression equation is:", pady=10, padx=30, relief=RAISED, borderwidth=15, width=25)

    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    x3_varnum=StringVar()
    x4_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=15)
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=15)
    x3_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=15)
    x4_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=15)
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
    x3_varLabel.grid(row=3, column=0)
    x3_varnum.grid(row=3, column=1) 
    x4_varLabel.grid(row=4, column=0)
    x4_varnum.grid(row=4, column=1) 
    y_varLabel.grid(row=7, column=0)
    y_varnum.grid(row=7, column=1)
    simplebtn.grid(row=8, column=1)
    display_Label.grid(row=8, column=0)
    display.grid(row=9, columnspan=2)
##########################################
##########################################

######## Multiple Linear Regression (5 independent variables)
# Estimating regression model using numpy linear algebra
def multiple_regression5():
    def userinputx():
        x1 = [float(x) for x in x_varnum.get().split(' ')]
        x1 = np.array(x1)
        x1 = x1.astype(np.float64)
        x1 = x1[...,None]
        x2 = [float(x) for x in x2_varnum.get().split(' ')]
        x2 = np.array(x2)
        x2 = x2.astype(np.float64)
        x2 = x2[...,None]
        x3 = [float(x) for x in x3_varnum.get().split(' ')]
        x3 = np.array(x3)
        x3 = x3.astype(np.float64)
        x3 = x3[...,None]
        x4 = [float(x) for x in x4_varnum.get().split(' ')]
        x4 = np.array(x4)
        x4 = x4.astype(np.float64)
        x4 = x4[...,None]
        x5 = [float(x) for x in x5_varnum.get().split(' ')]
        x5 = np.array(x5)
        x5 = x5.astype(np.float64)
        x5 = x5[...,None]
        x_matrix = np.concatenate((x1, x2, x3, x4, x5), axis=1)
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
        beta_three=beta_hat[0,3]
        beta_four=beta_hat[0,4]
        beta_five=beta_hat[0,5]
        print(type(beta_hat))
        print(beta_zero)
        print(beta_one)
        print(beta_two)
        display.insert(0, "Y = {}+ {}X_1 + {}X_2 + {}X_3 + {}X_4 + {}X_5".format(beta_zero,beta_one,beta_two,beta_three,beta_four,beta_five))


    # main window information
    mlwindow=tk.Toplevel()
    mlwindow.title("Multiple Linear Regression")
    mlwindow.geometry("800x800")
    mlwindow['bg']= "#cfe2f3"

    # Labels for user input
    welcome_label=tk.Label(mlwindow, text="Welcome to the Multiple Linear Relationship estimator: Input the values for X and Y (separate with spacebar)", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    x_varLabel=tk.Label(mlwindow, text="Enter the values for X1:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    x2_varLabel=tk.Label(mlwindow, text="Enter the values for X2:", pady=10, padx=30, relief=RAISED, borderwidth=15) 
    x3_varLabel=tk.Label(mlwindow, text="Enter the values for X3:", pady=10, padx=30, relief=RAISED, borderwidth=15)  
    x4_varLabel=tk.Label(mlwindow, text="Enter the values for X4:", pady=10, padx=30, relief=RAISED, borderwidth=15)   
    x5_varLabel=tk.Label(mlwindow, text="Enter the values for X5:", pady=10, padx=30, relief=RAISED, borderwidth=15)  
    y_varLabel=tk.Label(mlwindow, text="Enter the values for Y:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    display_Label=tk.Label(mlwindow, text="The estimated regression equation is:", pady=10, padx=30, relief=RAISED, borderwidth=15, width=25)

    # Entry boxes for user input
    x_varnum=StringVar()
    x2_varnum=StringVar()
    x3_varnum=StringVar()
    x4_varnum=StringVar()
    x5_varnum=StringVar()
    y_varnum=StringVar()
    # Entry boxes for user input
    x_varnum=tk.Entry(mlwindow, textvariable=x_varnum, relief=RAISED, bd=5, borderwidth=15)
    x2_varnum=tk.Entry(mlwindow, textvariable=x2_varnum, relief=RAISED, bd=5, borderwidth=15)
    x3_varnum=tk.Entry(mlwindow, textvariable=x3_varnum, relief=RAISED, bd=5, borderwidth=15)
    x4_varnum=tk.Entry(mlwindow, textvariable=x4_varnum, relief=RAISED, bd=5, borderwidth=15)
    x5_varnum=tk.Entry(mlwindow, textvariable=x5_varnum, relief=RAISED, bd=5, borderwidth=15)
    y_varnum=tk.Entry(mlwindow, textvariable=y_varnum, relief=RAISED, bd=5, borderwidth=15)

    # Button to regression coefficients
    simplebtn=tk.Button(mlwindow, text="Calculate Linear Relationship", command=multiple_reg, relief=RAISED, borderwidth=15, highlightbackground="blue")
    # Display box
    display=tk.Entry(mlwindow, relief=RAISED, bd=5, borderwidth=10, highlightbackground="blue", width=70)
    # Locations
    welcome_label.grid(row=0, columnspan=2)
    x_varLabel.grid(row=1, column=0)
    x_varnum.grid(row=1, column=1)
    x2_varLabel.grid(row=2, column=0)
    x2_varnum.grid(row=2, column=1) 
    x3_varLabel.grid(row=3, column=0)
    x3_varnum.grid(row=3, column=1)   
    x4_varLabel.grid(row=4, column=0)
    x4_varnum.grid(row=4, column=1)  
    x5_varLabel.grid(row=5, column=0)
    x5_varnum.grid(row=5, column=1)   
    y_varLabel.grid(row=7, column=0)
    y_varnum.grid(row=7, column=1)
    simplebtn.grid(row=8, column=1)
    display_Label.grid(row=8, column=0)
    display.grid(row=9, columnspan=2)
###########################################

####### Z scores (solve for Z) ##########
def zscorefun():
    # Finding z score from sample mean, pop mean, pop standard deviation, and number of observations
    def findzscore():
        x_bar = float(x_barnum.get())
        mu = float(mu_num.get())
        standard = float(pop_standard_num.get())
        obs = float(obs_num.get())
        z_score = (x_bar - mu) / (standard/sqrt(obs))
        display.insert(0, z_score)
    ### open window for Z score calculation
    zwindow=tk.Toplevel()
    zwindow.geometry("800x500")
    zwindow['bg']="#cfe2f3"    
    # Labels for user input
    welcomelabel=tk.Label(zwindow, text="Welcome to the Z score finder!", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    x_barLabel=tk.Label(zwindow, text="Enter the sample mean (x-bar):", pady=10, padx=30, relief=RAISED, borderwidth=15)
    mu_Label=tk.Label(zwindow, text="Enter the mean of the population mean (mu):", pady=10, padx=30, relief=RAISED, borderwidth=15)
    pop_standard_label=tk.Label(zwindow, text="Enter the population standard deviation (sigma):", pady=10, padx=30, relief=RAISED, borderwidth=15)
    obs_Label=tk.Label(zwindow, text="Enter the number of observations (n):", pady=10, padx=30, relief=RAISED, borderwidth=15)
    display_Label=tk.Label(zwindow, text="The Z score is:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    # Entry boxes for user input
    x_barnum=tk.Entry(zwindow, relief=RAISED, bd=5)
    mu_num=tk.Entry(zwindow, relief=RAISED, bd=5)
    pop_standard_num=tk.Entry(zwindow, relief=RAISED, bd=5)
    obs_num=tk.Entry(zwindow, relief=RAISED, bd=5)
    # Button to generate Z score
    Zbtn=tk.Button(zwindow, text="Calculate Z", command=findzscore, highlightbackground="blue")
    # Display Box
    display=tk.Entry(zwindow, highlightbackground="blue")
    #Locations
    welcomelabel.grid(row=0,columnspan=2)
    x_barLabel.grid(row=1, column=0)
    x_barnum.grid(row=1, column=1)
    mu_Label.grid(row=2, column=0)
    mu_num.grid(row=2, column=1)
    pop_standard_label.grid(row=3, column=0)
    pop_standard_num.grid(row=3, column=1)
    obs_Label.grid(row=4, column=0)
    obs_num.grid(row=4, column=1)
    Zbtn.grid(row=5, column=1)
    display_Label.grid(row=6, column=0)
    display.grid(row=6, column=1)
##########################################

####### Z scores (solve for X) ##########
def findxvaluefromz():
    # Finding z score from sample mean, pop mean, pop standard deviation
    def findxvalue():
        z_score = float(Zscorenum.get())
        mu = float(mu_num.get())
        standard = float(pop_standard_num.get())
        x_value = (mu + standard*z_score)
        display.insert(0, x_value)
    # open window for calculating X for a particular Z, pop mean, and pop standard deviation
    window=tk.Toplevel()
    window.title("Find X Given Z, mu, sigma")
    window.geometry("800x500")
    window['bg']="#cfe2f3"
    # Labels for user input
    welcomelabel=tk.Label(window, text="Welcome to the X finder!", pady=10, padx=30, relief=RAISED, borderwidth=15, bg='#fff2cc')
    ZscoreLabel=tk.Label(window, text="Enter the Z Score:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    mu_Label=tk.Label(window, text="Enter the mean of the population mean (mu):", pady=10, padx=30, relief=RAISED, borderwidth=15)
    pop_standard_label=tk.Label(window, text="Enter the population standard deviation (sigma):", pady=10, padx=30, relief=RAISED, borderwidth=15)
    display_Label=tk.Label(window, text="The value for X is:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    # Entry boxes for user input
    Zscorenum=tk.Entry(window, relief=RAISED, bd=5)
    mu_num=tk.Entry(window, relief=RAISED, bd=5)
    pop_standard_num=tk.Entry(window, relief=RAISED, bd=5)
    # Button to find X
    Xbtn=tk.Button(window, text="Calculate X Value", command=findxvalue, highlightbackground="blue")
    # Display Box
    display=tk.Entry(window, highlightbackground="blue")
    #Locations
    welcomelabel.grid(row=0, columnspan=2) 
    ZscoreLabel.grid(row=1, column=0)
    Zscorenum.grid(row=1, column=1)
    mu_Label.grid(row=2, column=0)
    mu_num.grid(row=2, column=1)
    pop_standard_label.grid(row=3, column=0)
    pop_standard_num.grid(row=3, column=1)
    Xbtn.grid(row=4, column=1)
    display_Label.grid(row=5, column=0)
    display.grid(row=5, column=1)
##############################################

# Main program tk window. Functions are launched from the main window.
# options for main window
statsapp=tk.Tk()
statsapp.title("Statistics Application")
statsapp.geometry("700x900")
statsapp['bg']= '#fff2cc'
# buttons
zbtn=tk.Button(statsapp, text="Z Score (click here)", command=zscorefun, pady=10, padx=30, relief=RAISED, borderwidth=15)
findxbtn=tk.Button(statsapp, text="Find X Given Z (click here)", command=findxvaluefromz, pady=10, padx=30, relief=RAISED, borderwidth=15)
simp_line_btn=tk.Button(statsapp, text="Simple Linear Regression (click here)", command=simple_linear, pady=10, padx=30, relief=RAISED, borderwidth=15)
multiple_2iv_btn=tk.Button(statsapp, text="Multiple Linear Regression 2 IV (click here)", command=multiple_regression2, pady=10, padx=30, relief=RAISED, borderwidth=15)
multiple_3iv_btn=tk.Button(statsapp, text="Multiple Linear Regression 3 IV (click here)", command=multiple_regression3, pady=10, padx=30, relief=RAISED, borderwidth=15)
multiple_4iv_btn=tk.Button(statsapp, text="Multiple Linear Regression 4 IV (click here)", command=multiple_regression4, pady=10, padx=30, relief=RAISED, borderwidth=15)
multiple_5iv_btn=tk.Button(statsapp, text="Multiple Linear Regression 5 IV (click here)", command=multiple_regression5, pady=10, padx=30, relief=RAISED, borderwidth=15)

# labels
welcome=tk.Label(statsapp, text="Welcome to the StatsApp: Select your calculation!", bg="#cfe2f3", pady=10, padx=30, relief=RAISED, borderwidth=15)
zlabel=tk.Label(statsapp, text="Find Z | x_bar, mu, sigma ------>", bg="#bacbda", pady=10, padx=30, relief=RAISED, borderwidth=15)
x_fromz_label=tk.Label(statsapp, text="Find X | z, mu, sigma ---------->", bg="#90dbf4", pady=10, padx=30, relief=RAISED, borderwidth=15)
simp_line_label=tk.Label(statsapp, text="Simple Linear Regression ------>", bg='#cfbaf0', borderwidth=15, pady=10, padx=30, relief=RAISED)
multiple_2iv_label=tk.Label(statsapp, text="Multiple Linear Regression 2 IV -->", bg='#f4cccc', borderwidth=15, pady=10, padx=30, relief=RAISED)
multiple_3iv_label=tk.Label(statsapp, text="Multiple Linear Regression 3 IV -->", bg='#bacbda', borderwidth=15, pady=10, padx=30, relief=RAISED)
multiple_4iv_label=tk.Label(statsapp, text="Multiple Linear Regression 4 IV -->", bg='#90dbf4', borderwidth=15, pady=10, padx=30, relief=RAISED)
multiple_5iv_label=tk.Label(statsapp, text="Multiple Linear Regression 5 IV -->", bg='#cfbaf0', borderwidth=15, pady=10, padx=30, relief=RAISED)

# place labels and buttons in main window
welcome.grid(row=0, columnspan=2)
zlabel.grid(row=1,column=0)
zbtn.grid(row=1,column=1)
x_fromz_label.grid(row=2,column=0)
findxbtn.grid(row=2,column=1)
simp_line_label.grid(row=3, column=0)
simp_line_btn.grid(row=3, column=1)
multiple_2iv_label.grid(row=4,column=0)
multiple_2iv_btn.grid(row=4,column=1)
multiple_3iv_label.grid(row=5,column=0)
multiple_3iv_btn.grid(row=5,column=1)
multiple_4iv_label.grid(row=6,column=0)
multiple_4iv_btn.grid(row=6,column=1)
multiple_5iv_label.grid(row=7,column=0)
multiple_5iv_btn.grid(row=7,column=1)
# run program
statsapp.mainloop()
