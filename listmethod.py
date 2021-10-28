num=[5,2,1,5,7,4,5]
num.append(20)
print(num)

num.insert(0,10)
print(num)

num.remove(5)
print(num)

#num.clear()

num.pop()
print(num)

print(num.index(7))

print(50 in num)

print(num.count(5))

num.sort()
print(num)

num.reverse()
print(num)

num2=num.copy()
print(num)
print(num2)

#remove duplicate in num

unique=[]
for i in num:
    if i not in unique:
        unique.append(i)

print(unique)

