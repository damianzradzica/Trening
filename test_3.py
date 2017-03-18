example = [9, 3, 9, 3, 9, 7, 9]

def solution(array):
    result = []
    new = []
    for i in array:
        new.append(i)

    for element in array:
        new.remove(element)
        if int(element) in new:
            new.append(element)
        else:
            result.append(element)
    return result


print(solution(example))