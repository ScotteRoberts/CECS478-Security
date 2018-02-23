#!/usr/bin/env python
#-*-coding: utf-8-*-

import random, time, math, re, os
import assignment1Quest as questions

# Final results
result = {'key':'','plain':'','score':''}

# Make hash table for english quad grams
readFile = 'enQGRAM.txt'
fo = open(readFile)
qGramHash = {}
wordList = fo.read().split('\n')
for qGrams in wordList:
    parsed = qGrams.split(' ')
    parsed[1] = int(parsed[1])
    qGramHash[parsed[0]] = parsed[1]

# Generate random key
def init_key():
    
	key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	key = list(key)
	random.shuffle(key)

	return "".join(key)

# Generate new Key from previous key using character swapping
def change_key(key):

	new_key = list(key)
	i = random.randrange(0,25)
	j = random.randrange(0,25)
	temp = new_key[i]
	new_key[i] = new_key[j]
	new_key[j] = temp

	return "".join(new_key)

# Add dictionary values to current dictionary
def sortDict():
    fo = open('dictionary.txt')
    wordList = fo.read().split('\n')
    wordList = sorted(wordList)
    dictTxt = '\n'.join(wordList)
    fo.close()
    nf = open('dictionary.txt', 'w')
    nf.write(dictTxt)
    nf.close()
    
# Simple Substitution decrypt
# Hard coded to English (for now)
def decrypt(ciphertext, key="ABCDEFGHIJKLMNOPQRSTUVWXYZ"):

	alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	plain = ""

	for i in ciphertext:
		if i.isalpha():
			if i.isupper():
				charIndex = key.find(i)
				substituted = alpha[charIndex]
			else:
				charIndex = key.lower().find(i)
				substituted = alpha.lower()[charIndex]
			plain += substituted
		else:
			plain += i

	return plain

# Generates "fitness" to the english language based on quadgrams.
def score_text(text):
    
    # This is using REGEX to substitute any unwanted characters
    text = re.sub("[^A-Z]","",text.upper())
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = 0
    
    # Grabs each quadgram of the entire ciphertext.
    for i in range(0,len(text)-3):
        qGram = text[i:i+4] 
        if(qGram in qGramHash):
            score += qGramHash[qGram]

    return score


# The main method
def hill_climbing(cipher_text, count, sleep, startKey='SHERLOCKAYNFGIJZDPQTUMWBVX', random=False):
    #Create the random key
    if(random):
        parent_key = init_key()
    else:
        parent_key = startKey
    # Initialize a blank key to use in the future iterations.
    child_key = ""
    # The parent score is kept as the "best fitness"
    parent_score = score_text(decrypt(cipher_text, parent_key))

    # For all iterations of the child key, if the score passes the parent
    # score, then replace the parent.
    for i in range(0, count):
        child_key = change_key(parent_key)
        child_score = score_text(decrypt(cipher_text, child_key))

        if (child_score > parent_score):
            parent_score = child_score
            parent_key = child_key

        time.sleep(sleep)

    # Final results returned for checking validity of the cipher.
    result['key'] = parent_key
    result['plain'] = decrypt(cipher_text, parent_key)
    result['score'] = parent_score

    return result
