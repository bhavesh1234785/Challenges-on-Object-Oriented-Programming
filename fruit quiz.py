import random
class FruitQuiz:
    #create a constructor
    def __init__(self):
        #create a dictionary of fruits as keys and color as value
        self.fruits={'apple':'red',
                     'orange':'orange',
                     'watermelon':'green',
                     'banana':'yellow'}
    #function for the quiz, here a fruit will be chosen randomly
    def quiz(self):
        while(True):
            fruit,color=random.choice(list(self.fruits.items()))
            print("what is the color of {}".format(fruit))
            user_answer=input()
            if(user_answer.lower()==color):
                print("correct answer")
            else:
                print("wrong answer")
            option = int(input("enter 0, if you want to play again otherwise enter 1: "))
            if (option):
                break
print("welcome to the fruit quiz")
fq=FruitQuiz()
fq.quiz()