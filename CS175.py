import Generator1, Generator2
import nltk, re, pprint                     #Word Processesing
from nltk import word_tokenize              #Word Processing
from os import listdir                      #For Navigating through folders
from os.path import isfile, join            #For Navigating through folders
from string import punctuation

def tokenize_files(path, f_list):
    print("~~~ACCESSING PATH " + path + "~~~")
    text = ""
    for file in f_list:
        try:
            f = open(path + "\\" + file)
        except:
            print("Unable to open file: " + file)
        else:
            text += f.read()
            f.close()
    return word_tokenize(text)

if __name__ == '__main__':
    #Paths to review data set
    pos_path = "pos" #Path to positive reviews
    neg_path = "neg" #Path to negative reviews 
    
    print("---Retrieving Files---")
    
    #Text files being gathered from folder
    pos_files = [f for f in listdir(pos_path) if isfile(join(pos_path, f))]
    neg_files = [f for f in listdir(neg_path) if isfile(join(neg_path, f))]
    pos_text = (tokenize_files(pos_path, pos_files))
    neg_text = (tokenize_files(neg_path, neg_files))
    
    print()
    print("---POSITIVE REVIEW GENERATOR1---")
    print()
    
    print(Generator1.generate(pos_text))
    
    print()
    print("---NEGATIVE REVIEW GENERATOR1---")
    print()
    
    print(Generator1.generate(neg_text))
    
    print()
    print("---POSITIVE REVIEW GENERATOR2---")
    print()
    
    print(Generator2.generate(pos_text))
    
    print()
    print("---NEGATIVE REVIEW GENERATOR2---")
    print()
    
    print(Generator2.generate(neg_text))
    
    
    


    
    

    