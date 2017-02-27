def safe_get(list, index):
    try:
        return list[index]
    except IndexError:
        return None

# print(safe_get([1, 2, 3, 4, 5], 2))
# print(safe_get([1, 2, 3, 4, 5], 7))

def divide(a, b):
    if isinstance(a, int) and isinstance(b, int) and a >= 0 and b > 0:
        return a / b
    elif b == 0:
        raise ValueError('Wartość parametru b musi być większa od zera')
    else:
        raise TypeError('Argumenty funkcji muszą być liczbami całkowitymi')

# print(divide(4, 2))
# # print(divide(4, 'osiem'))
# print(divide(4, 0))

list_numbers = ['123456789', '987654321']

def phone(number):
    if number in list_numbers:
        print('Numer istnieje')
    else:
        raise Exception('numer nie istnieje')

# phone('123456789')
# phone('f34fgrg3')