import random
num=random.randint(1,100)

i=0

while i<50:
    n=int(input("Guess the number, its can be any num 1 to 100. ONLY 4 tries!!!\n"))
    if n==num:
        print("You win!!!")
        i=50
    elif n>num:
        print("Too high")
        i+=1
    else:
        print("Too low")
        i+=1