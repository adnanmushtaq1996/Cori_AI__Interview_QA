# Word Analytics CORI AI

"""
Created on : Sun 13 14:03:01 2020
Author : Karol

"""

# Import Dependencies

import requests as reqs
import sys
import urllib
import re
import os

# Initialize Counters

word_counter = 0
letter_counter = 0
non_letter_counter = 0

# Load Data

# Read the URL Txt file 
url = 'http://textfiles.com/adventure/aencounter.txt'
file = urllib.request.urlopen(url)

# Write data to txt file
text_file = open("data.txt", "wt")

for line in file:
    decoded_line = line.decode("utf-8")
    n = text_file.write(decoded_line)
text_file.close()

# Load stored Data from TXT file 
with open ("data.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')
print(type(data))

# Implementation Logic

splcharlist = ['-', '+', '#', '@', '!', '(', ')', '?', '.', ',', ':', ';', '"', "'", '`'," ","*","[","]"]

for i in data:
    if i not in splcharlist and i.isdigit() == False:
        letter_counter = letter_counter + 1
    else :
        if i != " ":
            non_letter_counter = non_letter_counter + 1
        
print("ANSWER 1 : The total number of letters are : ",letter_counter)
print("ANSWER 2 : The total number of words are : ",len(data.split()))
print("ANSWER 3 : The total number of NON letters are : ",non_letter_counter)

word_counter = {}
for word in data.split():
    if word in word_counter:
        word_counter[word] += 1
    else:
        word_counter[word] = 1

popular_words = sorted(word_counter, key = word_counter.get, reverse = True)

top_3 = popular_words[:3]
print(top_3)  

from collections import Counter
words_to_count = (word for word in data.split() if word[:1].isupper())
c = Counter(words_to_count)
print(c.most_common(3))

print("ANSWER 4 : The Top three most common words are : ",top_3)

frequency_dict = {}
for character in data:
    if character not in splcharlist:
        if character in frequency_dict:
            frequency_dict[character] += 1
        else:
            frequency_dict[character] = 1
            
# Arrange in ascending order
frequency_dict = dict(sorted(frequency_dict.items(), key=lambda item: item[1]))
print(frequency_dict)        
most_occurring = max(frequency_dict, key=frequency_dict.get)

print("\nMost occuring character is: ", most_occurring)
print("It is repeated %d times" %(frequency_dict[most_occurring]))
print("\nANSWER 5 : The Top three most common letters are : ",list(frequency_dict.keys())[-3:])

temp = []
temp1 = []
temp2 = []
for i,j in word_counter.items():
    if j == 1:
        temp.append(i)

for i in temp:
    for j in i:
        if j in splcharlist:
            temp2.append(i)
        else :
            temp1.append(i)
                
temp = [x for x in temp1 if x not in temp2]
mylist = list(dict.fromkeys(temp))
print("ANSWER 7 : Words only used once : ",mylist)

temp =[]
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in alphabet: 
    if char not in data.lower(): 
        temp.append(char)

print("ANSWER 8 : All letters not used in the document : ",temp)

# Remove stored Data in Text File
os.remove("data.txt")

# Results Summary

print("Results of Question Word Analytics ")
print("\nANSWER 1 : The total number of letters are : ",letter_counter)
print("\nANSWER 2 : The total number of words are : ",len(data.split()))
print("\nANSWER 3 : The total number of NON letters are : ",non_letter_counter)
print("\nANSWER 4 : The Top three most common words are : ",top_3)
print("\nANSWER 5 : The Top three most common letters are : ",list(frequency_dict.keys())[-3:])
print("\nANSWER 7 : Words only used once : ",mylist)
print("\nANSWER 8 : All letters not used in the document : ",temp)
