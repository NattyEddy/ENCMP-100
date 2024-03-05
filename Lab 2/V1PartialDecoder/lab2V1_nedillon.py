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

print('Version 1')
# ----------Students write/modify their code below here ---------------------
day = 0

code = input('Please enter a code to break: ')
code = np.array(list(code),dtype=int)
print("The code entered is %s" % code)

## PROHIBIT IF NOT 9 DIGITS
if len(code) != 9:
    print("Decoy Message: Not a nine-digit number.")
## PROHIBIT IF EVEN
elif sum(code) % 2 == 0: # if divisible by two
    print("Decoy Message: Sum is even.")
else:
    day = code[2] * code[1] - code[0]
    if code[2]**code[1] % 3 == 0: # if divisible by three
        place = code[5] - code[4]
    else:
        place = code[4] - code[5]
    print("Day =", day)
    print("Place =", place)
    