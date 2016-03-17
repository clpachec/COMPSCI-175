# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 08:46:23 2016

@author: Carl
"""
import random

def generateNModel(text, N):
	"""
    Create n-gram model of the text given.
    
    Parameters
    ----------
	text: list
		The list of POS in order to generate the n-gram model
    N: int
        The number of tuple for the n-gram model
        
    Returns
    -------
    dict
		dictionary containing the n-gram model
        
    """
    dictionary = {}
    for i in range(0, len(text) - N):
        fragment = tuple(text[i:i+N])
        next_letter = text[i+N]
        if fragment not in dictionary:
            dictionary[fragment] = {}
        if next_letter not in dictionary[fragment]:
            dictionary[fragment][next_letter] = 1
        else:
            dictionary[fragment][next_letter] += 1
    return dictionary
    

def getNextWord(model, fragment):
	"""
    Given a n-gram model. Find the next POS based on how many that POS has appeared.
    
    Parameters
    ----------
	model: dict
		The n-gram model
    fragment: tuple
        The POS to generate the next word
        
    Returns
    -------
    str
		The string of the next POS
        
    """
    words = []
    if fragment not in model:
        return ""
    for word in model[fragment].keys():
        for times in range(0, model[fragment][word]):
            words.append(word)
    return random.choice(words)

def generateText(text, order, length):
	"""
    Given the list of POS in order. Will generate a POS based on the markov chain.
    
    Parameters
    ----------
	text: str
		The POS to sample
		
    order: int
        The number of tuple which will influence the complexity of the generated text
    
	length:int
		The length of the cutoff for the sentence to generated.
		
    Returns
    -------
    str
		The string of the generated POS.
    """
    model = generateNModel(text, order)
    randomInteger = random.randint(0, len(text) - order)
    currentFragment = tuple(text[randomInteger:randomInteger + order])
    
    while currentFragment[0] == ".":
        randomInteger = random.randint(0, len(text) - order)
        currentFragment = tuple(text[randomInteger:randomInteger + order])
        
    output = "" + " ".join(currentFragment)
    for i in range(0, length-order):
        newWord = getNextWord(model, currentFragment)
        
        if newWord == "":
            break
        
        output += " " + newWord
        currentFragment = currentFragment[1:] + (newWord,)
        
    return output