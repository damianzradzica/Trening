# Zad. 3a
def multiplication_table(n):
    for i in range (1, 11):
        result = i * n
        print(str(i) + ' * ' + str(n) + ' = ' + str(result))


multiplication_table(4)

# Zad. 3b
def even_odd(n):
    for i in range(0, n+1):
        if i % 2 == 0:
            print(str(i) + ' - parzysta')
        else:
            print(str(i) + ' - nieparzysta')

even_odd(7)

# Zad. 3c
def tree(n):
    for i in range(0, n+1):
        print(i*'*')

tree(9)