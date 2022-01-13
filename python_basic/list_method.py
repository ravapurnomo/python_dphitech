print('>>> .append() method')
orders = ['daisies','periwinkle']
print(orders)

orders.append('tulips')
print(orders)

print('>>> .count() method')
backpack = ['pencil', 'pen', 'notebook', 'textbook', 'pen',
            'highlighter', 'pen']
print('berikut list isi dalam tas: ',backpack)
numPen = backpack.count('pen')
print('jumlah pulpen dalam tas ada: ',numPen)

print('>>> .len() function')
print('jumlah objek dalam backpack ada : ',len(backpack))

print('>>> .sort() method')
exampleList = [4,2,1,3]
exampleList.sort()
print(exampleList)