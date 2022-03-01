num=int(input("Enter the number to check: "))

for i in range(2,num):
    if num%i==0:
        print("Not a prime number")
        break;
    else:
        print("It was a prime number")
