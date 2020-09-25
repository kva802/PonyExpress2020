

def kv(a,n):
    b = []
    b.append(a[0])
    b.append(a[n])
    return(b)

a = []
int(input(n))

for i in range(n):
    a.append(int(input()))


print(kv(a,n))
