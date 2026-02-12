'''
1 for snake
-1 for water
0 for gun
'''
import random
choices = [-1,1,0]
computer = random.choice(choices)
comp_dict = {1 : "snake" , -1 : "water" , 0 : "gun"}
youstr = input("Enter your choice : ")
youDict = {"s": 1 , "w" : -1 , "g" : 0}
you = youDict[youstr]
print(f"The Computer's choice was {comp_dict[computer]}")
print(f"Your choice was {comp_dict[you]}")

if(computer == you):
    print("It's a Draw!")
elif (computer == -1 and you == 1):
    print("You win!")
elif (computer == -1 and you == 0):
    print("You Lose!")
elif (computer == 1 and you == 0):
    print("You Win!")
elif(computer == 1 and you == -1):
    print("You Lose!")
elif (computer == 0 and you == 1):
    print("You Lose!")
elif(computer == 0 and you == -1):
    print("You win!")
else:
    print("Something went wrong!!")