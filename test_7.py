def solution(N):
    number = str(N)
    length = len(number)
    zeros = 0
    for i in number:
        if int(i) == 0:
            zeros += 1
    if length == 1:
        result = 1
    elif str(0) in number:
        result = ((length-zeros) ** 2)
    else:
        result = (length ** 2) - length
    return result

print(solution(10063))