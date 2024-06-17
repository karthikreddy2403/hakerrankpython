'''Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

The length of the segment matches Ron's birth month, and,
The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.'''


n = int(input())
s = list(map(int, input().split()))
d, m = map(int, input().split())
result = 0
if n < m:
    print(result)
else:
    current_sum = sum(s[:m])
    if current_sum == d:
        result += 1
    for i in range(m, n):
        current_sum += s[i] - s[i - m]
        if current_sum == d:
            result += 1

    print(result)
    
    
    
'''XOR operation'''    
    
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]:
            res += '0';
        else:
            res += '1';

    return res

s = input()
t = input()
print(strings_xor(s, t))
        

