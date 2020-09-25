def kv(a):
    seta = set(a)
    if len(a) == len(seta):
        return('no')
    else:
        return ('yes')

a = [1, 2, 2, 3]



print(kv(a))
