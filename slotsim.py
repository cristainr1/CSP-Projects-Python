#Cristian Romero
#GAMBLING
import random
import time
def oreo():
    money=0
    print("Hello! The machine will spin 5 times, your score is determined by the last set. Each spin costs 10 credits.")
    money=int(input("How many credits do you have? (50,100,500): "))
    xy=0
    sy=['♠', '♣', '☆', '7']
    while xy==0:
        xy=0
        if 10>money:
            print("INSUFFICIENT FUNDS. PLEASE INSERT CREDITS.")
            yw=int(input("How many credits do you want to add? Type 0 if 0. (50, 100, 500): "))
            if yw==0:
                break
            else:
                money=money+yw
        for i in range (4):
            x= sy[random.randint(0,3)]
            y= sy[random.randint(0,3)]
            z= sy[random.randint(0,3)]
            print(x     ,y     ,z)
        x= random.randint(0,3)
        y= random.randint(0,3)
        z= random.randint(0,3)
        print(sy[x]     ,sy[y]     ,sy[z])
        if x==3 and y==3 and z==3:
            print("You win the jackpot! (1) +1000$")
            #global money
            money=money+1100

        if x==2 and y==2 and z==2:
            print("You win the jackpot! (2) +5000$")
            #global money
            money=money+510

        if x==1 and y==1 and z==1:
            print("You win the jackpot! (3) +250$")
            #global money
            money=money+260

        if x==0 and y==0 and z==0:
            print("You win the jackpot! (4) +125$")
            #global money
            money=money+135

        else:
            money=money-10
            print(f"You have {money} credits.")
        xw=int(input(f"what would you like to do? 1==Continue 2==Add Money 3==Cashout (1,2,3): "))

        if xw==1:
            continue
        if xw==2:
            yy=int(input("How many credits do you want to add? Type none if none. (50, 100, 500): "))
            money=money+yy
        if xw==3:

            print(f"You have {money} credits!.")
            break



oreo()
