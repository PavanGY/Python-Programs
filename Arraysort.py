# Initializing the array
arr=[]
n=int(input("elements:"))
for i in range(0,n):
    l=int(input(":"))
    arr.append(l)
print(arr)
temp=0
#Printing the array

print("The array is: ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")

#Sorting

for i in range(0,len(arr)):
    for j in range(i+1,len(arr)):
        if(arr[i]>arr[j]):
            temp=arr[i];
            arr[i]=arr[j];
            arr[j]=temp;

print();


print("The sorted array is: ")
for i in range(0,len(arr)):
    print(arr[i],end=" ")
