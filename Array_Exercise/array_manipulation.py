def arrayManipulation(n, queries):

    zeros = [0] * n
    for query in queries:
        number = query[2]
        start = query[0]
        stop = query[1]

        zeros[start] += number
        zeros[stop+1] -= number

    prefix_sum = []
    prefix_count = 0
    for item in zeros:
        prefix_count += item
        prefix_sum.append(prefix_count)
    
    return max(prefix_sum)
