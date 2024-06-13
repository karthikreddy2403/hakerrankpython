'''Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.'''


s=input()
key=s[-2]
time=s[0:8]
time=time.split(":")
if key=='A'and time[0]=='12':
    time[0]='00'
    militry_time=":".join(time)
    print(militry_time)
elif key=="p" and time[0] =="12":
    militry_time=":".join(time)
    print(militry_time)
elif key =="P" and time[0] !="12":
    conv_hour=int(time[0])
    conv_hour+=12
    conv_hour=str(conv_hour)
    time[0]=conv_hour
    militry_time=":".join(time)
    print(militry_time)

else:
    militry_time=":".join(time)
    print(militry_time)


'''There is a collection of input strings and a collection of query strings. For each query string, determine how many times it occurs in the list of input strings. Return an array of the results.'''


n=int(input())
strings=[]
for i in range (0,n):
    strings.append(input())
q=int(input())
queries=[]
for i in range (0,q):
    queries.append(input())

for i in queries:
    key=0
    for j in strings:
        if i==j:
            key+=1
    print(key)


    
    

