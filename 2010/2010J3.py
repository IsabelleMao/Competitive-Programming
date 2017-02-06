#Punchy
#Feb 6, 2016
#Isabelle (15.477 years old)

#omg an import!!!!!
import math

#Initially, the variables A and B contain the value 0.
a = 0
b = 0

#1 X n means set the variable X to the integer value n;
def newValue(x, n):
    x = n

#2 X means output the value of variable X to the screen;
def output(x):
    print(x)

#3 X Y means calculate X + Y and store the value in variable X;
def add(x, y):
    x += y

#4 X Y means calculate X  Y and store the value in variable X;
def multiply(x, y):
    x *= y

#5 X Y means calculate X - Y and store the value in variable X;
def subtract(x, y):
    x -= y

#6 X Y means calculate the quotient of X/Y and store the value in variable X as an integer, discarding the remainder.
def divide(x, y):
    x /= y
    if x > 0:
        x = math.floor(x)
    elif x < 0:
        #Round up if it's negative 'cause yeah
        x = math.ceil(x)


def read():
    while True:
        input = input()
