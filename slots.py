#slots

#init
import random
import time

#function
def slots():
    symbols = ["7","♫","♫","♫","♫","☾","☾","☾","🂡","🂡","✪","✪"]
    global cash
    cash = 100
    while True:
        print("would you like to spin the slot machine?")
        print("A) yes(-10$)")
        print("B) view balance")
        print("C) add balance")
        print("D) enter test mode")
        spin = input("type response here: ").upper()
        spin.strip()

        if spin == "A":
            if cash >= 10:
                spin1 = symbols[random.randint(0, 9)]
                spin2 = symbols[random.randint(0, 9)]
                spin3 = symbols[random.randint(0, 11)]
                time.sleep(0.5)

                print(f"| {spin1} | {spin2} | {spin3} |")

                #non 7
                if spin1 == "♫" and spin1 == spin2 == spin3:
                    cash = cash + 50
                    print("small win!!!!!")
                    print("+50$")
                    continue
                elif spin1 == "☾" and spin1 == spin2 == spin3:
                    cash = cash + 100
                    print("medium win!!!!!")
                    print("+100$")
                    continue
                elif spin1 == "🂡" and spin1 == spin2 == spin3:
                    cash = cash + 150
                    print("big win!!!!!")
                    print("+150$")
                    continue

                #jackpot
                elif spin1 == "7" and spin1 == spin2 == spin3:
                    cash = cash + 500
                    print("you won the jackpot!!!!!!!!")
                    print("+500$")
                    continue




                elif spin1 == "✪" or spin2 == "✪" or spin3 == "✪":
                    wild1 = symbols[random.randint(0, 9)]
                    wild2 = symbols[random.randint(0, 9)]
                    time.sleep(0.5)

                    print(f"| {wild1} | {wild2} | ✪ |")

                    if wild1 == "♫" and wild1 == wild2:
                        cash = cash + 50
                        print("small win!!!!!")
                        print("+50$")
                        continue
                    elif wild1 == "☾" and wild1 == wild2:
                        cash = cash + 100
                        print("medium win!!!!!")
                        print("+100$")
                        continue
                    elif wild1 == "🂡" and wild1 == wild2:
                        cash = cash + 150
                        print("big win!!!!!")
                        print("+150$")
                        continue

                    #jackpot
                    elif wild1 == "7" and wild1 == wild2:
                        cash = cash + 500
                        print("you won the jackpot!!!!!!!!")
                        print("+500$")
                        continue


                else:
                    cash = cash - 10
                    print("you lost!!!")
                    print("-10$")
                    continue

            else:
                print("you do not have enough funds to play")
                continue



        elif spin == "B":
            print(f"you have ${cash}")
        elif spin == "C":
            load = int(input("how much money wouyld you like to add?: "))
            cash = cash + load
            continue
        elif spin == "D":
            print("you have now entered test mode, you will spin 1000 times")
            tcash = 10000
            for i in range(1000):
                spin1 = symbols[random.randint(0, 9)]
                spin2 = symbols[random.randint(0, 9)]
                spin3 = symbols[random.randint(0, 9)]
                if spin1 == "♫" and spin1 == spin2 == spin3:
                    tcash = tcash - 40

                    continue
                elif spin1 == "☾" and spin1 == spin2 == spin3:
                    tcash = tcash - 90

                    continue
                elif spin1 == "🂡" and spin1 == spin2 == spin3:
                    tcash = tcash - 140

                    continue

                #jackpot
                elif spin1 == "7" and spin1 == spin2 == spin3:
                    tcash = tcash - 490

                    continue

                else:
                    tcash = tcash +10

                    continue
            tprofit = tcash - 10000
            print(f"total profits: {tprofit}")
            print(f"total spent: 10000")




#main
slots()
