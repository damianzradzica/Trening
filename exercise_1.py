# pkt a.
def square(num):
    return num**2

print(square(5))

# pkt b.
def multiply(subject, times):
    return subject*times

print(multiply(7, 2))

# pkt c.
def power(base, optional=2):
    return base ** optional

print(power(4))
print(power(4, 4))

# pkt d.
def convert_to_usd(pln):
    return pln/3.85

print(convert_to_usd(40))

# pkt e.
def calculate_net(gross, vat):
    net = gross/(1+vat)
    return net

print(calculate_net(1.23, 0.23))
