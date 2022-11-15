import random
tools=['stone','paper','scisor']
d=0
w=0
l=0
def play():
   global w
   global l
   global d 
   c_ch=str(random.choice(tools))
   print('1-stone  2-paper 3-scisor')
   p_ch=int(input('Enter your tool '))
   if (c_ch  == "stone"):
      if p_ch ==3 :
          print('loose')
          l=l+1
      elif p_ch ==2:
          print('win')
          w=w+1
      else:
          print('draw')
          d=d+1
   elif c_ch =='paper':
      if p_ch ==3:
          print('loose')
          l=l+1
      elif p_ch ==1:
          print('win')
          w=w+1
      else:
          print('draw')
          d=d+1
   else:
      if p_ch ==1:
          print('loose')
          l=l+1
      elif p_ch ==2:
          print('win')
          w=W+1
      else:
          print('draw')
          d=d+1          
          
while True:
   print('1-play 2-exit ')
   a=int(input('Enter your choice '))
   if(a==1):
       play()
   else:
       print('your wins:'+str(w))
       print('computer wins:'+str(l))
       print('your winning percentage is '+str(w*100/(w+d+l))+'%')
       break
   
