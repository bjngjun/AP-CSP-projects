#bingjun
#pokemon evolution

#init
import time
import random

#global
day = 1
level = 1
player = "name"
name = "name"
energy = 1
evolution = "polywag"

#function
def greeting():
    global name
    global player
    wait()
    print("welcome to pokemon codespace")
    wait()
    player = input("type in your name: ")
    wait()
    print(f"hello {player}")
    wait()
    print("today you start your new life as a pokemon trainer!")
    wait()
    print("you recived a poliwag as your first pokemon!")
    wait()
    name = input("what would you like to name your pokemon?: ")
    wait()
    print(f"your polywag is now named {name}")

def evo1():
    print((r" _..__                                    ___\n"))
    print((r"/     `._                          ,--\"\"\"\"   `\"-.\n"))
    print(("|         `.                    _.'\"\"/`.        |/`-.\n"))
    print(("|           `.                ,+ `..' | |       |'...+.\n"))
    print(("|     \\       \\              / /\\____,' '    __ `.`._,\".\n"))
    print(("|      ..      \\           ,'  \\      .' ,-\"'  `. `.._,'`.\n"))
    print(("|       .`.     \\         /     `-..-'  .  _.... |._      \\\n"))
    print(("'        ' `     \\       /          ,-\"\"`.____...'  `.     \\\n"))
    print((r"`        `.`.    \\     '         ,'   _,--------.`.  `.    L\n"))
    print((r" `         ` `.   \\   j         /  .,' ,\"_.....`.`.`   \\   |\n"))
    print((r"  `.        `. `.  \\  |        / ,'/ .','..... `.\\ \\|   .  |\n"))
    print((r"    `.        `. .  \\ |       j . / ..'.,-\"\". \\ || ||   |  |\n"))
    print((r"      `.        `.`. \\'.      | | | |||.   .,.','/ /'   |  |\n"))
    print((r"        `-.       `. .:\\      | | | ||'`..___.'.','/   j   |\n"))
    print((r"           `-._     `-._\\      \\'.`.`..`..__....','   ,   /\n"))
    print((r"               `--......-\\      \\ `.`.`.......-\"'   ,'   /\n"))
    print((r"                          `.     `. `-..____,.-\" _.'   ,'\n"))
    print((r"                            >.     '--...___,..-'   _.\"\n"))
    print((r"                          ,'  `--,__            _,-\"  `-.\n"))
    print((r"                      _.-'      '   `'--------\"' `.      `-.\n"))
    print((r"                    .'        ,'                   \\        `.\n"))
    print((r"                   .        .'                      `.        .\n"))
    print((r"                   |      ,'                          `._     |\n"))
    print((r"                    `----'                               `\"--\" mh\n"))
    print(("\n"))
    print(("\n"))

def evo2():
    print((r"            ___   _,-'\"\"-.\n"))
    print((r"          /`.  `./,\\`.    `.\n"))
    print((r"         /'. |  / || |      .\n"))
    print((r"        . `|,+-'| `| |       `._\n"))
    print((r"        `,-'    `. | '          `.\n"))
    print((r"       ,' -'      `\"'             `.\n"))
    print((r"      /\"`-.                         `.\n"))
    print((r"     :`.   \\                          .\n"))
    print((r"    ' `.\\   \\                          `\n"))
    print((r"   .`.  .`   `           `.             .\n"))
    print((r"  / `.'  .`   .      .     \\             \\\n"))
    print((r" /``  .`  `\\   .      \\     .             .\n"))
    print((r"j  .\\  .:  .'  :       .    '             |\n"))
    print((r"|`. .. ||  :|  |        ,..--`._          |\n"))
    print((r"|:| |: :|  |:  |      ,'        |         |\n"))
    print((r"||| :: |:  |:  |      |         |         |\n"))
    print((r":'j '| :|  :|  |      |         |         |\n"))
    print((r"`/ .j  ,:  :|  |     ,'         `         |\n"))
    print((r" \\/ / . '  ',  |   .'            \\        '\n"))
    print((r" ` , /,'  /.  j   |               .      /\n"))
    print((r"  `.'/   /'   '   |  .             .   ,'\n"))
    print((r"    .  .'/   /    `._/             '  /\n"))
    print((r"     `.,'   /       |          __,' .'\n"))
    print((r"       `-._,         `.   _,.-\" _,-'\n"))
    print((r"           `+..____    `\"'    .'\n"))
    print((r"          _/    |  `\"\"\"''\\    '\n"))
    print((r"    _,.-\"'      \\        |     \\\n"))
    print((r"_.-'             .       |      `\n"))
    print((",                 |       |       `.\n"))
    print(("`_          __,,-'        '         `.\n"))
    print((r" `'\"\"'\"'\"''             .            .\n"))
    print((r"                        |            |\n"))
    print((r"                        '            /\n"))
    print((r"                         `.        ,'\n"))
    print((r"                           `-..,.-' mh\n"))

