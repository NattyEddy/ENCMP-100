## TSPANALYZE  Geomatics and the Travelling Sales[person] Problem
#
# According to the ISO/TC 211, geomatics is the "discipline concerned
# with the collection, distribution, storage, analysis, processing, [and]
# presentation of geographic data or geographic information." Geomatics
# is associated with the travelling salesman problem (TSP), a fundamental
# computing problem. In this lab assignment, a University of Alberta
# student completes a Python program to analyze, process, and present
# entries, stored in a binary data file, of the TSPLIB, a database
# collected and distributed by the University of Heidelberg.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Nathan Edillon 100%
# Student CCID: nedillon
# Others:
#
# To avoid plagiarism, list the names of persons, Version 0 author(s)
# excluded, whose code, words, ideas, or data you used. To avoid
# cheating, list the names of persons, excluding the ENCMP 100 lab
# instructor and TAs, who gave you compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the person's contributions in percent. Without these
# numbers, adding to 100%, follow-up questions will be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#
import scipy.io as io
import numpy as np
import matplotlib.pyplot as plt


## DATA / CONSTANTS
#  universal access for the whole program
tsp = io.loadmat('tspData.mat',squeeze_me=True)
tsp = np.ndarray.tolist(tsp['tsp'])

def menu():
    print()
    print("MAIN MENU")
    print("0. Exit program")
    print("1. Print database")
    print("2. Limit dimension")
    print("3. Plot one tour")
    print()
    choice = int(input("Choice (0-3)? "))
    while not (0 <= choice <= 3):
        choice = int(input("Choice (0-3)? "))
    return choice

def plotEuc2D(coord, comment, name):
    x_coords = []
    y_coords = []
    
    for i in range(0, len(coord)):
        x_coords += [coord[i][0]]
        y_coords += [coord[i][1]]
    
    plt.plot(x_coords, y_coords, label = name)
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.title(comment)
    plt.legend()
    plt.show()

def tspPrint():
    print()
    print("NUM  FILE NAME  EDGE TYPE  DIMENSION  COMMENT")
    for k in range(1,len(tsp)):
        name = tsp[k][0]
        edge = tsp[k][5]
        dimension = tsp[k][3]
        comment = tsp[k][2]
        print("%3d  %-9.9s  %-9.9s  %9d  %s"
              % (k,name,edge,dimension,comment))
        
def tspPlot():
    num = int(input("Number (EUC_2D)? "))
    edge = tsp[num][5]
    tsp1 = tsp[num]
    if edge == 'EUC_2D':
        print("See tspPlot.png")
        plotEuc2D(tsp1[10], tsp1[2], tsp1[0])
    else:
        print("Invalid (%s)!!!" % edge)

def main():
    
    file = open('tspAbout.txt','r')
    print(file.read())
    file.close()
    choice = menu()
    
    while choice != 0:
        if choice == 1:
            tspPrint()
        elif choice == 3:
            tspPlot()
    
        choice = menu()
    
    
main()