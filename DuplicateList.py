numbers=[1,2,5,5,6,7,7,8,1]
uniques=[]

for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)