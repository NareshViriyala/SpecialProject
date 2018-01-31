'''
marks = 45
if(marks>80):
    print('First Class')
elif(marks>60) and (marks <= 80):
    print('Second Class')
else:
    print('Third Class')
'''

'''
num = int(input('Enter value for n = '))
if(num <= 0):
    print('Enter valid value')
else:
    sum=0
    while(num>0):
        sum+=num
        num-=1

print(sum)
'''

for quant in range(99,0,-1):
    print(quant)
    if(quant == 65):
        break
