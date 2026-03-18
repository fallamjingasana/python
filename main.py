import random
import time
number = random.randint(1,100)
def intro():
    print("may i ask you for your name")
    global name
    name =input()
    print(name+",we are going to play a game i am thinking of a number between 1 and 100")
    if(number%2==0):
        x='even'
    else:
        x='odd'
    print('this is an {} number'.format(x))
    time.sleep(.5)
    print("guess the number")
    def pick():
        while guessestaken < 6:
            time.sleep(.25)
            enter=input("Guess:")
            guess = int(enter)
            if guess<=100 and guessestaken>=1:
                guessestaken=guessestaken+1
                if guessestaken<6:
                    if guess<number:

                      print("the guess that you made is too ")
                    if guess>number:
                       print('the guess that you have mad is too high')
                    if guess!= number:
                        time.sleep(.5)
                        print('try again')
                    if guess==number:
                        break
            if guess>100 or guess<1:
                        print('silly goose that number int in the range')
                        time.sleep(.25)
                        print("please enter a number between 1 and 100")
    except:
            print('idk if its a number')
    if guess == numbr:
        guessestaken= str(guessestaken)
        print('good job you guesed it my numbe')
    if guess !=number:
        print('thats not right')
playagain='yes'
while playagain=='yes':
    intro()
    pick()
    print('do you want to play again')
    playagain=input9
                    



