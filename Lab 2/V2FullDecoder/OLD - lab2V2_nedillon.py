# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Nathan Edillon
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
# numbers, adding to 100%, follow-up questions may be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#
import numpy as np

print('Lab 2 - Version 2')
# ----------Students write/modify their code below here ---------------------

## VARIABLES / CONSTANTS
#

day = 0
place = 0
rescue_day = ""
rendezvous = ""


## USER INPUTS CODE
#

code = input('Please enter a code to break: ')
code = np.array(list(code),dtype=int)
print("The code entered is %s" % code)


## RULE 1: MUST BE A NINE-DIGIT NUMBER
#

if len(code) != 9: # execute if not a nine-digit number
    
    print("Decoy Message: Not a nine-digit number.")

## RULE 2: SUM OF NUMBER'S DIGITS MUST BE AN ODD NUMBER
#

elif sum(code) % 2 == 0: # if array of digits is divisible by two
    
    print("Decoy Message: Sum is even.")

else:
    
    ## RULE 3: DETERMINE THE DAY
    #  multiply the third digit by the second digit
    #  and subtract by the first
   
    day = code[2] * code[1] - code[0] # day decrypt
    
    
    ## RULE 4: DETERMINE THE RENDEZVOUS POINT
    #  raise the third digit by the second and
    #  determine if it is divisible by three; if so
    #  then subtract the fifth digit from the sixth,
    #  otherwise subtract the sixth digit from the
    #  fifth
    
    if code[2]**code[1] % 3 == 0: # place decrypt: if divisible by three
        place = code[5] - code[4]
    else:
        place = code[4] - code[5]
    
    if day >= 1 and day <= 7: # only run for days 1-7
        if day == 1:
            rescue_day = "Monday"
        elif day == 2:
            rescue_day = "Tuesday"
        elif day == 3:
            rescue_day = "Wednesday"
        elif day == 4:
            rescue_day = "Thursday"
        elif day == 5:
            rescue_day = "Friday"
        elif day == 6:
            rescue_day = "Saturday"
        elif day == 7:
            rescue_day = "Sunday"
        
        if place >= 1 and place <= 7: # only run for places 1-7
            if place == 1:
                rendezvous = "bridge"
            elif place == 2:
                rendezvous = "library"
            elif place == 3:
                rendezvous = "river crossing"
            elif place == 4:
                rendezvous = "airport"
            elif place == 5:
                rendezvous = "bus terminal"
            elif place == 6:
                rendezvous = "hospital"
            elif place == 7:
                rendezvous = "railway station"
            
            print("Rescued on %s at the %s" % (rescue_day, rendezvous)) # final decoded message
                
        else: # fourth decoy message when not places 1-7
            print("Decoy Message: Invalid rendezvous point.")
        
    else: # third decoy message when not days 1-7
        print("Decoy Message: Invalid rescue day.")