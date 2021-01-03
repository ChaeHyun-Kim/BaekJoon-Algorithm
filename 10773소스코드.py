k = int(input())
stack =[]
i=-1
for _ in range(k):
    a =int(input())
    if a==0:
        del stack[i:]
        i-=1#인덱스값 -1
    else:
        stack.append(a)
        i+=1
print(sum(stack))    
