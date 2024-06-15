'''Given a square matrix, calculate the absolute difference between the sums of its diagonals.'''



n=int(input())
matrix=[]

for i in range (n):
    lis=list(map(int,input().split()))
    matrix.append(lis)
def absolute_diff(n):
    diagonal_1=0
    diagonal_2=0
    for i in range(n):
        for j in range(n):
            if i==j:
                val=matrix[i][j]
                diagonal_1=diagonal_1+val
    key=n-1
    for i in range (0,n):
        for j in range(0,n):
            if key==j:
                val=matrix[i][j]
                diagonal_2=diagonal_2+val
        key=key-1
    result=diagonal_2-diagonal_1
    if result<=0:
        result=-result
    else:
        result=result
    print(result)
absolute_diff(n)



'''Quicksort usually has a running time n*log(n) of , but is there an algorithm that can sort even faster? In general, this is not possible. Most sorting algorithms are comparison sorts, i.e. they sort a list just by comparing the elements to one another. A comparison sort algorithm cannot beat n*log(n) (worst-case) running time, since n*log(n)  represents the minimum number of comparisons needed to know where to place each element.'''


n=int(input())
arr=list(map(int,input().split()))
final_arr=[]
for i in range(100):
    final_arr.append(0)
for i in arr:
    final_arr[i]+=1
for i in final_arr:
    print(i,end=' ')

        
            
            
                
    
        
    
    