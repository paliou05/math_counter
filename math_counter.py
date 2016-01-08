import operator
import random
import time
import threading
from random import randint


def random_calc():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}
    num1 = randint(40,80)
    num2 = randint(1,40)
    op = random.choice(list(ops.keys()))
    answer = int(ops.get(op)(num1,num2))
    print('What is {} {} {}?\n'.format(num1, op, num2))
    return answer

def ask_question():
    answer = random_calc()
    print answer
    guess = (input("Give your answer\n>"))
    if guess == answer:
        print "Correct"
    else:
        print "Wrong"
        
def background(f):
    def bg_f(*a, **kw):
        threading.Thread(target=f, args=a, kwargs=kw).start()
    return bg_f

@background
def counter(n):
    for k in range(0, n+1):
        print("You have {} seconds to answer.".format(n-k))
        time.sleep(1)
    return

 
def menu():
    while True:
        select  = input("To play press (1)\nTo exit press (2)\n>")
        if select == 1:
            game_s = input("Select your game(seconds)>")
            game_q = input("Select your game(questions)>")
            for i in range(game_q):
                counter(game_s)
                ask_question()
                #    reset_counter()
        elif select == 2:
            break
                
if __name__ == '__main__':
    menu()