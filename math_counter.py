import operator
import random
from random import randint

def randomCalc():
    ops = {'+':operator.add,
           '-':operator.sub,
           '*':operator.mul,
           '/':operator.truediv}
    num1 = randint(40,80)
    num2 = randint(1,40)
    op = random.choice(list(ops.keys()))
    answer = ops.get(op)(num1,num2)
    print('What is {} {} {}?\n'.format(num1, op, num2))
    return answer

def askQuestion():
    answer = randomCalc()
    print answer
    guess = float(input("Give your answer\n>"))
    
    if guess == answer:
        print "Correct"
    else:
        print "Wrong"

if __name__ == '__main__':
    askQuestion()