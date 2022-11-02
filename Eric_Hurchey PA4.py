#Eric Hurchey
#Programming Assignment 4
#03/29/2022

import random
FILE='''I am typing a bit of nonsense in order to test my text justification program. The goal is to split a file into paragraphs using a unique separator, and then for each paragraph, split it into lines and add spaces so the each line prints the same length.

We are ignoring punctuation and carriage returns. The only caveat is that if the last line only has one word in it, it should be left justified.

The goal of the program is to be a primitive simulation of one of the functions of a word processor, the most ubiquitous of software applications which used to have a vibrant ecosystem of variants, but which has collapsed into a monopoly governed by Microsoft word. Other parts of word processing require paging files into buffers, spell checking, display management and keyboard processing.'''

def printpara(words,length): #call a function to print out the paragraphs in order
    line = []
    spaces = []
    while len(words) != 0:
        line.append(getline(words,length))
    for i in range(len(line)):
        for x in range(len(line[i])):
            spaces=[[1]*len(line[x]) for x in range(len(line))]
    for q in range(len(spaces)):
        spaces[q][len(spaces[q]) - 1]=0
    spaces = addspaces(line,spaces,length)
    printline(line,spaces)

def printline(line,spaces): #call a function to print out the desired line length with no spaces
    for i in range(len(line)): #the length of each line will print out the needed spaces
        print(" ") 
        for x in range(len(line[i])): #here, each line will make sure that the lines are even
            print(line[i][x] + (" " * spaces[i][x]), end='')

def addspaces(line, spaces, length): #call a function to print out the amount of spaces that will be printed within each line
    total_line = 0
    for i in range(len(line)):
        total_line = 0
        for e in range(len(line[i])):
            total_line += 1 + len(line[i][e])
        total_line -= 1
        while length > total_line:
            if i != len(line) - 1:
                m = random.randint(0, len(spaces[i]) - 2)
                spaces[i][m] += 1
                total_line += 1
            elif i == len(line) - 1:
                spaces[i][len(spaces[i]) - 1] = length - total_line
                length = total_line
    return spaces

def getline(words,length): #a given call function
    ans = []
    total = 0
    while (length>total) and 0 != len(words):
        word = words.pop(0)
        total += len(word) + 1 #add 1 for the space
        ans.append(word)
 #now we are one word too long
    if total > length:
        words.insert(0,ans.pop())
    return ans

def main(FILE,length): #calling a main function
    test = FILE.split('\n\n')
    for i in test:
        printpara(i.split(), length)
        print() #this is very important that this is within the for loop because if it's not, then there will not be any spaces between the paragraphs

main(FILE, 40) #calling back a wanted length
print() #just wanting to clearly seperate one file length from another, this is not needed, but just for clarity sake and to visual see the difference
main(FILE, 60) #calling back a wanted length
