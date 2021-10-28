#list of coordinate
for i in range(0,2):
    for j in range(0,4):
        print(f'({i},{j})')

# Question
# XXXX
# XX
# XXXX
# XX
# XX
star=[4,2,4,2,2]
for i in star:
    print("X"*i)


for x_count in star:
    output=""
    for count in range(x_count):
        output +='x'

    print(output)


# print L shap

num=[1,1,1,1,1,6]
for x in num:
    count=''
    for i in range(x):
        count+='X'

    print(count)
