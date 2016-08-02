#!/usr/bin/env python3
# File: /home/cgarndt/Python/Lyndadotcom-upandrunningwithpython/conditionals.py

# Index
#   1. IF ELIF ELSE statement 
#   2. Rewrite of #1 as a conditional statement all in one line.
#   3. Using curly braces which will be replaced by the values in the format.
#   4. Conditional - Short IF statement


def main():
  x, y = 100, 100
  
# 1. Option A: IF ELIF ELSE statement
#   if(x < y):
#     st = 'x is less than y';
#   elif(x == y):
#     st = 'x is same as y';
#   else:
#     st = 'x is greater than y';
#   print(st);

# 2. Otion B ... rewrite Option A as a "conditional statement".
  # Python has a conditional called a "conditional statement"
  #   - which lets you write in one line the following: "a if c else b"
#   st = "x is less than y" if(x < y) else "x is greater than or equal to y";
#   print(st);

# 3. Using curly braces which will be replaced by the values in the format.
  a, b = 5, 1
  if a < b:
    print('a ({}) is less than b ({})'.format(a, b));
  else:
    print('a ({}) is not less than b ({})'.format(a, b));
  
# 4. Conditional - Short IF statement
  print('foo' if a < b else 'bar');

if(__name__ == "__main__"):
  main();



