"""
Created on Sun Mar  6 15:06:58 2016

@author: Carl
"""
import pickle

def createMovieReviewDictionary(numberOfProduct):
    """
    Create a dictionary file containing the reviews of each movies.
    The dictionary will have a format of dict{str:dict{str:list}}
    textDictionary will have keys that is the movies product serial
    textDictionary[product] will have keys for the rating
    textDictionary[product][rating] will give a list of review strings
    
    Parameters
    ----------
    numberOfProduct : int
        The number of movies to put into the dictionary. Note that this is not
        the number of reviews but the number of movies.
        
    Returns
    -------
    None
        
    """
    #Open the movie review data, can only be open in encoding latin-1
    file = open("movies.txt", 'r', encoding='latin-1')
    
    #Intialize Variables.
    textDictionary = {}
    currentProductNumber = 0
    
    #For loop to every line in file and add the movie review into the dictionary
    for line in file:
        #Take out the uneeded text in the file and store the text in the appropriate variables
        if (line[:18] == "product/productId:"):
            product = line[19:-1]
        elif(line[:13] == "review/score:"):
            rating = line[14:-1]
        elif (line[:12] == "review/text:"):
            review = line[13:]
        #Insert the review into the dictionary. Create the nessesary keys if not in the dictionary
        elif (line == "\n"):
            if product not in textDictionary:                
                textDictionary[product] = {}
                currentProductNumber += 1 #Keep track of how many movies are inserted
            if rating not in textDictionary[product]:
                textDictionary[product][rating] = []
            textDictionary[product][rating].append(review)
        #End the for loop when the desired number of movies has been reached
        if currentProductNumber >= numberOfProduct:
            break

    #Close file
    file.close()
    
    #Create the dictionary file
    pickle.dump(textDictionary, open( "reviewDictionary.p", "wb" ) )
    
if __name__ == '__main__':
    #The number of movies to put into the dictionary
    numberOfProduct = 1000
    
    #Create the dictionary file
    createMovieReviewDictionary(numberOfProduct)