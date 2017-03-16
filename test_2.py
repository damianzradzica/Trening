def binary(number):
    result = bin(number)[2:]
    return result

def solution(N):
    # write your code in Python 2.7
    value = bin(N)[2:]
    long = len(value)
    result = 0
    for i in range(0, long-1):
        if int(value[i]) == 1 and int(value[i+1]) == 0 and str(1) in value[i+1:]:
            count = 1
            while int(value[i+1+count]) == 0:
                count += 1
            # elif int(value[i+1+count]) == 1:
            else:
                if count > result:
                    result = count
    return result



liczba = 529
print(binary(liczba))
print(solution(liczba))