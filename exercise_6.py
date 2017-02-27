def safe_get(list, index):
    try:
        return list[index]
    except IndexError:
        return None

print(safe_get([1, 2, 3, 4, 5], 2))
print(safe_get([1, 2, 3, 4, 5], 7))

