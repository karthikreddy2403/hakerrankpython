'''There is a large pile of socks that must be paired by color. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.'''


n = int(input())
arr = list(map(int, input().split()))
arr.sort()  
result = 0
i = 0
while i < n - 1:
    if arr[i] == arr[i + 1]:
        result += 1
        i += 2  
    else:
        i += 1
print(result)
