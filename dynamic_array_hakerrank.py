def dynamicArray(n, queries):
   
    arr = [[] for _ in range(n)]
    lastAnswer = 0
    answers = []


    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]
        
        
        index = (x ^ lastAnswer) % n
        
        if query_type == 1:
           
            arr[index].append(y)
        elif query_type == 2:
            lastAnswer = arr[index][y % len(arr[index])]
            answers.append(lastAnswer)
    
    return answers
if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    q = int(data[1])
    queries = []
    index = 2
    for _ in range(q):
        queries.append([int(data[index]), int(data[index+1]), int(data[index+2])])
        index += 3
    
    result = dynamicArray(n, queries)
    
 
    for res in result:
        print(res)
