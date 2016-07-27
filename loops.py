#!/usr/bin/env python3
# File: /home/cgarndt/Python/Lyndadotcom-upandrunningwithpython/loops.py

# Index
#   1. Define a While loop
#   2. Define a For loop
#   3. Use a For loop over a collection.
#   4. Use the BREAK and CONTINUE statements
#   5. Using the enumerate() function to get index
#

def main():
  x = 0;
  
  # 1. Define a While loop
#   while(x < 5):
#     print(x);
#     x = x + 1;
#=> ... prints 0,1,2,3,4
  
  # 2. Define a For loop
  #   - python For loops are what are called "iterators". Need to use range().
#   for x in range(5,10):
#     print(x);
#=> ... prints 5,6,7,8,9 and excludes 10.

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

# 5. Using the enumerate() function to get index
#      * Yes the FOR loop does not have a counter BUT you can get one if you really need it.
#      * So
  days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun'];
  # The enumerate function is going to iterate over days collection AND return the value
  # of the item being looked at in addition to returning the index of the item in question.
  # So the function returns two values.
  for i, d in enumerate(days):
    print(i, d);


if(__name__ == "__main__"):
  main();

