#!/usr/bin/env python3

# Below examples duplicates Python's range method except that the below
#   custom method is "inclusive" or it returns 25 vs range would return max of 24.

# Index
#   1. YIELD statement
#      a. is similar to a RETURN statement in that it returns a value to caller.
#      b. different from the RETURN statement in that code continues AFTER the YIELD
#           statement.
#      c. So, code flow executes the YIELD which returns an object/value and then continues
#           to the next line under the YIELD statement.
#   2. 
#

def main():
  print("this is the generator.py file.")
  for i in inclusive_range(25): # (25) or (5, 25) or (5, 25, 3)
    print(i, end = '')

def inclusive_range(*args):
  # *args represents a tuple.
  
  # IF numargs < 1 ... requires at least one argument to be sent.
  # ELIF statements is assigning values to stop, start, step.
  if numargs < 1: raise TypeError('requires at least one argument')
  elif numargs == 1:
    stop = args[0]
    start = 0
    step = 1
  elif numargs == 2:
    (start, stop) = args
    step = 1
  elif numargs == 3:
    (start, stop, step) = args
  else: raise TypeError('inclusive_range expected at most 3 arguments, got {}'.format(numargs))
  
  # iterator
  i = start
  while i <= stop:
    yield i
    i += step


if __name__ == '__main__': main()
