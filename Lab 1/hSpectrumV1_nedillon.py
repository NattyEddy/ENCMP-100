## HSPECTRUM  Quantum Chemistry and the Hydrogen Emission Spectrum
#
# The periodic table is central to chemistry. According to Britannica,
# "Detailed understanding of the periodic system has developed along with
# the quantum theory of spectra and the electronic structure of atoms,
# beginning with the work of Bohr in 1913." In this lab assignment, a
# University of Alberta student explores the Bohr model's accuracy in
# predicting the hydrogen emission spectrum, using observed wavelengths
# from a US National Institute of Standards and Technology database.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Nathan Edillon
# Student CCID: nedillon
# Others: Liam 3%
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
import matplotlib.pyplot as plt


## CONSTANTS
# to be used in model setup to find rydberg

electron_mass = 9.1093837e-31 # kg
fundamental_charge = 1.6021766e-19 # C
permitivitty = 8.8541878e-12 # m^-3 kg^-1 s^4 A^2
h = 6.6260702e-34 # m^2 kg/s (Planck's constant)
c = 2.9979246e8 # m/s (speed of light)


## EXPERIMENT DATA
#
data = [656.460,486.271,434.1692,410.2892,397.1198,389.0166,383.6485] # nm
nist = np.array(data)
n = len(nist)


## MODEL SETUP
#
rydberg = (electron_mass * fundamental_charge**4) / (8 * permitivitty**2 * h**3 * c) # 1/m
print("Rydberg constant:", int(rydberg), "1/m")


## SIMULATION DATA
#
nf = input("Final state (nf): ")
nf = int(nf)
ni = np.arange(nf+1,nf+n+1)

# for the second plot of data, each point is calculated using wavelength formula
bohr =  1e9 / (rydberg * (1 / nf**2 - 1 / ni**2))


## PLOTTING DATA
# third argument determines shape and colour of point
# need 'bx' for blue cross and 'ro' for red spot
# plotting format (x, y(x), 'marker type') plus optional label
plt.plot(ni, nist, 'bx', label = "NIST Data")
plt.plot(ni, bohr, 'r.', label = "Bohr Model")

plt.xlabel("Initial State (ni)")
plt.ylabel("Wavelength (nm)")
plt.title("Hydrogen Emission Spectrum")
plt.legend()

plt.grid(True)
plt.show()
