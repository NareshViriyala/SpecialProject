names = ['Naresh', 'Bharat', 2.0, 1, '23rd']
print(names)

#concatenation
names = names + ['new item']
print(names)

#repitition
print(names * 2)

#slicing
print(names[2:4])

#indexing
print(names[3])

#append
names.append('append')
print(names)

#extend
names.extend(['extend1','extend2'])
print(names)

#insert
names.insert(1,'add at index 1')
print(names)

#pop
print(names.pop())
print(names)