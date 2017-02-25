# Zad. 4
dict = {
    'name': 'Elijah Wood',
    'role': 'Frodo',
    'movie': 'LOTR'
}

def message(ctx):
    if ctx['name'] and ctx['role'] and ctx['movie']:
        return 'In {}, {} is a {}'.format(ctx['movie'], ctx['name'], ctx['role'])
    else:
        return None

print(message(dict))