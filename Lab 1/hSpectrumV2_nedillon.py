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
#  to be used in model setup to find rydberg

electron_mass = 9.1093837e-31 # kg
proton_mass = 1.6726219e-27 # kg
fundamental_charge = 1.6021766e-19 # C
permitivitty = 8.8541878e-12 # m^-3 kg^-1 s^4 A^2
h = 6.6260702e-34 # m^2 kg s^-1 (Planck's constant)
c = 2.9979246e8 # m s^-1 (speed of light)


## EXPERIMENT DATA
#  given experimental data put in an array
data = [656.460,486.271,434.1692,410.2892,397.1198,389.0166,383.6485] # nm
nist = np.array(data)
n = len(nist)


## MODEL SETUP
#  this section defines and refines the rydberg constant, used to find the wavelength of each
#  n level transition in the bohr model; this program uses the final corrected version, 
#  "rydberg_corrected"
rydberg = (electron_mass * fundamental_charge**4) / (8 * permitivitty**2 * h**3 * c) # 1/m
h_scale_factor = proton_mass / (proton_mass + electron_mass) # kg / kg (unitless)
rydberg_corrected = h_scale_factor * rydberg # 1/m
print("Rydberg constant:", int(rydberg_corrected), "m" + chr(8315) + chr(185))


## SIMULATION DATA
#  allows user to input n final, then calculates an array of wavelengths associated with each
#  n initial to n final transition
nf = input("Final state (nf): ")
nf = int(nf)
ni = np.arange(nf+1,nf+n+1)

# for the second plot of data, each point is calculated using wavelength formula
bohr =  1e9 / (rydberg_corrected * (1 / nf**2 - 1 / ni**2))


## ERROR ANALYSIS
#  calculate the error between theoretical and experimental data, plot and state such error
error = data - bohr

# greatest difference graphed
# also note decimal formatting for numbers: "%.{i}f" % {num}
print("Worst-case error:", "%.3f" % np.max(np.abs(error)), "nm") 

# error analysis bar graph (difference)
plt.bar(ni, error, label = "NIST-Bohr", color = "indigo")
plt.xlabel("Initial State (ni)")
plt.ylabel("Wavelength (nm)")
plt.title("Hydrogen Emission Spectrum")
plt.legend()

plt.show()


## PLOTTING DATA
#  final plot between theoretical bohr model data and experimental NIST data

# third argument determines shape and colour of point
# need 'bx' for blue cross and 'r.' for red dot
# plotting format (x, y(x), 'marker type') plus optional label (used for legend)
plt.plot(ni, nist, 'bx', label = "NIST Data")
plt.plot(ni, bohr, 'r.', label = "Bohr Model")

plt.xlabel("Initial State (ni)")
plt.ylabel("Wavelength (nm)")
plt.title("Hydrogen Emission Spectrum")
plt.legend()

plt.grid(True)
plt.show()
