# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Nathan Edillon 93%
# Student CCID: nedillon
# Others: Norbert 5%, CAMP 2%
#
# To avoid plagiarism, list the names of persons, Version 0 author(s)
# excluded, whose code, words, ideas, or data you used. To avoid
# cheating, list the names of persons, excluding the ENCMP 100 lab
# instructor and TAs, who gave you compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the person's contributions in percent. Without these
# numbers, adding to 100%, follow-up questions may be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#
import matplotlib.pyplot as plt
import numpy as np

# print('Version 2')
# ------------Students edit/write their code below here--------------------------
# ---------------Remove any code that is unnecessary-----------------------------

## CONSTANTS / VARIABLES
#

savings = 2000.00 # $

ENGINEERING_TUITION = 6550.00 # $
ARTS_TUITION = 5550.00 # $
SCIENCE_TUITION = 6150.00 # $

MONTHLY_PAYMENT = 200.00 # $
ANNUAL_INTEREST_RATE = 0.0625 # %
COMPOUNDED_INTEREST = ANNUAL_INTEREST_RATE / 12 # %
ANNUAL_TUITION_INCREASE = 0.07 # %

annual_engg_cost = [ENGINEERING_TUITION] # $
annual_arts_cost = [ARTS_TUITION] # $
annual_science_cost = [SCIENCE_TUITION] # $

sum_arts_tuition = 0.00 # $
sum_engg_tuition = 0.00 # $
sum_science_tuition = 0.00 # $

MONTHS = np.arange(1, 216)
years = [0]
annual_savings = [savings]

total_tuition = [0, 1, 2] # [Arts, Science, Engineering]
program = ["Arts", "Science", "Engineering"]
minimum_monthly_payment = 1 # $ as an integer
state = ["insufficient", "enough"] # choose string based on true/false
tuition_cost_met = False

user_input = ""
choice = 0

## SAVINGS CALCULATION
#  using equation 1 from the instructions, evaluate savings for each month in 18 
#  years, adding each iteration into list annual_savings; years is used for 
#  scaling the graph; the final iteration is the total savings amount
for month in MONTHS:
    
    savings = (savings * (1 + COMPOUNDED_INTEREST)) + MONTHLY_PAYMENT
    annual_savings += [savings]
    years += [month / 12.0]
    
print("The savings amount is $%.2f" % savings)


## TUITION CALCULATION
#  using equation 2, evaluate the annual cost of each faculty for each year in 22 
#  years, adding each iteration into the list for each respective faculty
for year in np.arange(0, 21):
    
    annual_engg_cost += [annual_engg_cost[-1] * (1 + ANNUAL_TUITION_INCREASE)]
    annual_arts_cost += [annual_arts_cost[-1] * (1 + ANNUAL_TUITION_INCREASE)]
    annual_science_cost += [annual_science_cost[-1] * (1 + ANNUAL_TUITION_INCREASE)]
    
sum_arts_tuition = annual_arts_cost[-1] + annual_arts_cost[-2] + annual_arts_cost[-3] + annual_arts_cost[-4]
sum_science_tuition = annual_science_cost[-1] + annual_science_cost[-2] + annual_science_cost[-3] + annual_science_cost[-4]
sum_engg_tuition = annual_engg_cost[-1] + annual_engg_cost[-2] + annual_engg_cost[-3] + annual_engg_cost[-4]

print("The cost of the Arts program is $%.2f" % sum_arts_tuition)
print("The cost of the Sciences program is $%.2f" % sum_science_tuition)
print("The cost of the Engineering program is $%.2f" % sum_engg_tuition)

# Version 2 addition: put final tuition cost into the following list:
total_tuition[0] = sum_arts_tuition
total_tuition[1] = sum_science_tuition
total_tuition[2] = sum_engg_tuition


## PLOT
#  plot the balance and the total tuition for each faculty, scaled to years 0-18

plt.plot(years, annual_savings, label = "Saving Balance")
plt.axhline(y = sum_arts_tuition, color = "orange", label = "Arts")
plt.axhline(y = sum_science_tuition, color = "green", label = "Sciences")
plt.axhline(y = sum_engg_tuition, color = "red", label = "Engineering")

plt.xlabel("Years")
plt.ylabel("Amount $")
plt.title("Savings vs. Tuition")
plt.xticks(np.arange(19))
plt.xlim(0, 18)
plt.ylim(0, 100000)
plt.legend()
plt.show()


## USER FUNDS OPTIMIZATION
#  perform the calculation for mimimum funds required to contribute to savings
#  for adequate coverage

print("\n------------------------------------------------------------------------------------------\n")
print("For more details on a program, enter the number of the respective option below: ")
print("1. Arts")
print("2. Science")
print("3. Engineering")

# this while loop prompts the user until a valid option is chosen
# the reason I decided to use strings here is because it avoids throwing errors
# when the user enters a non-integer, without the need to throw an exception
while user_input != "1" and user_input != "2" and user_input != "3":
    user_input = input("Please enter a number from 1-3: ")

# the user's valid option is then cast into an integer    
choice = int(user_input)

# determine whether current savings equals or exceeds tuition
tuition_cost_met = annual_savings[-1] > total_tuition[choice - 1]

# to calculate the minimum monthly cost, use the same savings calculation for
# an initial monthly contribution of $1, and compare it to the desired program
# tuition cost over the 18 year period; increase the minimum payment by an
# increment of 1 until the total savings exceeds the tuition cost
while True:
    
    # reset these variables before each calculation
    savings = 2000.00 # $
    years = [0]
    annual_savings = [savings]
    
    # from section SAVINGS CALCULATION
    for month in MONTHS:
        savings = (savings * (1 + COMPOUNDED_INTEREST)) + minimum_monthly_payment
        annual_savings += [savings]
        years += [month / 12.0]
    
    # compare savings to tuition, stop if savings covers cost
    if annual_savings[-1] > total_tuition[choice - 1]: break
    else: minimum_monthly_payment += 1

# print the message indicating in/sufficient funds and print minimum monthly cost
print("You currently have %s funds for the %s Program." % (state[tuition_cost_met], program[choice - 1]))
print("The minimum monthly contribution required is $%i a month." % minimum_monthly_payment)