# /usr/bin/python
try:
  num_array = []	
  num = raw_input("Enter how many elements you want ?\n")
  for i in range(int(num)):
    num_array.append(int(raw_input("Enter number \n")))
  for i in reversed(num_array):
    print i 
except: 
  print "Please enter number"

