def nested_sum(t) :
    res=0
    for i in t:
       res=res+sum(i)
    return res   
t = [[1,2],[3],[4,5,6]]
print(nested_sum(t))
