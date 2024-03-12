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

'''
DEBUG PROGRAM

CONTAINS CODE TO PARSE THROUGH ALL POSSIBLE PLOT ENTRIES

'''


## MENU PROMPT 
#  description: prompts user for options and returns the user selection
#  input: none
#  output: user-defined integer "choice"
#  action: prints options, asks for user input until an integer from
#          0-3 is selected, then stores input as "choice"
def menu():
    print()
    print("MAIN MENU")
    print("0. Exit program")
    print("1. Print database")
    print("2. Limit dimension")
    print("3. Plot one tour")
    print()
    choice = int(input("Choice (0-3)? ")) # choice 4 hidden
    while not (0 <= choice <= 4):
        choice = int(input("Choice (0-3)? "))
    return choice


## PLOT COORDS
#  description: defines the graph of a given dataset
#  input: list of coordinates "coord", list of titles "comment",
#         and list of names "name"
#  output: none
#  action: taking the x coords and y coords from "coords" and
#          noting the first and last coords, plot all the points
#          from the given data in blue and connecting the first
#          and the last points with a red line by plotting it
#          separately on top; label accordingly
def plotEuc2D(coord, comment, name):
    x_coords = []
    y_coords = []
    
    for i in range(0, len(coord)):
        x_coords += [coord[i][0]]
        y_coords += [coord[i][1]]
    
    start_finish_coords = [[x_coords[0], x_coords[-1]], [y_coords[0], y_coords[-1]]]
    
    plt.plot(x_coords, y_coords, ".-", label = name)
    plt.plot(start_finish_coords[0], start_finish_coords[1], ".r-")
    plt.xlabel("x-coordinate")
    plt.ylabel("y-coordinate")
    plt.title(comment)
    plt.legend()
    plt.savefig("tspPlot.png")
    plt.show()


## SELECTION 1: PRINT DATABASE
#  description: prints out the database of location data that 
#               can be used
#  input: database "tsp"
#  output: none
#  action: print out each set of data and their respective
#          metadata
def tspPrint(tsp):
    print()
    print("NUM  FILE NAME  EDGE TYPE  DIMENSION  COMMENT")
    for k in range(1,len(tsp)):
        name = tsp[k][0]
        edge = tsp[k][5]
        dimension = tsp[k][3]
        comment = tsp[k][2]
        print("%3d  %-9.9s  %-9.9s  %9d  %s"
              % (k,name,edge,dimension,comment))
        
        
## SELECTION 2: LIMIT DIMENSION
#  description: limits the database by the desired dimension
#               limit
#  input: database "tsp"
#  output: none
#  action: after calculating the min and max values of file
#          dimensions and asking for the user's desired limit,
#          evaluate whether the desired limit is valid considering
#          the min and max, then remove any 
def tspLimit(tsp):
    dimensions = []
    for i in range(1, len(tsp)):
        dimensions += [tsp[i][3]]        
    tsp_min = min(dimensions)
    tsp_max = max(dimensions)
    print("Minimum dimension: %d" % tsp_min)
    print("Maximum dimension: %d" % tsp_max)
    
    tsp_new = tsp
    limit = -1
    while True:
        if limit == 0: 
            print("Cancelling operation...")
            break;
        elif (limit >= tsp_min and limit <= tsp_max):
            print("Limiting dimension to %d..." % limit)
            tsp_new = [tsp[0]]
            for i in range(1, len(tsp)):
                if tsp[i][3] <= limit:
                    tsp_new += [tsp[i]]
            break;
        else:
            limit = int(input("Limit (enter 0 to cancel): "))
    return tsp_new
    

## SELECTION 3: PLOT ONE TOUR
#  description: takes one set from the database and plots 
#               their coordinates
#  input: database "tsp"
#  output: none
#  action: the number a user inputs selects the index 
#          associated with a file, evaluates the edge type
#          of the desired file, and plots it if it is of
#          type "EUC_2D" using function "plotEuc2D()"
def tspPlot(tsp):
    while True:
        num = int(input("Number (EUC_2D)? "))
        if num > len(tsp) - 1:
            pass
        else:
            edge = tsp[num][5]
            tsp1 = tsp[num]
            if edge == 'EUC_2D':
                print("See tspPlot.png")
                plotEuc2D(tsp1[10], tsp1[2], tsp1[0])
                break
            

## SELECTION 4: PLOT ALL TOURS
#  DEBUG ONLY FEATURE: TEST ALL CASES
#  FINDS WHICH EUC_2D CASES NEED CAREFUL ATTENTION
#  input: database "tsp"
#  output: none
#  action: parse through whole database, filter out edge file type
#          "EUC_2D", then attempt to plot all entries
def tspPlotAll(tsp):
    for i in range(1, len(tsp)):
        if tsp[i][5] == "EUC_2D":
            print("See tspPlot.png")
            plotEuc2D(tsp[i][10], tsp[i][2], tsp[i][0]) # refer to SELECTION 3


def main():
    tsp = io.loadmat('tspData.mat',squeeze_me=True)
    tsp = np.ndarray.tolist(tsp['tsp'])
    file = open('tspAbout.txt','r')
    print(file.read())
    file.close()
    choice = menu()
    while choice != 0:
        if choice == 1:
            tspPrint(tsp)
        elif choice == 2:
            tsp = tspLimit(tsp)
        elif choice == 3:
            tspPlot(tsp)
        elif choice == 4:
            tspPlotAll(tsp)
    
        choice = menu()
    
main()