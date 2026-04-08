import random
class fruitquiz:
    def __init__(self):
        self.fruits = {'apple':'red',
        'banna':'yellow',
        'orange':'orange',
        'watermelon':'green'
        }
    
    def quiz(self):
        while(True):
            fruit,colour = random.choice(list(self.fruits.items()))
            print("what is the colour of {}".format(fruit))
            user_answer = input()
            if ( user_answer.lower()==colour):
                print("correct answer")
            else:
                print("wrong answer")
            option = int(input("enter 0 if you want to play again else ener 1: "))
            if (option):
                break
print("welcome to fruit quiz")
fq = fruitquiz()
fq.quiz()