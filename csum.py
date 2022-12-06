def csum(t):
    a=[]
    l= len(t)
   
    for i in range(l):
       
        a.append(0)
        for j in range((i+1)):
           a[i]=a[i]+t[j]
    return a
    
t=[1,2,3]
print(csum(t))
