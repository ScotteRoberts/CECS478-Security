# -*- coding: utf-8 -*-
"""
@Author Scott Roberts
@Date: 02/06/18
"""

import enchant
import assignment1Quest as questions

dictionary = enchant.Dict("en_US")

#Assignment Strings

# use dictionary.check("") to see if a word exists

# to get a list from a delimeted string, use str.split("")
# the parameter of split is the delimeter

def ceasarShiftCharacter(char = "", shift = 0):
    shiftedValue = (ord(char) + shift)
    if(shiftedValue >= 123):
        shiftedValue = shiftedValue %123 + 97
    return chr(shiftedValue)

def ceasarShiftList(encString = ""):
    encString = encString.replace(" ", "")
    for s in range(26):
        shiftedString = []
        for i in list(encString):
            shiftedString.append(ceasarShiftCharacter(i, s))
        shiftedString = ''.join(shiftedString)
        print(shiftedString)
        print()