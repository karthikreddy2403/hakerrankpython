'''Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.'''



arr=list(map(int,input().split()))

for i in range (0,len(arr)):
    for j in range (i+1,len(arr)):
        if arr[i]>arr[j]:
            arr[i],arr[j]=arr[j],arr[i]
minimum_sum=0
maximum_sum=0
for i in range(0,len(arr)-1):
    minimum_sum+=arr[i]
for i in range (1,len(arr)):
    maximum_sum+=arr[i]
print(minimum_sum,end=' ')
print(maximum_sum)