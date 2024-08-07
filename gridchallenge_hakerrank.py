def gridChallenge(grid):
    sorted_grid = [sorted(row) for row in grid]
    num_rows = len(sorted_grid)
    num_cols = len(sorted_grid[0])

    for col in range(num_cols):
        last_char = ""
        for row in range(num_rows):
            current_char = sorted_grid[row][col]
            if current_char < last_char:
                return "NO"
            last_char = current_char

    return "YES"

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0].strip())
    index = 1

    results = []
    for _ in range(t):
        n = int(data[index].strip())
        grid = [data[index + i + 1] for i in range(n)]
        index += n + 1
        
        results.append(gridChallenge(grid))

    sys.stdout.write("\n".join(results) + "\n")
