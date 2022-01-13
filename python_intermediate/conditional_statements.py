# if else statements

a = 1
b = 2

if a < b:
    print("a is less than b")
    print("a is definitely less than b")
print("Not sure if a is less than b")

c = 5
d = 4
if c < d:
    print("c is less than d")
else:
    print("c is Not less than d")
    print("I don't think c is less than d")
print("outside the if block")

e = 18
f = 8
if e < f:
    print("e is less than f")
elif e == f:
    print("e is equal to f")
elif e > f + 10:
    print("e is greater than f by more than 10")
else:
    print("e is greater than f")

g = 9
h = 8
if g < h:
    print("g is less than h")
else:
    if g == h:
        print("g is equal to h")
    else:
        print("g is greater than h")

name = "YK"
height_m = 2
weight_kg = 110

bmi = weight_kg / (height_m ** 2)
print("bmi:",bmi)

if bmi < 25:
    print(name," is not overweight")
else:
    print(name," is overweight")

# another example

nilaiA = 4
if nilaiA%2 ==0:
    print("nilaiA is even")

nilaiB = 5
if nilaiB%2 == 0:
    print("nilaiB is even")
else:
    print("nilaiB is odd")

nilaiC = 5
if nilaiC%2 == 0:
    print("nilaiC is divisible by 2")
elif nilaiC%3 == 0:
    print("nilaiC is divisible by 3")
else:
    print("nilaiC is neither divisible by 2 nor by 3")

if (1,2):
 print('foo')

x = 0
a = 0
b = -5
if a > 0:
  if b < 0:
    x = x + 5
  elif a > 5:
    x = x + 4
  else:
    x = x + 3
else:
  x = x + 2
print(x)

if 1:
  print("1 is truthy!")
else:
  print("1 is not truthy!")

if 1 + 1 == 2:
  if 2 * 2 == 16:
    print("if")
  else:
    print("else")

spam = 7
if spam > 5:
           print("five is less than 7")
if spam > 8:
             print("eight is less than 7")

def bar( z ):
    i = 1
    while (i <= z):
        i *= 2
    return i
    print(i)
print(bar( 7 ))