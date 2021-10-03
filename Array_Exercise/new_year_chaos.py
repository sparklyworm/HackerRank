# given array 
# determine the number of bribes the numbers have to make to get to their current position 
# a larger number has to bribe the number in front of it to swap places with it
# print "too chaotic" if any number bribed more than 2 times

# answer from editorial 

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

   # loop starts from last item and its corresponding index
   for index in index_list:

       original = index + 1
       item = q[index]
       
       if  item != original:
           if index-1 >= 0 and q[index-1] == original:
               # swap places
                q[index-1] = q[index]
                q[index] = original
                counter += 1

           elif index-2 >= 0 and q[index-2] == original:
               # move what was originally at index-2 to index 
               # while shifting the other items forward
               # ( not a swap between q[index-2] and q[index])
               q[index - 2] = q[index -1]
               q[index-1] = q[index]
               q[index] =  original
               counter += 2
    
           else:
                print("Too chaotic")
                chaos = True
                break
            
   if not chaos: 
        print(counter)
    