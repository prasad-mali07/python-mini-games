# We are going to write a program that generates a random number and asks the user to guess it.
# If the player’s guess is higher than the actual number, the program displays “Lower number please”. Similarly, if the user’s guess is too low, 
# the program prints “higher number please” When the user guesses the correct number, the program displays the number of guesses the player used 
# to arrive at the number.
# Hint: Use the random module.
import random
def guess(): 
    count = 1
    number = int(input("Enter a number : "))
    system_number = random.randint(1 , 100) 
    while(number != system_number):
        if number > system_number:
            print("Try a new number with smaller value")
            number = int(input("Enter the smaller number : "))
            count += 1
        elif number < system_number:
            print("Try a new number with greater value")
            number = int(input("Enter the greater number : "))
            count += 1
    if number == system_number:
        print(f"You guessed the exact number which is {system_number} in {count} guesses")

def main():
    guess()

main()