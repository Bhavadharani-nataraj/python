def isstring(a):
    if len(a)>=2 and a[0:2]=='is':
        return(a)
    else:
        return('is'+a)
print(isstring('island'))
print(isstring('a'))
