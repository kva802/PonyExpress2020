import math 

def kv(a):
    b = []
    b.append(a*4)
    b.append(a*a)
    b.append(math.sqrt(2*math.sqr(a)))
    return(b)

a = int(input())

print(kv(a))
