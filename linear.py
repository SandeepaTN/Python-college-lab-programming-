lst=[]
c=0
n=int(input('enter no of elements '))
for i in range(n):
    a=int(input('enter the number '))
    lst.append(a)
print(lst)
x=int(input('enter the nymber to be searched '))
for i in lst:
    if x == i:
        print('element found at position '+str(lst.index(x)+1))
        c=1
if(c == 0):
    print('element not found')

