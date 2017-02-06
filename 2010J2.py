#Up and down

#Nicky forward
a = int(input())
#Nicky backward
b = int(input())
#Byron forward
c = int(input())
#Byron backward
d = int(input())
#Step count
s = int(input())

nicky = 0
nicky_counter = 0
nicky_forward = True

bleh = 1
while bleh <= s:
    if nicky_forward == True:
        nicky += 1
        nicky_counter += 1
        if nicky_counter == a:
            nicky_forward = False
            nicky_counter = 0
    else:
        nicky -= 1
        nicky_counter += 1
        if nicky_counter == b:
            nicky_forward = True
            nicky_counter = 0
    bleh += 1

byron = 0
byron_counter = 0
byron_forward = True
bleh = 1
while bleh <= s:
    if byron_forward == True:
        byron += 1
        byron_counter += 1
        if byron_counter == c:
            byron_forward = False
            byron_counter = 0
    else:
        byron -= 1
        byron_counter += 1
        if byron_counter == d:
            byron_forward = True
            byron_counter = 0
    bleh += 1

if nicky > byron:
    print("Nikky")
elif byron > nicky:
    print("Byron")
elif byron == nicky:
    print("Tied")