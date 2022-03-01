arr=[10,20,30,40]

max=arr[0]
n=len(arr)

for i in range(1,n):
    if arr[i]>max:
        max=arr[i]

print(max)

min=arr[0]
for i in range(1,n):
    if arr[i]<min:
        max=arr[i]

print(min)