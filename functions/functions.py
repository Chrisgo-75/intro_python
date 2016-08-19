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
#        a. You can also assign "none" as a default value.
#           - "none" is a special value that you can test for.
#              IF param1 is None:
#                param1 = 9
#        b. state parameter as "incoming optional arguments". (i.e. below)
#   7. Function with variable number of arguments
#      7b. Function with optional incoming arguments.
#   8. Quick Start Example: Checking if a number is a prime number or not
#   9. Have a parameter value within a function be assigned a value by default
#        i.e. def func(a=7):
#   10. Valid empty function that will not raise Python errors.
#   11. Named arguments example ... Yes!!!
#       - **kwargs is a "dictionary".
#   12. 

# ---

# define a function
# def func1():
#   print('I am a function');

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
# def func2(param1, param2):
#   print(param1, " ", param2);

# 4. function that takes parameters
# func2(10,20);
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
#
# 7b. Function with optional incoming arguments.
def testfunc(*args):
  print('Function example with optional incoming arguments:')
  print(args)
  # could also iterate over args by
  # for n in args: print(n, end='  ')
# call testfunc
#testfunc(1,3,5)
#=> (1, 3, 5)  # displays normal tuple which is "immutable" ... can't add/change it.
#print()


# 8. Quick Start Example: Checking if a number is a prime number or not
def isprime(n):
  if n ==1:
    print('1 is special');
    return False;
  for x in range(2,n):
    if n % x == 0:
      print("{} equals {} x {}".format(n, x, n // x));
      return False;
  else:
    print(n, 'is a prime number');
    return True;
# Call above function in a FOR loop
# for n in range(1,20):
#   isprime(n);
#=> ... below
#     1 is special
#     2 is a prime number
#     3 is a prime number
#     4 equals 2 x 2 # 4 is not a prime numb b/c it is devisible evenly by 2.
#     5 is a prime number
#     6 equals 2 x 3
#     ...and so on up to 19.

# 10. Valid empty function that will not raise Python errors.
def validemptyfunc():
  pass
# call above function.
# validemptyfunc()

# 11. Named arguments example ... Yes!!!
def testfunc(**kwargs):
  # kwargs is a "dictionary".
  print('Named arguments example:')
  #TODO edit below to show print kwards['one'] AND THEN its value.
  print(kwargs['one'], kwargs['two'], kwargs['four'])

testfunc(one = 1, two = 2, four = 42)
print()





