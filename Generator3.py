"""
Created on Sun Mar  6 21:37:49 2016

@author: Carl
"""

import Markov_Word
import pickle
import random


def createText(reviewDictionary, star, numberOfReviews):
    """
    Returns a string representing the reviews of the desire star rating.

    Parameters
    ----------
    reviewDictionary : dict{str:dict{str:list}}
        The formated review dictionary. Has a form of reviewDictionary[product][star] 
        which will a list of reviews of that nature.
        
    star: str
        The star rating wanted
        Has to have a format of "1.0", "2.0", "3.0", "4.0" or "5.0"
        
    numberOfReviews: int
        The number of review wanted for the data. 
        Higher number means more reviews will be concatenated.
        
    Returns
    -------
    str
        A combine str of reviews
        
    Examples
    --------
    >>> createText({}, "1.0", 1)
    --------
    ""
    """
    outputText = ''
    
    for i in range(numberOfReviews):
        #Randomly choose a product
        product = random.choice(list(reviewDictionary.keys()))
        
        #Make sure product has that star rating available
        while star not in reviewDictionary[product]:
            product = random.choice(list(reviewDictionary.keys()))
        review = random.choice(reviewDictionary[product][star])
        
        #Remove review from list to make sure that review is not picked again
        reviewDictionary[product][star].remove(review) 
        
        #Delete that rating star key from product if empty
        if reviewDictionary[product][star] == []: 
            del reviewDictionary[product][star]
        outputText += review
        
    return outputText

if __name__ == '__main__':
    #load the dictionary review file. If the file does not exist. 
    #Use the Parse Review py to generate one
    reviewDictionary = pickle.load( open( "reviewDictionary.p", "rb" ) )
    
    #The desire rating for the generated review.
    #Has to have a format of "1.0", "2.0", "3.0", "4.0" or "5.0"
    star = "5.0"
    
    #The number of review data. The higher the number, the more reviews able to sample
    numberOfReviews = 1000
    
    #Create the sample review text data
    text = createText(reviewDictionary, star, numberOfReviews)
    
    #The higher the tuple number, the more organic the sentence will be 
    #but the more similar it will be to the original data. 
    #2 is a good inbetween number of the tuple
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