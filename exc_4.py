a=[0,1,3]
new_list=[]
b=0

for i in range(max(a)+1):
    new_list.append(b)
    b=b+1
stop= True
while stop:
    for i in new_list:
        if i in a:
            pass
        else:
            print(f'Missed number: {2}')
            stop= False