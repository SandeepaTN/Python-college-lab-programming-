a = {}
while True:
    x = int(input('1-check and add 2-exit'))
    if(x == 1 ):
        name = input('enter friend name ')
        if name in a:
                print('birth day-'+str(a[name]))
        else :
                 day=  input("enter friend's birthady ")
                 a.update({name :day})
    else:
         break
         
