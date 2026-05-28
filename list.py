#bingjun
#list

#int

#function
def list():
    list = []
    done = []

    while True:
        print("")
        print("welcome to the to-do list")
        print(f"to-do list: {list}")
        print(f" done list: {done}")
        print("please choose a option")
        print("A) add")
        print("B) remove")
        print("C) complete")
        print("D) quit")
        start = input("type in your option here: ").upper()
        start = start.strip()

        if start == "A":
            while True:
                print("")
                print(list)
                add = input("please type in the task you would like to add: ").lower()
                checkA = add.isspace()
                add = add.strip()

                if checkA == True:
                    print("invalid input")
                    break
                elif checkA == False:
                    list.append(add)
                    print(f"{add} successfully added to list")
                    break

        elif start == "B":
            while True:
                print("")
                print(list)
                remove = input("please type in the task you would like to remove: ").lower()
                checkB = add.isspace()
                remove = remove.strip()

                if checkB == True:
                    print("invalid input")
                    break

                elif checkB == False:
                    if remove in list:
                        list.remove(remove)
                        print(f"{remove} successfully removed from list")
                        break

                    else:
                        print("this task is not on the list")
                        break

        elif start == "C":
            while True:
                print("")
                print(list)
                complete = input("please type in the task you have completed: ").lower()
                checkC = complete.isspace()
                complete = complete.strip()

                if checkC == True:
                    print("invalid input")
                    break

                elif checkC == False:
                    if complete in list:
                        list.remove(complete)
                        done.append(complete)
                        print(f"{complete} successfully removed from to-do list and added to completed list")
                        break

                    else:
                        print("this task is not in the list")
                        break

        elif start == "D":
            print("")
            print("ok bye")
            return

        else:
            print("")
            print("please type in a valid option")
            continue

#main
list()
