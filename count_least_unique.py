def count_least_unique(l = [] , k = 0):
    sl = []
    o = []
    for i in set(l):
        o.append((i,l.count(i)))
    o = sorted(o , key = lambda x : x[1] , reverse = True)
    for k,v in o:
        sl.extend([k]*v)
    print(sl)
    print(o)
    return len(set(sl[:-k]))

l = [1, 21,21,3,4,2,1,2,2]
print(count_least_unique(l,4))

