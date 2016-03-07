# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 21:37:49 2016

@author: Carl
"""

import Markov_Word
import pickle
import random


def createText(reviewDictionary, star, numberOfReviews):
    outputText = ''
    for i in range(numberOfReviews):
        product = random.choice(list(reviewDictionary.keys()))
        while star not in reviewDictionary[product]:
            product = random.choice(list(reviewDictionary.keys()))
        outputText += random.choice(reviewDictionary[product][star])
    return outputText

if __name__ == '__main__':
    reviewDictionary = pickle.load( open( "reviewDictionary.p", "rb" ) )
    text = createText(reviewDictionary, '5.0', 10)
    print(Markov_Word.generateText(text, 2, 100))