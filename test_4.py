example = [3, 8, 9, 7, 6]
number = 3

def solution(array, rotation):
    return array[-rotation:] + array[:-rotation]

print(solution(example, number))