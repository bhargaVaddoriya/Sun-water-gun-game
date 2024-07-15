
'''
1 : snack
-1 : water
0 : gun
'''
import random


def calculation(computer_num,user_num):

    if computer_num == -1 and user_num == 1:
        print ("User Win")
    elif computer_num == -1 and user_num == 0:
        print( "You Lose a Game")
    elif computer_num == 1 and user_num == -1 :
        print( "You Lose a Game")
    elif computer_num == 1 and user_num == 0 :
        print( "You Win")
    elif computer_num == 0  and user_num == -1 :
        print( "You Win")
    elif computer_num == 1 and user_num == 1 :
        print( "You Lose a Game")
    else:
        print( "Something went wrong.")
    

computer = random.randint(-1,1)

youdict = {
 "s" : 1,
 "w" : -1 ,
 "g" : 0
    }
reverseDict = {
1 : "Snake",
-1 : "Water",
0 : "Gun"

}

is_true = True

while is_true:
    younum = youdict[input("Enter s for snack ,w for water and g for gun. : ")]
    print(f"Computer Chooes {reverseDict[computer]}")
    calculation(computer,younum)

    again=input("Do you want to Play again!, yes or no :")
    if again == "no":
        is_true = False
    