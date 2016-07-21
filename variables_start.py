#!/usr/bin/env python3
# File: /home/cgarndt/Python/Lyndadotcom-upandrunningwithpython/variable_start.py

# declare a variable and initialize it
f = 0;
print(f);

# re-declaring variable
f = "abc";
print(f);

# Error: different types cannot be combined
# Python is "strongly typed" language.
# print("string type " + 123);
# FIX is to convert number to string type
print('string type ' + str(123));

# Global vs. local variables in fuctions
def someFunction():
  # By default, variables declared in functions have a scope just within the declared function.
  f = "variable scope in function";
  print(f);
  global f;
  f = "variable scope is now global."
  print(f);

  
someFunction();
print(f);


# del statement deletes the definition of a variable that was previously declared.
del f; # You can undefine variables using the del statement.
print(f); # NameError: name 'f' is not defined.

