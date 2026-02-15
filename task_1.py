number = int(input('Enter your five-digit number: '))
a = number//10000
b = number%10000//1000
c = number%1000//100
d = number%100//10
e = number%10
print(a)
print(b)
print(c)
print(d)
print(e)