"""
Given a string, 
find the number of pairs of substrings of the string 
that are anagrams of each other.
"""
"""
use concept of signatures
substrings are anagrams of each other if they have the exact same number of alphabets
signature = [ 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0] 
26 for all the alphabets
eg. the word "cab" has signature [ 1 1 1 0 0 0 ....]
substrings have the same signature if they are anagrams
"""
import string
import math

def sherlockAndAnagrams(s):

    # ALPHABET = string.ascii_lowercase()
    NUM_ALPHA = 26
    a = "a"

    signatures = {}
    n = len(s)

    for start in range(n):
        for finish in range(start,n):
            substring = s[start:finish+1]
            signature = [0] * NUM_ALPHA
            for letter in substring:
                signature[ord(letter) - ord(a)-1] += 1
            signature = tuple(signature)
            signatures[signature] = signatures.get(signature,0) + 1

    num_of_anagrams = 0
    for signature, num in signatures.items():
        """
        how many pairs (2) are there?
        combination: n!/(n-2)! * 1/2!    
        """
        if num > 2:
            num_of_anagrams += math.factorial(num)/math.factorial(num-2) * 1/2
        elif num == 2:
            num_of_anagrams += 1
        
    
    return int(num_of_anagrams)

