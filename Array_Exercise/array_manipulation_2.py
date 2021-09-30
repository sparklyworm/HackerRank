# using dictionary makes things wayyyy faster!

def arrayManipulation(n, queries):
    mydict = {}
    for query in queries:
        number = query[2]
        start = query[0]
        stop = query[1]

        mydict[start] = mydict.get(start, 0) + number
        mydict[stop+1] = mydict.get(stop+1, 0) - number

    sum, largest = 0, 0
    for key in sorted(mydict):
        sum += mydict[key]
        if sum>largest:
            largest = sum
        
    return largest