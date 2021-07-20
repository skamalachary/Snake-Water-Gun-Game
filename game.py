"""skamalachary keep :) fresh"""
import random
li=["s","w","g"]
chance =10
no_of_chance=0
computer_point=0
human_point=0
print("\t\t\tSanke,Water,Gun Game\n\n")
print(" s for snake \n w for water \n g for gun \n")
while no_of_chance < chance:
    _input=input("sanke,water,gun:")
    _random=random.choice(li)

    if(_input==_random):
        print(" Tie both 0 points to each " )
        print(f"you guess {_input} and computer guess {_random}")
    #if user enter S
    elif _input =="s" and _random =="g":
        computer_point=computer_point+1
        print(f"you guesss {_input} and computer guess {_random}")
        print("computer win 1 point")
        print(f"computer points {computer_point} and yourpoints {human_point}")
    elif _input =="s" and _random =="w":
        human_point=human_point+1
        print(f"you guesss {_input} and computer guess {_random}")
        print("you win 1 point")
        print(f"computer points {computer_point} and yourpoints {human_point}") 
    elif _input =="g" and _random =="w":
        computer_point=computer_point+1
        print(f"you guesss {_input} and computer guess {_random}")
        print("computer win 1 point")
        print(f"computer points {computer_point} and yourpoints {human_point}")
    elif _input =="g" and _random =="s":
        human_point=human_point+1
        print(f"you guesss {_input} and computer guess {_random}")
        print("you win 1 point")
        print(f"computer points {computer_point} and yourpoints {human_point}")
    elif _input =="w" and _random =="s":
        computer_point=computer_point+1
        print(f"you guesss {_input} and computer guess {_random}")
        print("computer win 1 point")
        print(f"computer points{computer_point}and yourpoints{human_point}")
    elif _input =="w" and _random =="g":
        human_point=human_point+1
        print(f"you guesss {_input} and computer guess {_random}")
        print("you win 1 point")
        print(f"computer points {computer_point} and yourpoints {human_point}")
    else:
        print("you have input wrong!! \n")
        print("Game Over! \n")
    no_of_chance=no_of_chance+1
    print(f" {chance-no_of_chance} is lesf out of chance {chance} ")
    

if(computer_point == human_point):
     print(" Tie \n")
elif(computer_point > human_point):
     print(" Computer win and you loose  \n")
else:
     print(" You win and Computer loose \n")
print(f"Your poins is {human_point} and Computer points is {computer_point} ")



        


