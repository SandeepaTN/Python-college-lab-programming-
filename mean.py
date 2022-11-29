import math
a = input("enter some comma seperated numbers : ")
list1 = (a.split(","))
list1=list(map(int,list1))
mean = sum(list1)/len(list1)
print('mean = ' +str(mean))
sum=0
for i in list1 :
    sum=sum+((i-mean)**2)
variance= sum/(len(list1)-1)
print('variance = ' +str(variance))
sd = math.sqrt(variance)
print('standard deviation = ' +str(sd))


