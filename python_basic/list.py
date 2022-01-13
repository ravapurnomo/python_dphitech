item1="bread"
item2="pasta"
item3="fruits"
items=["bread", "pasta", "fruits", "veggies"]

print(items[0])

items[0]='chips'
print(items)
print(items[0])
print(items[0:2])
print(items[-1])

items=["bread", "pasta", "fruits", "veggies"]

print(items)

items.append("butter")

print(items)

items=["bread", "pasta", "fruits", "veggies"]
items.insert(1,'butter')

print(items)

food=["bread", "pasta", "fruits"]
bathroom=["shampoo", "soap"]
itemss=food+bathroom
print(itemss)

panjang=len(itemss)
print(panjang)

cek="bread" in itemss
cek1="caos" in itemss
print(cek)
print(cek1)
