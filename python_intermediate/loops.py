a = ["banana", "apple", "microsoft"]
print(a[0])
print(a[1])
print(a[2])

for element in a:
    print(element)
    print(element)

b = [20, 10, 5]
total = 0
for e in b:
    total = total + e
print(total)

c = list(range(1, 5))
print(c)

x = 0
for i in range(1, 5):
    x += i
print(x)

print(list(range(1,8)))

total3 = 0
for i in range (1, 8):
    if i % 3 == 0:
        total3 += i
print(total3)

# Menghitung kelipatan 3 dan 5, dibawah 100
print(list(range(1, 100)))

total4 = 0
for y in range (1, 100):
    if y % 3 == 0:
        total4 += y
    elif y % 5 == 0:
        total4 += y
print("total dari angka kelipatan 3 dan 5 yang berada dibawah ankga 100 adalah", total4)

z = list(range(1,100))
total5 = 0
for h in z:
    if h % 3 == 0 or h % 5 == 0:
        total5 += h
print("total5", total5)

for i in "apple":
    print(i)

for c in "family":
    print(c.capitalize())

fam_heights = [1.73, 1.80, 1.65, 1.10]
for height in fam_heights:
    print(height)
for i in enumerate(fam_heights):
    print(("index :" + str(i)))
    # SALAH -> print("index :" + str(i) + ":" + str(height))

example = ['left', 'right', 'up', 'down']

"""for i in range(len(example)):
    print(i, example[i])"""

for i, j in enumerate(example):
    print(i, j)

new_dict = dict(enumerate(example))

print(new_dict)

[print(i, j) for i, j in enumerate(new_dict)]








