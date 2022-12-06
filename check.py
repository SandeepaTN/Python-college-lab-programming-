import re
def check(s):
    x=re.search('\d{3}-\d{3}-\d{4}',s)
    if x == None:
        print('false')
    else:
      print('true')    
s='41-555-6546' 
check(s)
s='413-555-6546' 
check(s)
