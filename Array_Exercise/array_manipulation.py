def arrayManipulation(n, queries):
    
    zeros = [0] * n
    track = {}
    for query in queries:
        number = query[2]
        start = query[0]
        stop = query[1]
        
        # for i in range(start, stop):
        #     zeros[i] += number  
    
        if queries.index(query) == 0:
            track[start, stop] = number
            continue
        changed = False
        to_add = {}
        to_del = []
        for key in track:
            print("key0", key[0])
            print("start", start)
            if start < key[0]:
                if stop < key[0]: # out of range
                    to_add[start, stop] = number
                    changed = True
                elif stop <= key[1]: # right overlap
                    to_add[key[0], stop] = track[key] + number
                    to_add[start, key[0]-1] = number # left
                    to_add[stop + 1, key[1]] = track[key] # right
                    to_del.append(key)
                    changed = True
                elif stop > key[1]: # is super set 
                    track[key] += number
                    to_add[start, key[0]-1] = number # left
                    to_add[key[1]+1, stop] = number # right
                    to_del.append(key)
                    
            elif start >= key[0] and start <= key[1]: # left overlap
                if stop <= key[1]: # is subset
                    to_add[start,stop] = track[key] + number
                    to_add[key[0], start -1] = track[key] # left
                    to_add[stop+1, key[1]] = track[key] # right
                    to_del.append[key]
                elif stop > key[1]:
                    to_add[start, key[1]] = track[key] + number
                    to_add[key[1] + 1, stop] = number # right
                    to_add[key[0], start-1] = track[key] # left


        if not changed:
            track[start, stop] = number
            
        for key, value in to_add.items():
            track[key] = value
        for item in to_del:
            track.pop(item)
    #print(track)    
    return max(track.values())
        
        # ways to overlap
        # 1. a full subset
        # 2. start is in range, stop is out
        # 3. start is out, stop is in range
        # 4. is a full super set
        # if start < previous_start
        #   stop < previous_start : no overlap at all ->insert new [start, stop]
        #   stop > previous start : overlap -> insert new [previous_start, previous_stop or stop]; remove [previous_start, previous_stop]
        # if start > previous_stop: no overlap at all -> insert new
       
    