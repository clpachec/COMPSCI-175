'''
Created on Feb 19, 2016

@author: Arielle
'''


import random
import sys

"""
    Definition: Generate text based on Markov-Chaining technique
    
    Credit: https://code.activestate.com/recipes/194364-the-markov-chain-algorithm/
"""
def generate(tokens):
    nonword = "\n" # Since we split on whitespace, this can never be a word
    w1 = nonword
    w2 = nonword

    # GENERATE TABLE
    table = {}
    
    print("---Creating Tables---")
    
    for word in tokens:
        table.setdefault( (w1, w2), [] ).append(word)
        w1, w2 = w2, word

    table.setdefault( (w1, w2), [] ).append(nonword) # Mark the end of the file
    # GENERATE OUTPUT
    w1 = nonword
    w2 = nonword
    
    generated_text = ""
    
    print("---Beginning Text Generation---")
    
    for i in range(300):
        newword = random.choice(table[(w1, w2)])
        if newword == nonword: sys.exit()
        generated_text += newword + " "
        w1, w2 = w2, newword

    return generated_text