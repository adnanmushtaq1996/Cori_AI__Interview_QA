# Word Analytics CORI AI
# url = 'https://vmsensorlog.westeurope.cloudapp.azure.com:1880/huckleberry-finn'

"""
Created on : Sun 13 14:03:01 2020
Author : Karol

"""

# Import Dependencies
import requests as reqs
import sys
import urllib
import os
import argparse


def multiple_counter():
    # Initialize Counters
    word_counter = 0
    letter_counter = 0
    non_letter_counter = 0
    for i in data:
        if i not in splcharlist and i.isdigit() == False:
            letter_counter = letter_counter + 1
        else :
            if i != " ":
                non_letter_counter = non_letter_counter + 1

    if letter_counter != 0:
        print('"%d words", where %d is the number of words in the given document' %(letter_counter, letter_counter)) 
    if len(data.split()) != 0:
        print('"%d letters", where %d is the number of letters in the given document' %(len(data.split()), len(data.split())))   
    if non_letter_counter != 0:
        print('"%d symbols", where %d is the number of non-letter and non-digit character, excluding white spaces, in the document' %(non_letter_counter, non_letter_counter))


def common_occurence():
    global word_counter

    # Method 1
    word_counter = {}
    for word in data.split():
        if word in word_counter:
            word_counter[word] += 1
        else:
            word_counter[word] = 1

    popular_words = sorted(word_counter, key = word_counter.get, reverse = True)

    top_3 = popular_words[:3]
    print(top_3)  

    # Method 2
    from collections import Counter
    words_to_count = (word for word in data.split() if word[:1].isupper())
    c = Counter(words_to_count)
    print(c.most_common(3))

    if len(top_3) != 0:
        print('"Top three most common words: %s, %s, %s", where %s, %s, and %s are the top three most common words' %(*top_3, *top_3))

    frequency_dict = {}
    for character in data:
        if character not in splcharlist:
            if character in frequency_dict:
                frequency_dict[character] += 1
            else:
                frequency_dict[character] = 1
                
    # Arrange in ascending order
    frequency_dict = dict(sorted(frequency_dict.items(), key=lambda item: item[1]))
    #print(frequency_dict)        
    most_occurring = max(frequency_dict, key=frequency_dict.get)

    #print("\nMost occuring character is: ", most_occurring)
    #print("It is repeated %d times" %(frequency_dict[most_occurring]))
 
    print('"Top three most common letters: %c, %c, %c", where %c, %c, and %c are the top three most common letters' %(*list(frequency_dict.keys())[-3:], *list(frequency_dict.keys())[-3:]))


def single_usage():
    
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

    if len(mylist) != 0 :
        print('Words only used once: ', mylist)


def non_used_letters():
    temp =[]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet: 
        if char not in data.lower(): 
            temp.append(char)

    if len(temp) != 0 :
        print("Letters not used in the document: ", temp)


def main() :
    # Load Data
    # Read the URL Txt file 
    global data, splcharlist
    
    try :
        file = urllib.request.urlopen(url)
    except :
        print("HTML endpoint entered is not Valid or not opening !!")
        sys.exit(1)

    # Write data to txt file
    text_file = open("data.txt", "wt",encoding='utf-8')

    for line in file:
        decoded_line = line.decode("utf-8")
        n = text_file.write(decoded_line)
    text_file.close()

    # Load stored Data from TXT file 
    with open ("data.txt", "r") as myfile:
        data=myfile.read().replace('\n', '')

    # Implementation Logic
    splcharlist = ['-', '+', '#', '@', '!', '(', ')', '?', '.', ',', ':', ';', '"', "'", '`'," ","*","[","]"]

    multiple_counter()
    common_occurence()
    single_usage()
    non_used_letters()

    # Remove stored Data in Text File
    os.remove("data.txt")

def argsparser():
    global url
    parser = argparse.ArgumentParser(description='Word Analytics.')
    parser.add_argument('--end_point', '--ep', help='Provide HTTPS endpoint', required = True)

    args = parser.parse_args()
    url = args.end_point


if __name__ == "__main__":
    argsparser()
    main()