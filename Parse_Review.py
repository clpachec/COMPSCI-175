# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 15:06:58 2016

@author: Carl
"""
import pickle

file = open("movies.txt", 'r', encoding='latin-1')

textDictionary = {}

i = 0
productNumber = 0

for line in file:
    if productNumber >= 10000:
        break
    if (line[:18] == "product/productId:"):
        product = line[19:-1]
        productNumber += 1
    elif(line[:13] == "review/score:"):
        rating = line[14:-1]
    elif (line[:12] == "review/text:"):
        review = line[13:]
    elif (line == "\n"):
        if product not in textDictionary:
            textDictionary[product] = {}
        if rating not in textDictionary[product]:
            textDictionary[product][rating] = []
        textDictionary[product][rating].append(review)
    i += 1

file.close()
pickle.dump(textDictionary, open( "reviewDictionary.p", "wb" ) )