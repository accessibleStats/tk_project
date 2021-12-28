
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
    welcome_label=tk.Label(slwindow, text="Welcome to the Simple Linear Relationship estimator: Input the values for X and Y (separate with spacebar)", pady=10, padx=30, relief=RAISED, borderwidth=15)
    x_varLabel=tk.Label(slwindow, text="Enter the values for X:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    y_varLabel=tk.Label(slwindow, text="Enter the values for Y:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    display_Label=tk.Label(slwindow, text="The estimated relationship is:", pady=10, padx=30, relief=RAISED, borderwidth=15, width=25)
    # Entry boxes for user input
    x_varnum=tk.Entry(slwindow, relief=RAISED, bd=5)
    y_varnum=tk.Entry(slwindow, relief=RAISED, bd=5)
    # Button to generate Z score
    simplebtn=tk.Button(slwindow, text="Calculate Linear Relationship", command=simple_linear)
    # Display box
    display=tk.Entry(slwindow)
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
    Zbtn=tk.Button(zwindow, text="Calculate Z", command=findzscore)
    # Display Box
    display=tk.Entry(zwindow)
    #Locations
    x_barLabel.grid(row=0, column=0)
    x_barnum.grid(row=0, column=1)
    mu_Label.grid(row=1, column=0)
    mu_num.grid(row=1, column=1)
    pop_standard_label.grid(row=2, column=0)
    pop_standard_num.grid(row=2, column=1)
    obs_Label.grid(row=3, column=0)
    obs_num.grid(row=3, column=1)
    Zbtn.grid(row=4, column=1)
    display_Label.grid(row=5, column=0)
    display.grid(row=5, column=1)
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
    ZscoreLabel=tk.Label(window, text="Enter the Z Score:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    mu_Label=tk.Label(window, text="Enter the mean of the population mean (mu):", pady=10, padx=30, relief=RAISED, borderwidth=15)
    pop_standard_label=tk.Label(window, text="Enter the population standard deviation (sigma):", pady=10, padx=30, relief=RAISED, borderwidth=15)
    display_Label=tk.Label(window, text="The value for X is:", pady=10, padx=30, relief=RAISED, borderwidth=15)
    # Entry boxes for user input
    Zscorenum=tk.Entry(window, relief=RAISED, bd=5)
    mu_num=tk.Entry(window, relief=RAISED, bd=5)
    pop_standard_num=tk.Entry(window, relief=RAISED, bd=5)
    # Button to find X
    Xbtn=tk.Button(window, text="Calculate X Value", command=findxvalue)
    # Display Box
    display=tk.Entry(window)
    #Locations
    ZscoreLabel.grid(row=0, column=0)
    Zscorenum.grid(row=0, column=1)
    mu_Label.grid(row=1, column=0)
    mu_num.grid(row=1, column=1)
    pop_standard_label.grid(row=2, column=0)
    pop_standard_num.grid(row=2, column=1)
    Xbtn.grid(row=3, column=1)
    display_Label.grid(row=4, column=0)
    display.grid(row=4, column=1)
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
# labels
welcome=tk.Label(statsapp, text="Welcome to the StatsApp: Select your calculation!", bg="#cfe2f3", pady=10, padx=30, relief=RAISED, borderwidth=15)
zlabel=tk.Label(statsapp, text="Find Z | x_bar, mu, sigma ->", bg="#90dbf4", pady=10, padx=30, relief=RAISED, borderwidth=15)
x_fromz_label=tk.Label(statsapp, text="Find X | z, mu, sigma ->", bg="#cfbaf0", pady=10, padx=30, relief=RAISED, borderwidth=15)
simp_line_label=tk.Label(statsapp, text="Simple Linear Regression -->", borderwidth=15, pady=10, padx=30, relief=RAISED)
# place labels and buttons in main window
welcome.grid(row=0, columnspan=2)
simp_line_label.grid(row=1, column=0)
simp_line_btn.grid(row=1, column=1)
zlabel.grid(row=2,column=0)
zbtn.grid(row=2,column=1)
x_fromz_label.grid(row=3,column=0)
findxbtn.grid(row=3,column=1)
# run program
statsapp.mainloop()
