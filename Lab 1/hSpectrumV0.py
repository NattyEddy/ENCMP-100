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
# Student name:
# Student CCID:
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
import numpy as np
import matplotlib.pyplot as plt

## EXPERIMENT DATA
#
data = [656.460,486.271,434.1692,410.2892] # nm
nist = np.array(data)
n = len(nist)

## MODEL SETUP
#
rydberg = 1.0973732e7 # 1/m
print("Rydberg constant:",rydberg)

## SIMULATION DATA
#
nf = input("Final state (nf): ")
nf = int(nf)
ni = np.arange(nf+1,nf+n+1)
plt.plot(ni,nist,'bx')
plt.grid(True)
plt.show()
