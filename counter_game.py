import math

def counter_game(n):
    moves = 0

    while n != 1:
        # Get the highest power of 2 less than or equal to n
        highest_power_of_2 = 1 << (n.bit_length() - 1)
        
        if highest_power_of_2 == n:
            n //= 2
        else:
            n -= highest_power_of_2
        
        moves += 1
    
    # Determine the winner based on the number of moves
    if moves % 2 == 0:
        return "Richard"
    else:
        return "Louise"

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        result = counter_game(n)
        print(result)
