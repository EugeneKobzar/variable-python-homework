import math

a = float(input('inpute side a: '))
b = float(input('inpute side b: '))
c = float(input('inpute side c: '))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print(s)