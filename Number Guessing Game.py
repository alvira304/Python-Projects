# import random and time module
import random
import time

guess = 0
tries = 0                    

#Generating random number between 1 to 10
number = random.randint(0,10)

#Greeting the user
name = input("Enter your name : ")
name= ("Hello "+name.capitalize()+" !")
print("-" * 30)
print(name.center(30))
print("-" * 30)
time.sleep(1)

#processing user's decision
question = input("Are you ready to guess ? [Y/N]: ")
if question.lower() == 'n':
    print("Okay! We expect you soon")
    exit()
if question.lower() == 'y':
    time.sleep(1)
    print("Great, Let's Play\n")
    time.sleep(1)
    print("I'm thinking of number betwen 1 & 10\n")
    time.sleep(1)
    
#guessing the number and printing the result
while not(guess==number):   #it means guess is not equal to number
    guess = int(input("\nGuess the number : "))
    tries +=1                           # this calculates the number of tries
    if guess == number :  # if guess gets equals to number exit the while loop
        print("\ncongratulation ! you guessed it right.")
        time.sleep(1)
        print("The number is {}.".format(number))
        print("\nit has taken you {} tries.".format(tries))
        time.sleep(1)
        print("\nThank you for playing.")
        exit()                        
    
    elif (guess > number) :           # if guess is greater than number
        print("\nNo! Guess lower number")

    elif (guess < number) :           # if guess is smaller than number
        print("\nNo! Guess higher number")

