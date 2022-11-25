import random

print("Tic Tac Toe Game")

print("In the two digit below, the first digit represents row, and second digit represents column")
game=[["00","01","02"],["10","11","12"],["20","21","22"]]

#use for loop to iterate the array
for rows in game:
    for columns in rows:
       print(columns,end=" ")
    print()
   
userinputR = input("Enter the row from 0, 1, 2: ")
userinputC = input("Enter the column from 0, 1, 2: ")

compChoiceR = random.randint(0,2)
compChoiceC = random.randint(0,2)

game[userinputR][userinputC] = "X"
game[compChoiceR][compChoiceC] = "O"



