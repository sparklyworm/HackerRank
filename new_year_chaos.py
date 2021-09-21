# answer from editorial 

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # optimised linear approach   
   # similar to array inversion concept
   def my_range(start, stop, f):
    x = start
    while x < stop if stop > start else x > stop:
        yield x
        x = f(x)
   n = len(q)
   counter = 0
   chaos = False
   index_list = list(my_range( n-1, 0, lambda x: x-1))
   for index in index_list:
       # loop starts from last item and its corresponding index
       
       origin = index + 1
       item = q[index]
       
       if  item != origin:
           if index-1 >= 0 and q[index-1] == origin:
               # swap places
                q[index-1] = q[index]
                q[index] = origin
                counter += 1

           elif index-2 >= 0 and q[index-2] == origin:
               # move what was originally at index-2 to index 
               # while shifting the other items forward
               # ( not a swap between q[index-2] and q[index])
               q[index - 2] = q[index -1]
               q[index-1] = q[index]
               q[index] =  origin
               counter += 2
    
           else:
                print("Too chaotic")
                chaos = True
                break
            
   if not chaos: 
        print(counter)
    
    

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
