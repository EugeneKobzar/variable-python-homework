import math

a = float(input('Inpute side a: '))
b = float(input('Inpute side b: '))
c = float(input('Inpute side c: '))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print('Your triangle square is:', s)