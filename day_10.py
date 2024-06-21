'''finding minimum required page turns to open certain page either
from back side or from front side'''


def min_page_turns(n, p):
    return min(p // 2, (n // 2) - (p // 2))

n = int(input())
p = int(input())
print(min_page_turns(n, p)) 