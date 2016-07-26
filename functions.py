#!/usr/bin/env python3
# File: /home/cgarndt/Python/Lyndadotcom-upandrunningwithpython/functions.py

# Index
#   Define a fuction
#   2. Call and Prints Function
#   3. Functions in Python are Objects, they have a value
#      Function that takes parameters
#   4. Function that takes parameters
#   5. Define a function that returns a value
#   6. Function with default value for parameter
#   7. Function with variable number of arguments

# ---

# define a function
def func1():
  print('I am a function');

# 1. simply calls func1
#func1();

# 2. Call and Prints Function1
#print(func1());
# => None  so above cmd is trying to print the return value but the function doesn't return anything.

# 3. Functions in Python are Objects, they have a value.
#    a. This is how Python treats objects.
#print(func1);
# => <function func1 at 0x7f001cca2bf8>

# -------

# function that takes parameters
def func2(param1, param2):
  print(param1, " ", param2);

# 4. function that takes parameters
func2(10,20);
#print(func2(10,20));

# -------

# 5. define a function that returns a value
def cube(x):
  return(x*x*x);
#print(cube(3));

# 6. function with default value for parameter
def power(num, x=1):
  result = 1;
  for i in range(x):
    result = result * num;
  return(result);
# 
# print(power(2));
# print(power(2,3));
# print(power(x=3, num=2)); # can reverse the order of the arguments sent when done in this manner.

# 7. function with variable number of arguments
#      - the star in "*args" means that I can pass in a variable number of arguments.
def multi_add(*args):
  result = 0;
  for x in args:
    result = result + x
  return result
# 
# print(multi_add(4,5,10,4));
# => 23

