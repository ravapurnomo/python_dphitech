import math

a = math.sqrt(16)
print(int(a))

b = math.pow(2,5)
print(int(b))

c = dir(math)
print(c)

x = 6.354

d = math.ceil(x)
e = math.floor(x)
print(d)
print(e)

f = math.pi
print(f)

g = math.log10(100)
print(g)

h = math.log10(1000)
print(h)

i = math.floor(2.3)
print(i)

import calendar
cal = calendar.month(2016,1)
print(cal)

cal2 = calendar.isleap(2016)
print(cal2)

caldir = dir(calendar)
print(caldir)

def say(message, times = 1):
    print(message * times)
say('Hello')
say('World', 5)

def func(x = 1, y = 2):
    x = x + y
    y += 1
    print(x,y)
func(x = 1, y = 2)

