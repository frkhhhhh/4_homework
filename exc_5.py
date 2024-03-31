

def f(text):

    if len(text)==0:
        return f' none liked it'
    
    elif len(text)==1:
        return f'{text[0]} liked it.'
    elif len(text)==2:
        return f'{text[0]} and {text[1]} liked it.'
    elif len(text)==3:
        return f'{text[0]}, {text[1]} and {text[2]} liked it'
    elif len(text)==4:
        return f'{text[0]}, {text[1]} and {len(text)-2}'
a=[]
print(f(a))   


