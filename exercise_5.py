# Zad. 5
numbers = [i*2.5 for i in range(0, 14)]
print(numbers)

def avg(list):
    sum = 0
    for i in list:
        sum += i
    result = sum/(len(list))
    return result

print(avg(numbers))