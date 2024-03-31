def find(q:list):
    b=0
    c=q.copy()
    for i in q:
        if c.count(i)>1:
            c.remove(i)
            b+=1
            print(i)
    q.sort()
    for i in range(1,b+1):
        c.append('_')
        return c
print(find([4,1,5,1,8,5,4]))               
