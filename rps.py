#rock paper sissors
#play against the computer in a game of rock paper sissors
#bingjun

#init
import random
import time
#function
def rps():
    computerwins = int(0)
    playerwins = int(0)
    ties = int(0)
    while True:
        computer = random.randint(1,3)
        if computer == 1:
            opponent = ("rock")
        elif computer == 2:
            opponent = ("paper")
        elif computer == 3:
            opponent = ("sissors")

        print(f"computer wins:{computerwins}")
        print(f"player wins:{playerwins}")
        print(f"ties:{ties}")

        print("Choose one of the following")
        print("A) rock")
        print("B) paper")
        print("C) sissors")
        option = input("type in your choice: ").upper()

        #rock
        if option == "A":
            player = ("rock")
            #tie
            if computer == 1:
                print(" ")
                print(f"you chose {player}")
                print(f"the computer chose {opponent}")
                print(" ")
                print("TIE")
                print(" ")
                ties = ties + 1

                print("would you like to continue playing?")
                print("A) yes")
                print("B) no")
                end = input("").upper()
                if end == "A":
                    continue
                elif end == "B":
                    return
                print(" ")

            #win
            elif computer == 3:
                print(" ")
                print(f"you chose {player}")
                print(f"the computer chose {opponent}")
                print(" ")
                print("WIN")
                print(" ")
                playerwins = playerwins + 1

                print("would you like to continue playing?")
                print("A) yes")
                print("B) no")
                end = input("").upper()
                if end == "A":
                    continue
                elif end == "B":
                    return
                print(" ")

            #lost
            elif computer == 2:
                print(" ")
                print(f"you chose {player}")
                print(f"the computer chose {opponent}")
                print(" ")
                print("LOSE")
                print(" ")
                computerwins = computerwins + 1

                print("would you like to continue playing?")
                print("A) yes")
                print("B) no")
                end = input("").upper()
                if end == "A":
                    continue
                elif end == "B":
                    return

        #paper
        if option == "B":
            player = ("paper")
            #tie
            if computer == 2:
                print(" ")
                print(f"you chose {player}")
                print(f"the computer chose {opponent}")
                print(" ")
                print("TIE")
                print(" ")
                ties = ties + 1

                print("would you like to continue playing?")
                print("A) yes")
                print("B) no")
                end = input("").upper()

                if end == "A":
                    continue
                elif end == "B":
                    return
                print(" ")

            #win
            elif computer == 1:
                print(" ")
                print(f"you chose {player}")
                print(f"the computer chose {opponent}")
                print(" ")
                print("WIN")
                print(" ")
                playerwins = playerwins + 1

                print("would you like to continue playing?")
                print("A) yes")
                print("B) no")
                end = input("").upper()
                if end == "A":
                    continue
                elif end == "B":
                    return
                print(" ")

            #lost
            elif computer == 3:
                print(" ")
                print(f"you chose {player}")
                print(f"the computer chose {opponent}")
                print(" ")
                print("LOSE")
                print(" ")
                computerwins = computerwins + 1

                print("would you like to continue playing?")
                print("A) yes")
                print("B) no")
                end = input("").upper()
                if end == "A":
                    continue
                elif end == "B":
                    return

        #sissor
        if option == "C":
            player = ("sissor")
            #tie
            if computer == 3:
                print(" ")
                print(f"you chose {player}")
                print(f"the computer chose {opponent}")
                print(" ")
                print("TIE")
                print(" ")
                ties = ties + 1

                print("would you like to continue playing?")
                print("A) yes")
                print("B) no")
                end = input("").upper()

                if end == "A":
                    continue
                elif end == "B":
                    return
                print(" ")

            #win
            elif computer == 2:
                print(" ")
                print(f"you chose {player}")
                print(f"the computer chose {opponent}")
                print(" ")
                print("WIN")
                print(" ")
                playerwins = playerwins + 1

                print("would you like to continue playing?")
                print("A) yes")
                print("B) no")
                end = input("").upper()
                if end == "A":
                    continue
                elif end == "B":
                    return
                print(" ")

            #lost
            elif computer == 1:
                print(" ")
                print(f"you chose {player}")
                print(f"the computer chose {opponent}")
                print(" ")
                print("LOSE")
                print(" ")
                computerwins = computerwins + 1

                print("would you like to continue playing?")
                print("A) yes")
                print("B) no")
                end = input("").upper()
                if end == "A":
                    continue
                elif end == "B":
                    return
        else:
            print(" ")
            print("please type in a valid letter option")
            print(" ")
            continue


#main
rps()
