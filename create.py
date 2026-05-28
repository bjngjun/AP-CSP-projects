#This program is the game of hangman where the player only has 8 tries to guess the word

#init
#imports pdf list
import pandas as pd
import random

#functions
def main(keyword):

    #defining each difficulty's words from the word list
    data = pd.read_csv("word.csv")
    easy = data['1'].tolist()
    medium = data['2'].tolist()
    hard = data['3'].tolist()

    #title
    print("welcome to hangman")
    print("this is a game where you guess the letters in a mystery word")
    print("")

    #if parameter is "admin" it gives infinite attempts
    if keyword == "admin":
        print("infinite lives enabled")
        print("set parameter to 'normal' to disable")
        #the infinite number comes from https://stackoverflow.com/questions/34264710/what-is-the-point-of-floatinf-in-python
        attempt = float('inf')
        print("")

    #if the parameter is "normal" it gives the standard six attempts
    elif keyword == "normal":
        attempt = 8
        print("infinite lives disable")
        print("set parameter to 'admin' to enable")
        print("")

    else:
        print("you have not typed in the correct parameter")
        print("your parameter must be either 'normal' or 'admin'")
        return

    #difficulty selection
    while True:
        print("what difficulty would you like to play?")
        print("A) easy")
        print("B) medium")
        print("C) hard")
        dif = input("type in your input here: ").upper()
        dif = dif.strip()
        print("")

        #if the player chooses easy mode it multiples the display by the amount of letters in the random easy word
        if dif == "A":
            data = easy
            answer = random.choice(data).lower()
            word = list(answer)
            #the idea to use underscores as spaces for the words comes from https://www.geeksforgeeks.org/python/hangman-game-python/
            display = [" _ "] * len(word)
            break

        #if the player chooses medium mode it multiples the display by the amount of letters in the random medium word
        elif dif == "B":
            data = medium
            answer = random.choice(data).lower()
            word = list(answer)
            display = [" _ "] * len(word)
            break

        #if the player chooses hard mode it multiples the display by the amount of letters in the random hard word
        elif dif == "C":
            data = hard
            answer = random.choice(data).lower()
            word = list(answer)
            display = [" _ "] * len(word)
            break

        #player has not selected a valid input
        else:
            print("please type in a valid input")
            print("")

    #a list that stores the players previous letters
    listy = []

    #displays the hangman based on the amount of attempts the player has
    while True:
        #winning display
        if (" _ ") not in display:
            stage9()
            break

        #eight attempts left display
        elif attempt >= 8:
            stage0()

        #seven attempts left display
        elif attempt == 7:
            stage1()

        #six attempts left display
        elif attempt == 6:
            stage2()

        #five attempts left display
        elif attempt == 5:
            stage3()

        #four attempts left display
        elif attempt == 4:
            stage4()

        #three attempts left display
        elif attempt == 3:
            stage5()
        #two attempts left display
        elif attempt == 2:
            stage6()

        #one attempt left display
        elif attempt == 1:
            stage7()

        #losing display
        elif attempt == 0:
            stage8()
            break

        #choosing letter to guesss
        if attempt > 1:
            print(f"you have {attempt} attempts left")
        elif attempt == 1:
            print(f"you have {attempt} attempt left")
        print("")
        print(*display)
        print("")
        print("guess the letter in the word")
        guess = input("type in your input here: ").lower()
        guess = guess.strip()
        print("")

        #setting the "count" variable to zero to start a new loop
        count = 0

        #if the input is equal to a single character the check starts
        if len(guess) == 1:
            #if player not used letter yet
            if guess not in listy:
                listy.append(guess)
                for i in range(len(display)):
                    if guess in word[i]:
                        display[i] = (f" {guess} ")
                        count = count + 1

                #if the "count" variable is higher or equal to one then the program runs text to tell the player
                if count >= 1:
                    print(f"there was {count} instances of the letter '{guess}' in the mystery word")

                #if the "count" variable is equal to zero the program runs text to tell the player and also removes one attempt unless admin mode is on
                elif count == 0:
                    print(f"the letter '{guess}' is not in the word")
                    if keyword == "normal":
                        attempt = attempt - 1
                    elif keyword == "admin":
                        attempt = attempt

            #if player has already used letter
            elif guess in listy:
                print(f"you have already tried this letter")

        #if the input's length is not equal to 1 letter then the player is informed and sent back to the menu
        else:
            print("please type in a valid input")
        print("")

    #player did not guess the word game end screen
    if attempt == 0:
        print("")
        print(f"the mystery word was '{answer}'")
        print("the man is now hanging")
        print("")
        print("YOU LOSE")
        print("")

    #player did guess the word game end screen
    elif (" _ ") not in display:
        print("")
        print(f"you correctly guessed the word as '{answer}'")
        print("the hangman is now free")
        print("")
        print("YOU WIN")
        print("")

#all of the custom text below come from "https://www.i2symbol.com/symbols/line"

def stage9():
    print("━━━━━━━━━          ")
    print("┃                  ")
    print("┃               () ")
    print("┃              |[]|")
    print("┃               || ")

def stage8():
    print("━━━━━━━━━ ")
    print("┃      () ")
    print("┃     |[]|")
    print("┃      || ")
    print("┃         ")

def stage7():
    print("━━━━━━━━━ ")
    print("┃      () ")
    print("┃     |[]|")
    print("┃      |  ")
    print("┃         ")

def stage6():
    print("━━━━━━━━━ ")
    print("┃      () ")
    print("┃     |[]|")
    print("┃         ")
    print("┃         ")

def stage5():
    print("━━━━━━━━━ ")
    print("┃      () ")
    print("┃     |[] ")
    print("┃         ")
    print("┃         ")

def stage4():
    print("━━━━━━━━━ ")
    print("┃      () ")
    print("┃      [] ")
    print("┃         ")
    print("┃         ")

def stage3():
    print("━━━━━━━━━ ")
    print("┃      () ")
    print("┃      [  ")
    print("┃         ")
    print("┃         ")

def stage2():
    print("━━━━━━━━━ ")
    print("┃      () ")
    print("┃         ")
    print("┃         ")
    print("┃         ")

def stage1():
    print("━━━━━━━━━ ")
    print("┃      (  ")
    print("┃         ")
    print("┃         ")
    print("┃         ")

def stage0():
    print("━━━━━━━━━ ")
    print("┃         ")
    print("┃         ")
    print("┃         ")
    print("┃         ")

#main
main("normal")

