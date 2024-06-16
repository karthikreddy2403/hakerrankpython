'''A pangram is a string that contains every letter of the alphabet. Given a sentence determine whether it is a pangram in the English alphabet. Ignore case. Return either pangram or not pangram as appropriate.'''


string=input()
string_lower=''
for i in string:
    asc=ord(i)
    if asc>64 and asc<91:
        string_lower=string_lower+chr(asc+32)
    else:
        string_lower=string_lower+i
alpha='abcdefghijklmnopqrstuvwxyz'
for i in string_lower:
    for j in alpha:
        if i==j:
            alpha=alpha.replace(i,'')
result=len(alpha)
if result==0:
    print('pangram')
else:
    print('not pangram')




'''There are two n-element arrays of integers, A and B . Permute them into some A' and B' such that the relation A'[i]+B'[i]>=K holds for all i where 0<=i<n.

There will be  queries consisting of ,A , and B. For each query, return YES if some permutation ,  satisfying the relation exists. Otherwise, return NO.'''


q=int(input())
for i in range (q):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    a.sort()
    b.sort(reverse=True)
    count=0
    for i in range(n):
        if(a[i]+b[i]>=k):
            count+=1
    if(count==n):
        print('YES')
    else:
        print("NO")
        
