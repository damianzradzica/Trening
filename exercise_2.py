# Zadanie 2

def football_win(a_home, b_away, a_away, b_home):
    if a_home + a_away > b_home + b_away:
        return '1'
    elif a_home + a_away < b_home + b_away:
        return '2'
    elif a_home + a_away == b_home + b_away:
        if a_away > b_away:
            return '1'
        elif a_away < b_away:
            return '2'
        else:
            return 'x'

print(football_win(2, 0, 0, 2))
print(football_win(2, 1, 2, 3))
print(football_win(0, 1, 0, 1))