#/usr/bin/python
'''
Invert a 2D Array
Enter the dimensions of array
Revert the dimensions of array
'''
try:
  enter_range = raw_input()
  length = len(enter_range.split())
  if (length > 2):
    print "Keep in mind its a 2d array"
  row,column = enter_range.split()
  row = int(row)
  column = int(column)
  b = list()
  for i in range(row):
    col = list()
    number_string = raw_input()
    a = number_string.split(' ',column)
    if (int(column) != len(a)):
      print "You have entered more or less numbers"
      break
    else:
      a = map(int,a)
      b.append(a)
  for i in range(column):
    for j in range(row):
      print b[j][i],
    print "\n"  
except:
  print "Type numbers"

