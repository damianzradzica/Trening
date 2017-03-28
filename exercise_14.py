def solution(A):
    # write your code in Python 2.7
    first = A[0]
    last = A[-1]
    complete = [i for i in range(first, last+1)]
    for i in complete:
        if i in A:
            pass
        else:
            return i

print(solution([1,2,4]))
