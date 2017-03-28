def solution(A):
    # write your code in Python 2.7
    long = len(A)
    A.sort()
    count = A[0]
    for element in range(1, long):
        if A[element] == count + 1:
            count += 1
            result = 1
        else:
            result = 0
    return result

print(solution([1,4,3,2,6]))