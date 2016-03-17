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
	text: string
		The text to generate the n-gram model
    N: int
        The number of tuple for the n-gram model
        
    Returns
    -------
    dict
		dictionary containing the n-gram model
        
    """
    dictionary = {}
    splitText = text.split()
    for i in range(0, len(splitText) - N):
        fragment = tuple(splitText[i:i+N])
        next_word = splitText[i+N]
        if fragment not in dictionary:
            dictionary[fragment] = {}
        if next_word not in dictionary[fragment]:
            dictionary[fragment][next_word] = 1
        else:
            dictionary[fragment][next_word] += 1
    return dictionary
    

def getNextWord(model, fragment):
	"""
    Given a n-gram model. Find the next word based on how many that word has appeared.
    
    Parameters
    ----------
	model: dict
		The n-gram model
    fragment: tuple
        The word to generate the next word
        
    Returns
    -------
    str
		The string of the next word
        
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
    Given the a sample text. Will generate a text based on the markov chain.
    
    Parameters
    ----------
	text: str
		The sample text
		
    order: int
        The number of tuple which will influence the complexity of the generated text
    
	length:int
		The length of the cutoff for the sentence to generated.
		
    Returns
    -------
    str
		The string of the generated text.
    """
    model = generateNModel(text, order)
    splitText = text.split()
    randomInteger = random.randint(0, len(splitText) - order)
    currentFragment = tuple(splitText[randomInteger:randomInteger + order])
    
	#Starts with a title word.
    while not currentFragment[0].istitle():
        randomInteger = random.randint(0, len(splitText) - order)
        currentFragment = tuple(splitText[randomInteger:randomInteger + order])
        
    output = "" + " ".join(currentFragment)
    for i in range(0, length-order):
        newWord = getNextWord(model, currentFragment)
        #break if the model run out of words
        if newWord == "":
            break
        
        output += " " + newWord
        currentFragment = currentFragment[1:] + (newWord,)
		
        #Finish sentence when reach a period. Not a title is used to avoid ending in Mr.
        if newWord.endswith('.') and not newWord.istitle():
            break
    return output

if __name__ == '__main__':
	#Used for testing purpose 
    from nltk.corpus import gutenberg
    text = gutenberg.raw('austen-emma.txt')
    print(generateText(text,2,2000))