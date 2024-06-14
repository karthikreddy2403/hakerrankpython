'''Given an array of integers, where all elements but one occur twice, find the unique element.'''


n=int(input())
a=list(map(int,input().split()))
count=[]
for i in a:
    key=0
    for j in a:
        if i==j:
            key+=1
    count.append(key)
count1=[]
for i in range (n):
    if count[i]<2:
        count1.append(i)
for i in range(0,len(count1)) :
    print(a[count1[i]])
    
    
    
'''You will be given a list of 32 bit unsigned integers. Flip all the bits (1 to 0 and 0 to 1) and return the result as an unsigned integer.'''    


n=int(input())
num=[]
for i in range(n):
    num.append(int(input()))
# 10------1010
binary=[]
for i in num:
    binary1=''
    while i>=1:
        reminder=i%2
        binary1=str(reminder)+binary1
        i=i//2
    binary.append(binary1)
flip=[]
for i in binary:
    length=len(i)
    length_zeros=32-length
    if length<32:
        for j in range(0,length_zeros):
            i="0"+i
    flip.append(i)
final_bin=[]
for i in flip:
    string=''
    for j in i:
        if j=='1':
            string=string+'0'
        else:
            string=string+'1'
    final_bin.append(string)
result=[]
for i in final_bin:
    result1=0
    power=31
    for j in i:
        j=int(j)
        result1=j*(2**(power))+result1
        power =power-1
    result.append(result1)
for i in result:
    print(i)
        
        
        

            
            
            

            
        
        

        
        
        

            
            
            

            
        
        
        

    
    

        
    