import pwd




try:
  pwd.getpwnam('fack')
except KeyError:
  print('User someusr does not exist')
  
 