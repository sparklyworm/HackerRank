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

    # for each query [a, b, k]
    # add k to the item at the a index, and add -k to item at b index
    # taking the prefix sum (sum from start till ith index)
    # will give the number that is at the ith index after adding all queries
