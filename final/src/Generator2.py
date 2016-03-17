'''
Created on Feb 19, 2016

@author: Arielle
'''


import random
import sys
from string import punctuation

"""
    Definition: Generate text based on Markov-Chaining technique
    
    Credit: https://code.activestate.com/recipes/194364-the-markov-chain-algorithm/
"""

nonword = "\n" # Since we split on whitespace, this can never be a word
punc_end = "!?."    #Sentence ending punctuations
contractions = ["'s","'d", "n't"]   #Contractions typically split as tokens

"""
    Returns word based on if it is a punctuation or not. If it is a punctuation, it does
    not add spacing. 

    Parameters
    ----------
    word : str
        A word which we want to extract features from.

    Returns
    -------
    str
        Processed string
        
"""


def process_word(word,prevWord):
    processed_word = word
    
    if(prevWord == nonword or prevWord in punc_end):
        processed_word = " " + processed_word.title()
    elif processed_word not in punctuation:
        if processed_word not in contractions:
            processed_word = " " + processed_word
    return processed_word

def generate(tokens):

    w1 = nonword
    w2 = nonword

    # GENERATE TABLE
    table = {}
    
    for word in tokens:
        table.setdefault( (w1, w2), [] ).append(word)
        w1, w2 = w2, word

    table.setdefault( (w1, w2), [] ).append(nonword) # Mark the end of the file
    # GENERATE OUTPUT
    w1 = nonword
    w2 = nonword
    
    generated_text = ""
    
    for i in range(300):
        newword = random.choice(table[(w1, w2)])
        if newword == nonword: sys.exit()
        generated_text += process_word(newword,w2) 
        w1, w2 = w2, newword

    return generated_text