
#APCSP Project
#Word Game
#Init
import pandas as pd
import random
data = pd.read_csv('2.csv')
words = data["the"].tolist()

turn = 0
win = 0
correct_word = ""
list_of_correct_words = []
list_of_other_letters=[]
user_word_split=[]
global current_word
global user_word
### This program uses the "google-20000-english" dataset.
### Source: https://github.com/first20hours/google-10000-english/blob/master/20k.txt
### Original Data: Derived from the Google Web Trillion Word Corpus (Linguistic Data Consortium)
### Author/Editor: Josh Kaufman
### Date Accessed: March 19, 2026

def pick_word():
    global correct_word
    sorted_number_list = []

    keep_asking = True
    while keep_asking == True:
        user_num = int(input('How many letters? (4 to 9): '))
        if user_num >= 4 and user_num <= 9:
            for i in range(len(words)):
                if len(words[i]) == user_num:
                    sorted_number_list.append(words[i].lower())
            if len(sorted_number_list) > 0:
                correct_word = random.choice(sorted_number_list)
                keep_asking = False
            else:
                print("No words found for that length. Try a different number.")
        else:
            print("Your input was not between 4 and 9.")

def turn_loop(turns):
    global turn
    global win
    global current_word
    global correct_word
    print(f"You will be playing a word game where you get to guess the word before your turns run out! ({turns} attempts)")
    current_word=[]
    for i in range (len(correct_word)):
            current_word.append("_")
    pick_word()
    while win < 1 and turn < turns:
        print(f"--- Turn {turn + 1} ---")
        check_word()
    if win >= 1:
        print(f"Congratulations! You got it: {correct_word}.")
    else:
        print(f"Game Over! The word was: {correct_word}!")

def check_word():
    global turn
    global win
    global user_word
    global user_word_split
    print(f"This is your current word: {current_word}")
    give_other_letters()
    user_word = input("Guess: ").lower()
    user_word_split=list(user_word)

    if user_word == correct_word:
        win = win + 1
        print("You Win!")
    else:
        if len(user_word) == len(correct_word):
            current_word.clear()
            for i in range (len(correct_word)):
                current_word.append("_")
            for i in range(len(correct_word)):
                if correct_word[i] == user_word[i]:
                    current_word[i] = correct_word[i]
            turn = turn + 1
        else:
            print(f"{user_word} is the wrong length.")
            check_word()

def give_other_letters():
    global current_word
    global user_word
    list_of_other_letters = []
    for i in range(len(current_word)):
        if user_word[i] not in current_word and user_word[i] in correct_word:
            if user_word[i] not in list_of_other_letters:
                list_of_other_letters.append(user_word[i])
    print(f"These letters are also in the word: {list_of_other_letters}")


#main

turn_loop(5)

