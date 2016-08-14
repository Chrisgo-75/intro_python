#!/usr/bin/env python3

# Index
#   1. Define variable and create an integer type
#      - example also shows how to print out the "type" or object class.
#      - Python shell in comparing variable (object) ids
#         >>> x is y
#         #=> True
#      - Python shell in comparing variable values
#         >>> x === y
#         #=> True
#   2. Tuple ... created with parens.
#      - When printing, Python will try to print it in a way that Python
#        could actually create one if it needed to.
#      - Are "immutable" object. So can't insert, append, delete ... once
#        created, it is. Can't change it.
#   3. List ... created with square brackets "[ ]".
#      - Is a "mutable" object. Can append, insert, etc.
#      - Append example
#      - Insert example
#   
#

def main():
  # 1. Defines variable and creates an integer type
  a = 1
  print(type(a), a)
  # => class 'int'> 1
  # Every variable is an "Object".
  
  b = 'one'
  print(type(b), b)
  # => <class 'str'> one
  
  # Assign multiple objects at the same time
  c, d = 0, 1
  print('Assign multiple objects at the same time "c, d = 0, 1"')
  print(c, d)
  # => 0 1
  print()
  
  # 2. Tuple
  e = (1, 3, 5, 7, 9)
  print('Tuple:')
  print(e)
  print(type(e), e)
  # => (1, 3, 5, 7, 9)
  print()
  
  # 3. List
  e2 = [1, 3, 5, 7, 9]
  print('List:')
  print(e2)
  print(type(e2), e2)
  # => [1, 3, 5, 7, 9]
  print('... appending "5" to List:')
  e2.append(5)
  print(type(e2), e2)
  # => <class 'list'> [1, 3, 5, 7, 9, 5]
  print('... insert "7" at the beginning using index 0:')
  e2.insert(0, 7)
  print(type(e2), e2)
  # => <class 'list'> [7, 1, 3, 5, 7, 9, 5]
  
  



if __name__ == '__main__': main()