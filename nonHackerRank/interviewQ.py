# 3[2[a][b]]
# 3[2[a]2[[d][f]]]
# 3[[a]2[[b]2[c]]]
# prints out string given the input in the format above

from collections import deque
stack = deque()
stringstack = deque()
s = "3[[a]2[[b]2[c]]]"


n = len(s)
previous_char = ""


for i in range(n):
    print(s[i])
    if s[i] == "]":
        x = stack.pop()
        if x.isalpha():
            num = stack.pop()
            stringstack.pop()
            stringstack.append(int(num) * x)
            
        else: #x is a number
            stringbuild = ""
            print(stringstack)
            while stringstack[-1] != ".":
                stringbuild = stringstack.pop() + stringbuild
            
            stringstack.pop()
            stringstack.append(int(x)*stringbuild)
            
    
    if s[i] == "[" and not previous_char.isdigit():
        stack.append("1")
        stringstack.append(".")
    if s[i].isdigit() or s[i].isalpha():
        stack.append(s[i])
    if s[i].isdigit():
        stringstack.append(".")
        print("stringstack")
        print(stringstack)
        
    previous_char = s[i]
    
print(stringstack.pop())
