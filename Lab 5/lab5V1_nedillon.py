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

main()
