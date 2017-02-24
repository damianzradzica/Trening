def multiplication_table(n):
    for i in range (1, 11):
        result = i * n
        print(str(i) + ' * ' + str(n) + ' = ' + str(result))


multiplication_table(4)