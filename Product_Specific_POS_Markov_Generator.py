"""
Created on Sun Mar  6 21:37:49 2016

@author: Carl
"""

import POS_Markov_Word
import pickle
import random
import nltk
import os.path

def createText(reviewDictionary, productNumber):
    outputText = ''
    ratings = ["1.0", "2.0", "3.0", "4.0", "5.0"]
    for rating in ratings:
        if rating in reviewDictionary[productNumber]:
            for review in reviewDictionary[productNumber][rating]:
                outputText += review
    return outputText

if __name__ == '__main__':
    #load the dictionary review file. If the file does not exist. 
    #Use the Parse Review py to generate one
    reviewDictionary = pickle.load( open( "reviewDictionary.p", "rb" ) )
    
    #"Pick Product Number" from this print statement
    print(reviewDictionary.keys())
    productNumber = "B00180OU66"
    
    #Create the sample review text data
    if os.path.exists("posTag.p"):
        text = pickle.load( open( "postag.p", "rb" ) )
    else:
        text = nltk.pos_tag(createText(reviewDictionary, productNumber).split())
        pickle.dump(text, open( "postag.p", "wb" ) )
        
    posList = [tag[1] for tag in text]
    
    posDict = {}
    for tag in text:
        if tag[1] in posDict:
            posDict[tag[1]].add(tag[0])
        else:
            posDict[tag[1]] = set(tag[0])
    
    #The higher the tuple number, the more organic the sentence will be 
    #but the more similar it will be to the original data. 
    order = 2
    
    #The number of words for each sentence. The generating text will automatically ends
    #when a sentence is finish so the number here only takes effect when the generating
    #text cannot find the ending sentence first.
    length = 100
    
    #The number of sentences wanted for the generated review.
    sentencesNumber = 3
    
    #Generate the review
    result = ""
    postString = POS_Markov_Word.generateText(posList, order, length)
    for tag in postString.split():
        result += " " + random.choice(list((posDict[tag])))
    print(result)