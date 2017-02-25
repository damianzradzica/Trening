# Zad. 5 a
numbers = [i*2.5 for i in range(0, 14)]
print(numbers)

def avg(list):
    sum = 0
    for i in list:
        sum += i
    result = sum/(len(list))
    return result

print(avg(numbers))

# Zad. 5 b
from random import randint

def d6(num):
    result = 0
    for i in range(1, num+1):
        throw = randint(1, 6)
        result += throw
    return result

print(d6(3))