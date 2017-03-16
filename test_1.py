list = [-1, 3, -4, 5, 1, -6, 2, 1]
def solution(array):
    result = []
    long = len(array)
    for P in range(0, long):
        suma_przed = 0
        suma_po = 0
        for element in range(0, P):
            suma_przed += array[element]
            return suma_przed
        for value in range(P+1, long):
            suma_po += array[value]
            return suma_po
        if suma_po == suma_przed:
            result.append(P)
    return result

print(solution(list))


