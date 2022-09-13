from random import random, randrange


rng=randrange(1,10)
secret=int(rng)
attempts=3
guess=0
print("I'm thinking of a number between 1 and 10. I'll give you three tries to guess it!")
while(attempts>0):
    guess=input("So, what do you think it is?")
    if(int(guess)>10):
        print("Hey, that's way too high!")
    elif(int(guess)<1):
        print("Hey, that's way too low!")
    elif(int(guess)>secret):
        attempts=attempts-1
        print("Ooh, that's bit too high. You've got",attempts,"tries left.")
    elif(int(guess)<secret):
        attempts=attempts-1
        print("Ooh, that's a bit too low. You've got",attempts,"tries left.")
    else:
        print("Ooh, that's... Eh, just kidding, you got it right!")
        attempts=0
else:
    print("The number I was thinking of is",str(secret)+".")