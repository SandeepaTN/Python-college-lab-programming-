a=int(input('Enter a number '))
b=int(input('Enter a number '))
c=int(input('Enter a number '))
if (a>b):
    if(a>c):
       print(str(a)+' largest')
    else:
      print(str(c)+' is largest')
else:
   if(b>c):
       print(str(b)+' is  largest')
   else:
       print(str(c)+' is  largest')

