#!/usr/bin/env python3
# Simple Substitution Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import pyperclip, sys, random
import assignment1Quest as questions

LETTERS = 'abcdefghijklmnopqrstuvwxyz'

# etaoinshrdlcumwfgypbvkjxqz

# qihsneuayjzmdflxbotkvwrpg

def main():
    
    myMessage = questions.string4
    myKey = 'etvbqlxhncpjmayfguisrwzkod'
    myMode = 'decrypt'
    
    '''
    myMessage = input('Please enter your message: ')
    myKey = input('Please enter your key (all lower case letters): ')
    myMode = input('Are you encrypting or decrypting? (e/d)?: ')
    '''
    
    checkValidKey(myKey)

    myMode = myMode.lower()
    if myMode == 'encrypt' or myMode == 'e':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt' or myMode == 'd':
        translated = decryptMessage(myKey, myMessage)
    print('Using key %s' % (myKey))
    print('The %sed message is:' % (myMode))
    print(translated)
    pyperclip.copy(translated)
    print()
    print('This message has been copied to the clipboard.')


def checkValidKey(key):
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')


def encryptMessage(key, message):
    return translateMessage(key, message, 'encrypt')


def decryptMessage(key, message):
    return translateMessage(key, message, 'decrypt')


def translateMessage(key, message, mode):
    translated = ''
    charsA = LETTERS
    charsB = key
    if mode == 'decrypt':
    # For decrypting, we can use the same code as encrypting. We
    # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA
        
    # loop through each symbol in the message
    for symbol in message:
        if symbol.lower() in charsA:
            # encrypt/decrypt the symbol
            symIndex= charsA.find(symbol)
            translated += charsB[symIndex]
    
    return translated


def getRandomKey():
    key = list(LETTERS)
    random.shuffle(key)
    return ''.join(key)

if __name__ == '__main__':
    main()
    
    
    
    