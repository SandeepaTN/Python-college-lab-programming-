def has_duplicate(t):
    f=False
    l=len(t)
    for i in range(l):
        for j in range((i+1),l):
          if (t[i] == t[j]):
            f= True
            break
    return f 
    
t=[1,7,9,7]
print(has_duplicate(t))
t=[1,7,8,9]
print(has_duplicate(t))
