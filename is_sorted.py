def is_sorted(t):
    f= True
    l=len(t)
    for i in range(l-1):
        if (t[i] > t[(i+1)]):
            f= False
            break
    return f 
    
t=[1,7,8,9]
print(is_sorted(t))
t=[1,6,3]
print(is_sorted(t))
