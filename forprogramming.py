# triange by for loop

for i in range (1,11):
    print('*'*i)



for item in 'PYthon':
    print(item ,end='')


for i in ['Mosh','john','sarah']:
    print (i)


for i in [1,2,3,4]:
    print(i,end='')


# it take a jump of 2 digits

for i in range(0,21,2):
    print(i,end='')


prices=[10,20,30]
total=0
for i in prices:
    total+=i
print(f"Total : {total}")
