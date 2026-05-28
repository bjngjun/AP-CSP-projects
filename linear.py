#linear
#bingjun

#init
import random

#function
def binary_search():
    guess =1
    attempt = 0
    low = 1
    high = 100
    found = False
    secret_number = random.randint(1,100)
    while found == False:
        mid = (low+high) // 2
        if  mid < secret_number:
            low= mid + 1
        if mid > secret_number:
            high = mid - 1
        elif mid == secret_number:
            found = True
            print(f"the bot found the number after {guess} guesses")
            break
        else:
            attempt=attempt + 1
            guess = guess + 1
            continue


def main():
    guess = 1
    attempt = 0
    secret = random.randint(1,100)
    print(secret)
    for guess in range(1,101):
        if guess == secret:
            print(f"bot found the number after {guess} times")
        else:
            attempt = attempt + 1
            guess = guess + 1


#main
binary_search()
