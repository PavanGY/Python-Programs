num=int(input("Enter a number: "))
factorial=1
if num<0:
    print("Sorry negative numbers don't have factorial")
elif num==0:
    print("The factorial for the Zero is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)