# -*- coding: utf-8 -*-
"""
@Author Scott Roberts
@Date: 02/06/18
"""

import enchant
import assignment1Quest as questions

#Assignment Strings

# Shift each ASCII character by a given "Shift" amount.
def ceasarShiftCharacter(char = "", shift = 0):
    shiftedValue = (ord(char) + shift)
    if(shiftedValue >= 123):
        shiftedValue = shiftedValue %123 + 97
    return chr(shiftedValue)

# Apply ceasarShiftCharacter on a string for 26 iterations
def ceasarShiftList(encString = ""):
    encString = encString.replace(" ", "")
    for s in range(26):
        shiftedString = []
        for i in list(encString):
            shiftedString.append(ceasarShiftCharacter(i, s))
        shiftedString = ''.join(shiftedString)
        print(shiftedString)
        print()