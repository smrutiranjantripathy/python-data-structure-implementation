# /usr/bin/python
package = list()
def checkpackage():
  l = len(package)
  if (l == 0):
    return 'no food'
  return 'food present'

def addpackage(cost):
  if(cost > (10**7)):
    print 'The cost is more than threshold'
  elif(cost <1):
    print 'The cost is less than threhold'
  else: 
    package.append(cost)

def removepackage():
  l = len(package)
  print package[l-1]
  package.remove(package[l-1])

queries = int(raw_input())
if(queries > (10**5)):
  print 'exceeded the upper threshold'
elif(queries < 1):
  print 'below minimal threshold'
else:
  for i in range(queries):
    order = raw_input()
    a = order.split("  ")
    try:
      a=map(int,a)
    except:
      print 'Enter Appropriate Amount of Space'
    if( a[0] == 1):
      if(len(a) >= 2):
        print 'xtra entry'
      if('no food'== checkpackage()):
        print 'No Food'      
      else: 
        removepackage();
    elif( a[0] == 2):
      addpackage(a[1]);
    else:
      print 'inavlid entry'
