num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Negative numbers do not have factorial")
elif num==0:
    print("The factorial for 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial for",num,"is",factorial)