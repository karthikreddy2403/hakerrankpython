
import os

def helper(num):
    return sum(int(digit) for digit in str(num))

def superDigit(n, k):
    initial_sum = helper(n)
    current = initial_sum * k
    while current >= 10:
        current = helper(current)
    
    return current

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()
    n = first_multiple_input[0]
    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    fptr.write(str(result) + '\n')
    fptr.close()
