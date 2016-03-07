# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 08:46:23 2016

@author: Carl
"""
import random

def generateNModel(text, N):
    dictionary = {}
    splitText = text.split()
    for i in range(0, len(splitText) - N):
        fragment = tuple(splitText[i:i+N])
        next_letter = splitText[i+N]
        if fragment not in dictionary:
            dictionary[fragment] = {}
        if next_letter not in dictionary[fragment]:
            dictionary[fragment][next_letter] = 1
        else:
            dictionary[fragment][next_letter] += 1
    return dictionary
    

def getNextWord(model, fragment):
    words = []
    if fragment not in model:
        return ""
    for word in model[fragment].keys():
        for times in range(0, model[fragment][word]):
            words.append(word)
    return random.choice(words)

def generateText(text, order, length):
    model = generateNModel(text, order)
    splitText = text.split()
    randomInteger = random.randint(0, len(splitText) - order)
    currentFragment = tuple(splitText[randomInteger:randomInteger + order])
    
    while not currentFragment[0].istitle():
        randomInteger = random.randint(0, len(splitText) - order)
        currentFragment = tuple(splitText[randomInteger:randomInteger + order])
        
    output = "" + " ".join(currentFragment)
    for i in range(0, length-order):
        newWord = getNextWord(model, currentFragment)
        
        if newWord == "":
            break
        
        output += " " + newWord
        currentFragment = currentFragment[1:] + (newWord,)
        
        if newWord.endswith('.') and not newWord.istitle():
            break
    return output

if __name__ == '__main__':
    from nltk.corpus import gutenberg
    text = gutenberg.raw('austen-emma.txt')
    print(generateText(text,4,2000))