#!/usr/bin/env python3


def main():
  # Defines variable and creates an integer type
  a = 1
  print(type(a), a)
  # => class 'int'> 1
  # Every variable is an "Object".
  
  b = 'one'
  print(type(b), b)
  # => <class 'str'> one
  
  # Assign multiple objects at the same time
  c, d = 0, 1
  print(c, d)
  # => 0 1
  
  # Tuple
  e = (1, 3, 5, 7, 9)
  print(e)
  # => (1, 3, 5, 7, 9)
  e2 = [1, 3, 5, 7, 9]
  print(e2)
  # => [1, 3, 5, 7, 9]
  
  



if __name__ == '__main__': main()