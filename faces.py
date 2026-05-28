#bingjun
#faces

#functions
def convert(msg):
        message = msg.replace(":)", "🙂")
        message = message.replace(":(", "🙁")
        return message







def main():
    msg = input("enter text: ")
    print( convert(msg) )

#program
main()

