#What is n, Daddy?

n = int(input())
half = n/2

def answer(n):
    if n == 1 or n == 9 or n == 10:
        return 1
    elif n <= 3 or n == 7 or n == 8:
        return 2
    elif n <= 6:
        return 3

answer = answer(n)
print(answer)
