cars = ['bnw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

list = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']
list.append('!')
print(list)

del list[4]
list.insert(4, 'a')

string = ''.join(list[:5]) + ', ' + ''.join(list[7:])
print(string)

print(list)
list.sort(reverse=True)
print(list)