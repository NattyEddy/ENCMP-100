## PERIHELION  Mercury's perihelion precession and general relativity
#
# In this lab assignment, a student completes a Python program to test with
# data an accurate prediction of Einstein’s theory, namely the perihelion
# precession of Mercury. Mercury’s orbit around the Sun is not a stationary
# ellipse, as Newton’s theory predicts when there are no other bodies. With
# Einstein’s theory, the relative angle of Mercury’s perihelion (position
# nearest the Sun) varies by about 575.31 arcseconds per century.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Nathan Edillon 95%
# Student CCID: nedillon
# Others: GOLDEN 5%
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
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def main():
    data = loaddata('horizons_results')
    data = locate(data) # Perihelia
    data = select(data,25,('Jan','Feb','Mar'))
    makeplot(data,'horizons_results')
    savedata(data, 'horizons_results')

## extracts data from a file
#  @param filename - name of the file
#  @return all necessary data from the file (a list)
#  prints progress as data loads in increments of 10 000
def loaddata(filename):
    file = open(filename+'.txt','r')
    lines = file.readlines()
    file.close()
    noSOE = True
    num = 0
    data = []
    for line in lines:
        if noSOE:
            if line.rstrip() == "$$SOE":
                noSOE = False
        elif line.rstrip() != "$$EOE":
            num = num+1
            if num % 10000 == 0:
                print(filename,":",num,"line(s)")
            datum = str2dict(line)
            data.append(datum)
        else:
            break # for
    if noSOE:
        print(filename,": no $$SOE line")
    else:
        print(filename,":",num,"line(s)")
    return data

## converts a string of data (each line in a file) into a dictionary
#  @param data - pulled from a line in a file
#  @return a dictionary with values "numdate" (float), "strdate" (string), and
#          "coord" (tuple of three floats))
#  divides data from @param data to extract comma-separated-values from a
#  string
def str2dict(data):
    metadata = data.split(",")
    caldate = metadata[1].split()
    
    numdate = float(metadata[0])
    strdate = caldate[1]
    x = float(metadata[2])
    y = float(metadata[3])
    z = float(metadata[4])
    
    return {'numdate':numdate,'strdate':strdate,
            'coord':(x, y, z)}

## calculates magnitude of each coordinate and returns small coordinates in
#  between greater ones
#  @param data1 - data pulled from a file
#  @return list of selected data from data1
def locate(data1):
    dist = [] # Vector lengths
    for datum in data1:
        coord = np.array(datum['coord'])
        dot = np.dot(coord,coord)
        dist.append(np.sqrt(dot))
    data2 = []
    for k in range(1,len(dist)-1):
        if dist[k] < dist[k-1] and dist[k] < dist[k+1]:
            data2.append(data1[k])
    return data2

## picks data to graph based on a set interval and a select set of months
#  @param data - data pulled from file
#  @param ystep - an integer for year interval
#  @param month - a set of strings with desired months
def select(data,ystep,month):
    accepted_data = []
    for line in data:
        string = line.get("strdate")
        meta = string.split("-")
        if meta[1] in month and int(meta[0]) % ystep == 0:
            accepted_data.append(line)   
    return accepted_data

def makeplot(data,filename):
    (numdate,strdate,arcsec) = precess(data)
    plt.plot(numdate,arcsec,'bo')
    plt.xticks(numdate,strdate,rotation=45)
    plt.xlabel("Perihelion date")
    plt.ylabel("Precession (arcsec)")
    add2plot(numdate,arcsec)
    plt.savefig(filename+'.png',bbox_inches='tight')
    plt.show()

def precess(data):
    numdate = []
    strdate = []
    arcsec = []
    v = np.array(data[0]['coord']) # Reference (3D)
    for datum in data:
        u = np.array(datum['coord']) # Perihelion (3D)
        ratio = np.dot(u,v)/np.sqrt(np.dot(u,u)*np.dot(v,v))
        if np.abs(ratio) <= 1:
            angle = 3600*np.degrees(np.arccos(ratio))
            numdate.append(datum['numdate'])
            strdate.append(datum['strdate'])
            arcsec.append(angle)
    return (numdate,strdate,arcsec)

def add2plot(numdate,actual):
    r = stats.linregress(numdate,actual)
    bestfit = []
    for k in range(len(numdate)):
        bestfit.append(r[0]*numdate[k]+r[1])
    plt.plot(numdate,bestfit,'b-')
    plt.legend(["Actual data","Best fit line"])
    
## save specified data into a csv file
#  @param data - desired data
#  @param filename - desired name of new file to create
#  extracts numdate, strdate, xcoord, ycoord, and zcoord from data and stores
#  in a .csv file
def savedata(data, filename):
    file = open(filename+'.csv', 'w')
    file.write("NUMDATE,STRDATE,XCOORD,YCOORD,ZCOORD\n")
    for line in data:
        file.write("%f,%s,%f,%f,%f\n" % (line.get('numdate'), 
                                         line.get('strdate'),
                                         line.get('coord')[0],
                                         line.get('coord')[1], 
                                         line.get('coord')[2]))

main()
