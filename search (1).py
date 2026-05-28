#Cristian Romero
# secret numbers


import random
#y= random.randint(1,100)
y= 1234567891011101987654321
print("")
print("#####################################################################")
secret_number=random.randint(1,y)

print(f"The secret number is {secret_number}.")



def linear_search():
    global secret_number
    global y
    print("***Linear Search Starts Here***")
    attempts=0
    for guess in range (1,y):
        attempts=attempts+1
        if guess==secret_number:

            print(f"It took {attempts} attempts to find the secret number which is {guess}.")
            print("#####################################################################")
            print("")


def binary_search():
    global secret_number
    global y

    print("***Binary Search Starts Here***")
    low=1
    high=y
    found=False

    attempts=0
    while found == False:
        mid=(low+high)//2
        if secret_number==mid:
            found=True
            print(f"It took {attempts} attempts to find the secret number which is {mid}.")

        elif mid> secret_number:
            high=mid
        elif mid< secret_number:
            low=mid
        attempts=attempts+1







binary_search()
linear_search()
