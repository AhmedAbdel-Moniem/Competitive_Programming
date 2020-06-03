# Filtering list being filled with strings and intetegers
def myfunc(x):
    y=[]
    for z in x:
        if type(z)==int: # filtering integers
            y.append(z)
    print(y)
x = [1,'a',8,'c','rr',53,90,'y']
t = [1,2,'1','123',123]
myfunc(x)


def myfunc(x):
    y=[]
    for z in x:
        if type(z)==str:  # filtering string items
            y.append(z)
    print(y)
x = [1,'a',8,'c','rr',53,90,'y']
t = [1,2,'1','123',123]
myfunc(x)
