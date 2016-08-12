#!/usr/bin/env python3

# Index
#   1. Strings can be created with single or double quotes.
#   2. Can introduce new line into a string.
#   3. Display escape characters (literally). Use "r" per example below.
#        - r == "raw string" which is primarily used in regular expressions.
#   4. Format or replace character in string (Python 3 @ 2 way)
#   5. Define a multi-line string using triple single/double quotes
#   6. 

def main():
  n = 42
  
  # 1. Single or Double quotes
  s = 'This is a string using single quotes!'
  print(s)
  s1b = "This is also a string using double quotes!"
  print(s1b)
  print()
  
  # 2. New line in string
  s2 = "This is a string\nwhich introduces a new line!"
  print(s2)
  print()
  
  # 3. Show escape characters (literally)
  s3 = r"This is a string that literally displays an escape character \n."
  print(s3)
  print()
  
  # 4. Format or replace character in string (Python 3 @ 2 way)
  s4 = "Inserting variable value in this string ... {} ... Python3 uses curly braces and the string's format method".format(n)
  print(s4)
  s4b = "Inserting varaible value in this string ... %s ... Python2 uses percents." % n
  print(s4b)
  print()
  
  # 5. Define a multi-line string using triple single/double quotes
  print('This example will display a multi-line (3 lines) example:')
  s5 = '''\
First line
Second line
Third line
'''
  print(s5)
  print()


if(__name__ == "__main__"):
  main();