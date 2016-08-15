#!/usr/bin/env python3
# File: /home/cgarndt/Python/Lyndadotcom-upandrunningwithpython/loops.py

# Index
#   * Python uses two types of looping constructs called FOR and WHILE.
#   1. Define a While loop
#      b. WHILE loop in Fibonacci series. (else can be used in a while loop).
#   2. Define a For loop
#      b. FOR loop ... read lines from a file. FOR loops uses interaters.
#   3. Use a For loop over a collection.
#   4. Use the BREAK and CONTINUE statements
#      b. CONTINUE: Skip printing "S"s via the "continue" statement
#      c. BREAK: STOP or BREAK out of the loop entirely by using the BREAK statement
#      d. ELSE: At the end of the looping then do the else clause.
#   5. Using the enumerate() function to get index
#

def main():
  x = 0;
  
  # 1. Define a While loop
#   while(x < 5):
#     print(x);
#     x = x + 1;
#=> ... prints 0,1,2,3,4
#
#   1b. WHILE loop in Fibonacci series.
#   a, b = 0, 1
#   while b < 50:
#     print(b);
#     a, b = b, a + b;
#   print('Done.');
#=> ... prints 1,1,2,3,5,8,13,21,34,Done.
  
  # 2. Define a For loop
  #   - python For loops are what are called "iterators". Need to use range().
#   for x in range(5,10):
#     print(x);
#=> ... prints 5,6,7,8,9 and excludes 10.
#
# 2b. FOR loop ... read lines from a file. FOR loops uses interaters.
  # read the lines from the file
#  fh = open('lines.txt');
#  for line in fh.readlines():
#    print(line); # print puts a new line at the end or line break.
    # OR to not have print add line breaks then add "end=''"
#    print(line, end='');

#   3. Use a For loop over a collection.
#        * the FOR loop does not have a counter.
#   days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
#   for d in days:
#     print(d);
#=> ... prints all the abbrev. days within collection.

# 4. Use the BREAK and CONTINUE statements
#   for x in range(5,10):
#     #if(x == 7): break
#     if(x % 2 == 0): continue
#     # Above if statement in English
#     # Take x divided it by 2. And if the value left over is equal to 0 THEN
#     # continue which means don't do print statement but go back to the start of the loop.
#     # So in essence, don't print on even numbers.
#     print(x);
# 4b. Skip printing "S"s via the "continue" statement
#   s = 'this is a string'
#   for c in s:
#     if c == 's': continue # if c == 's' then skip the print statement/go to FOR statement.
#     print(c, end='')
# 4c. STOP or BREAK out of the loop entirely by using the BREAK statement
#   s = 'this is a string'
#   for c in s:
#     if c == 's': break
#     print(c, end='')
# 4d. ELSE: At the end of the looping then do the else clause.
#   s = 'this is a string'
#   for c in s:
#     print(c, end='')
#   else:
#     print('else')
#
# 5. Using the enumerate() function to get index
#      * Yes the FOR loop does not have a counter BUT you can get one if you really need it.
#      * So
#   days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
#   # The enumerate function is going to iterate over days collection AND return the value
#   # of the item being looked at in addition to returning the index of the item in question.
#   # So the function returns two values.
#   for i, d in enumerate(days):
#     print(i, d);


if(__name__ == "__main__"):
  main();

