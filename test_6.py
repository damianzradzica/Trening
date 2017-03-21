def solution(A, B, M, X, Y):
    # write your code in Python 2.7
    ALen = len(A)
    ride = []
    stops = 0
    weight = 0
    counter = 0
    for i in range(0, ALen):
        if (weight <= int(Y) and weight + int(A[i+1]) > int(Y) and counter <= int(X) and counter + 1 > int(X)) or i == ALen:
            # winda jedzie
            newList = []
            for element in ride:
                if element not in newList:
                    newList.append(element)
            print(newList)
            stops += len(newList) + 1
            weight = 0
            counter = 0
            ride = []
        else:
            weight += A[i]
            counter += 1
            ride.append(B[i])
    return stops

print(solution([40, 40, 100, 80, 20], [3,3,2,2,3], 3, 5, 200))