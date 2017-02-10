#Punchy
#Feb 6, 2016
#Isabelle (15.477 years old)

#omg an import!!!!!
import math

#index 1 is first space, index 3 is second space.
def read():
    # Initially, the variables A and B contain the value 0.
    A = 0
    B = 0
    while True:
        entered = input()
        if entered == "7":
            break
        else:
            #The letter, A or B.
            letter = entered[2]
            number = entered[0]
            #1 X n means set the variable X to the integer value n;
            if "1" == number:
                if "A" == letter:
                    A = int(entered[4:])
                else:
                    B = int(entered[4:])
            #2 X means output the value of variable X to the screen;
            elif "2" == number:
                if "A" == letter:
                    print(A)
                else:
                    print(B)

            #3 X Y means calculate X + Y and store the value in variable X;
            elif "3" == number:
                if "A" == letter:
                    if "A" == entered[4]:
                        A += A
                    else:
                        A += B
                else:
                    if "A" == entered[4]:
                        B += A
                    else:
                        B += B
            #4 X Y means calculate X * Y and store the value in variable X;
            elif "4" == number:
                if "A" == letter:
                    if "A" == entered[4]:
                        A *= A
                    else:
                        A *= B
                else:
                    if "A" == entered[4]:
                        B *= A
                    else:
                        B *= B
            #5 X Y means calculate X - Y and store the value in variable X;
            elif "5" == number:
                if "A" == letter:
                    if "A" == entered[4]:
                        A -= A
                    else:
                        A -= B
                else:
                    if "A" == entered[4]:
                        B -= A
                    else:
                        B -= B
            #6 X Y means calculate the quotient of X/Y and store the value in variable X as an integer, discarding the remainder.
            elif "6" == number:
                if "A" == letter:
                    if "A" == entered[4]:
                        return 1
                    elif "B" == entered[4]:
                        if A > 0:
                            A = math.floor(A/B)
                        else:
                            A = math.ceil(A/B)
                else:
                    if "B" == entered[4]:
                        return 1
                    elif "A" == entered[4]:
                        if B > 0:
                            B = math.floor(B/A)
                        else:
                            B = math.ceil(B/A)
read()
