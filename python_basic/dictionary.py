# d = {"George":24, "Tom": 32}
d = {}
d["George"] = 24
d["Tom"] = 32
d["Jenny"] = 16

print(d["George"])
print(d["Tom"])
print(d["Jenny"])

d["Jenny"] = 20
print(d["Jenny"])

# Keys are commonly Strings or Numbers
d[10] = 100
print(d[10])
print("")

x = len(d)
print(x)

print(list(d.keys()))
# How to iterate over key-value pairs?
for key, value in d.items():
    print("key:")
    print(key)
    print("value:")
    print(value)
    print("")

j = [3,4,6,1,2]
j[1:2] = [7,8]
print(j) #CARITAU