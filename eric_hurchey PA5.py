#Eric Hurchey
#Programming Assignment #5
#4/7/2022
#

import random
import itertools
from itertools import chain

#listing out all of my global varibales
multiple_words = []
WORD = []
letters = set()
answers = []
file = open("words7.txt")

#calling for printing what the user has done so far
def printboard(clue, guesses, answers):
    for x in answers:
        print(answers[x])
    print(clue)
 
#calling the function that does most of the heavy work, specifically being able to guess or type in h or t or q
def twist(clue, answers):
    hint = clue
    anything = list(clue)
    random.shuffle(anything)
    typed = answers
    answers = {}
    for x in range(len(typed)):
        answers[typed[x]] = "_ " * len(typed[x])
    typed.remove(hint)
    guesses = ""
    while guesses != hint:
        printboard(clue, guesses, answers)
        guesses = input("Guess a word, or q for quit or t for twist or h for a hint: ")
        if guesses in answers:
            if guesses == hint:
                print("Good job! You win!")
                pass
            else:
                answers[guesses] = guesses
                typed.remove(guesses)
        if guesses == "h":
            guesses = random.choice(typed)
            print("You got: ", guesses)
            answers[guesses] = guesses 
        if guesses == "q":
            print("Thanks for playing!")
            break
        if guesses == "t":
            anything = list(clue)
            random.shuffle(anything)
            clue = "".join(anything)
        
#calling for a function to help out the getallwords function to better run the clue and the n-letter values
def getwords(clue, n):
    return ["".join(i) for i in itertools.permutations(clue, n)]
        
#recalls my getwords function so that it finds all of the n-letter extracts from clue
def getallwords(clue):
    for n in range (3, 8):
        WORD.append(getwords(clue, n))
    return WORD
   
#calling my main function so that it can run everything 
def main():
    with open("words7.txt") as file:
        line = file.read().split("\n")
        for x in line:
            if len(x) == 7:
                multiple_words.append(x)
        clue = multiple_words[random.randint(0, len(multiple_words) - 1)]
        GAME = list(chain.from_iterable(getallwords(clue)))
        for x in GAME:
            if x in line:
                letters.add(x)
        answers = list(letters)
        answers.sort(key = len)
        twist(clue, answers)

        
    
main()
