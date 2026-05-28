#Cristian Romero
#Create a game #4
import time
import random
y=str(input("How hard do you want your game? (easy, medium, or hard): "))
if y =="easy":
    x=10
elif y=="medium":
    x=20
elif y=="hard":
    x=30
number=random.randint(1,x)
name=input("What is your name?: ")
#print(high2)
start_time = time.perf_counter()
def five():
    message=f"You have 5 chances!"
    print(message)
    for i in range (5):
        messaget=f"Guess a number 1 to {x}!: "
        guess=int(input(messaget))
        if guess == number:
            print("***You got it!***")
            w=end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            g=30-elapsed_time
            g=round(g,1)
            messagem=f"Your score is {g}!"
            print(messagem)
            


            break
        elif guess == number +1 or guess== number -1 :
            print("HOT")
        elif guess == number +2 or guess== number -2:
            print("WARM")
        else:
            print("COLD")
    mess=f"The Number was {number}!"
    print(mess)
def scores():

    high2=0
    nameh=f"unknown"
    if global_g > high2:
        high2=g
        nameh=name
    gg=f"***{nameh} has the highest score of {g} for {y}.***"
    print(gg)
end_time = time.perf_counter()

five()
scores()
