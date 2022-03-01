num=int(input("Enter a number: "))

s=0
temp=num
while   temp > 0:
    c = temp%10
    s  +=c**3
    temp //= 10
if num==s:
    print("The number is  an Armstrong Number")
else:
    print("The number is not an Armstrong Number")
