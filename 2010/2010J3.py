#Punchy
#Feb 6, 2016
#Isabelle (15.477 years old)

#omg an import!!!!!
import math

#Initially, the variables A and B contain the value 0.
A = 0
B = 0

#1 X n means set the variable X to the integer value n;
def newValue(x, n):
    x = n
    return x

#2 X means output the value of variable X to the screen;
def output(x):
    print(x)

#3 X Y means calculate X + Y and store the value in variable X;
def add(x, y):
    x += y
    return x

#4 X Y means calculate X  Y and store the value in variable X;
def multiply(x, y):
    x *= y
    return x

#5 X Y means calculate X - Y and store the value in variable X;
def subtract(x, y):
    x -= y
    return x

#6 X Y means calculate the quotient of X/Y and store the value in variable X as an integer, discarding the remainder.
def divide(x, y):
    x /= y
    if x > 0:
        x = math.floor(x)
        return x
    elif x < 0:
        #Round up if it's negative 'cause yeah
        x = math.ceil(x)
        return x

#Set the letters to be variables.
def toVar(letter):
    if letter == "A":
        return A
    else:
        return B

#index 1 is first space, index 3 is second space.
def read():
    b = B
    a = A
    while True:
        entered = raw_input()
        if entered == "7":
            break
        else:
            letter = entered[2]
            letter = toVar(letter)
            number = entered[0]
            if number == "1":
                value = int(entered[4:])
                letter = newValue(letter, value)
            elif number == "2":
                output(letter)
            elif number == "3":
                letter2 = entered[4]
                letter2 = toVar(letter2)
                add(letter, letter2)
            elif number == "4":
                letter2 = entered[4]
                letter = toVar(letter2)
                multiply(letter, letter2)
read()