def evo3():
    print((r"                              __,.-\"\"\"'\"--..._.,---.\n"))
    print((r"                          _,-'               /      `.\n"))
    print((r"                       _.'                 ,'   ,-\"\"`.|\n"))
    print((r"                     ,'                        / ,+\"`.;\n"))
    print((r"                   ,'   ____                  . |_/  /\n"))
    print((r"                  /  .\"'    `-.               ` `..-/`.  _\n"))
    print((r"                 '  /                     .    `---'   `: `.\n"))
    print((r"                /  .    ,-\"\"`.           .'             \\`-.`+\"\"`\"`.\n"))
    print((r"               /   |  .' ,\"\".|               _,...,._    L |  `     `.\n"))
    print((r"              /    |  | ._)  /     \\    _.-\"'        \"`. | j          .\n"))
    print((r"             j     `  ' |  ,'        ,-'   ___......_   .|\"           |\n"))
    print((r"             |         `-+'        ,'  _,\"__.---\"\"\"`-.`.||            |\n"))
    print((r"             '                   ,'  ,'.-'    _______ `.`|\\           |\n"))
    print((r"           .\"                   /  ,\",'   _,\"+.------+`.`:|           |\n"))
    print((r"         ,'     .             ,' .,-'   .\".-'  _..._  ` \\''    .      ;\n"))
    print((r"      _,+      /             ,  ,/    ,'.' .-\",.----.+ `7  `.   `._,.'\n"))
    print((r"     /  '    ,'             .  '.   ,\".\" .:,-'__     :|j     `-.-'\n"))
    print((r"    j    \\  /|`            ,  //   .,' ,'.' .\"__`.   ||'\n"))
    print((r"  ,-+     `\" | \\             /.   //  /,\" ,'.'  \\ \\  |'\n"))
    print((r" /           '  \\         : j '  //  //  .,'     || ,\"\n"))
    print((r"/           /    \\        | :|  j.' j/   ||_.\") , ;<_\n"))
    print((".            `-.   `.      : ||  || |.    `..-'.'.'   `'-._\n"))
    print(("|              |     `.    | |:  :| |'        _,'          `.\n"))
    print(("|              |      /`-._`.`:. \\' `.`..__.-'+              `\n"))
    print(("`          .   F     ,     /\"`+-+.^+--`\"\"\"     `._            |\n"))
    print((r"`.       |   /     /     .                       `._         /\n"))
    print((r"  `._   _,..'    ,'      '                          `\"-....-'\n"))
    print((r"     `\"\"        /       j\n"))
    print((r"              ,'        |\n"))
    print((r"             /          |\n"))
    print((r"            j           '\n"))
    print((r"            |          /\n"))
    print((r"            |         /\n"))
    print((r"            '        /\n"))
    print((r"             `.___,.' mh\n"))

def wait():
    print("")

def main():
    global day
    global name
    global player
    global energy
    global level
    global evolution
    greeting()
    wait()

    while True:
        #evolution 2
        if level >= 5:
            evolution = "polywhirl"

        #evolution 3
        elif level >= 10:
            evolution = "polywrath"

        #start of day
        print(f"day {day}")
        wait()
        print("what would you like to do today?")
        print("A) rest")
        print("B) train")
        print("C) info")
        print("D) gym")
        choice = input("type in your choice: ").upper()

        #rest
        if choice == "A":
            wait()

            #true
            if energy == 0:
                day = day + 1
                energy = 1
                wait()
                print(f"{name} goes to sleep")

                print(f"{name} is fully rested")
            #false
            elif energy == 1:
                day = day
                print(f"{name} isn't tired")
                print(f"{name} wants to train")

            wait()
            continue

        #train
        elif choice == "B":
            wait()

            #true
            if energy == 1:
                day = day + 1
                energy = 0
                level = level + 1
                print(f"{name} trains for the day")
                print(f"{name} is now level {level}")

            #false
            elif energy == 0:
                day = day
                print(f"{name} has no energy to train")
                print(f"{name} needs to rest")

            wait()
            continue

        #info
        elif choice == "C":
            day = day
            wait()
            print(f"{evolution}({name})")
            print(f"level: {level}")
            wait()
            if evolution == "polywag":
                evo1()

            elif evolution == "polywhirl":
                evo2()

            elif evolution == "polywrath":
                evo3()

        #gym
        elif choice == "D":
                wait()
                wait()
                wait()
                wait()
                wait()
                wait()
                wait()
                print(f"day {day}")
                wait()
                print("what would you like to do at the gym?")
                print("A) train")
                choice2 = input("type in your choice: ").upper()

                #train 2
                if choice2 == "A":
                    #true
                    if energy == 1:
                        wait()

                        #chance
                        if level <=15:
                            print(f"you and {name} decide to challenge the gym")
                            chances = random.randint(level,15)

                            #win
                            if chances > 10:
                                level = level + 5
                                day = day + 1
                                energy = 0
                                print(f"{name} won the battle and is now level {level}")
                                wait()
                                continue

                            #lost
                            elif chances <= 10:
                                day = day + 1
                                energy = 0
                                print(f"{name} loses and returns home")
                                wait()

                        #instant
                        elif level >= 15:
                                level = level + 5
                                day = day + 1
                                energy = 0
                                print(f"{name} won the battle and is now level {level}")
                                wait()

                    #false
                    elif energy == 0:
                        day = day
                        wait()
                        print(f"{name} has no energy to do the gym battle")
                        print(f"{name} needs to rest")
                        wait()
                        continue

                else:
                    wait()
                    print("please type in a valid choice")
                    wait()
                    continue

        #error
        else:
            wait()
            print("please type in a valid choice")
            wait()
            continue

#main
main()
