import random
def  guess_number():
    return random.randint(1,100)
target_number=guess_number()
attempts=0
while True:
    user_guess=int(input("guess the number:"))
    attempts+=1

    if user_guess==target_number:
        print("congratulations! you guessed the number in n ",attempts,"attempts")
        break
    elif user_guess<target_number:
        print("try a higher number")
    else:
        print("try a lower number")