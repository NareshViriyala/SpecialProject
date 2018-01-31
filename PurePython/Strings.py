'''
singlelinestring = "This is a single line string"
multilinestring = """This is a multi line string
                    which can span to multiple lines"""

print(singlelinestring)
print(multilinestring)
'''

string1 = "Naresh"
string2 = "Kumar"

#concatenate
print(string1+' '+string2)

#repetition
print((string1+' ') * 20)

#Slicing

#print from 2 to 4
print(string1[2:4])

#print from 3
print(string1[2])

#print from -2
print(string1[:-2])

#find()
print(string1.find('ar'))

#replace
print(string1.replace('ar','AR'))

#split()
str = 'n,a,r,e,s,h'
arr = str.split(',')
print(arr)


#count()
print(string1.count('a', 0, -1))

'''more function
upper()
lower()
max()
min()
isalpha()
'''
