# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Nathan Edillon 99%
# Student CCID: nedillon
# Others: Ali 1%
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
rescue_day = np.array(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"], dtype = str)
rendezvous = np.array(["bridge", "library", "river crossing", "airport", "bus terminal", "hospital", "railway station"], dtype = str)


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
    
    
    ## PRINT APPROPRIATE MESSAGES
    #
    
    if day < 1 or day > 7: # when not days 1-7
        
        print("Decoy Message: Invalid rescue day.") # third decoy message 
        
    elif place < 1 or place > 7: # when not places 1-7
        
        print("Decoy Message: Invalid rendezvous point.") # fourth decoy message 
                    
    else: 
        
        print("Rescued on %s at the %s" % (rescue_day[day - 1], rendezvous[place - 1])) # final decoded message