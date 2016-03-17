"""
Created on Sun Mar  6 21:37:49 2016

@author: Carl
"""

import Markov_Word
import pickle

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
    
    #The number of review data. The higher the number, the more reviews able to sample
    numberOfReviews = 1000
    
    #Create the sample review text data
    text = createText(reviewDictionary, productNumber)
    
    #The higher the tuple number, the more organic the sentence will be 
    #but the more similar it will be to the original data. 
    order = 2
    
    #The number of words for each sentence. The generating text will automatically ends
    #when a sentence is finish so the number here only takes effect when the generating
    #text cannot find the ending sentence first.
    length = 10000
    
    #The number of sentences wanted for the generated review.
    sentencesNumber = 3
    
    #Generate the review
    for i in range(sentencesNumber):
        print(Markov_Word.generateText(text, order, length))
        print()