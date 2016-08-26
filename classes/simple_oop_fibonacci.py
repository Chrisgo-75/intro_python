#!/usr/bin/env python3

# simple fibonacci series
# the sum of two elements defines the next set
# Tid bits of info
#   * All methods within a class have self as the first argument. It's not required BUT
#     it's a really, really good idea to always call it self.
#   * Creating a new object syntax: ClassName() ... so the name of the class with parens.
#   * $ python3  # opens python shell
#       - >>> id(x)  # shows the ID of this variable/object x.
#         >>> 87643021609
#       - >>> type(x) # displays object type/class
#         >>> <class 'int'>
#       - 
#
class Fibonacci():
  # self == reference to the instance of this class or instance_object.
  # __init__ is a special function or method (constructor) that gets called when
  #          an instance of this Class is initialized.
  def __init__(self, a, b):
    self.a = a # creates object variable.
    self.b = b
  
  # self == reference to the instance of this class or instance_object.
  # This function/method is a generator function.
  def series(self):
    while(True):
      # The below "yield" generates an iterator that is used in
      #   "for r in f.series():"
      yield(self.b)
      self.a, self.b = self.b, self.a + self.b


f = Fibonacci(0,1)
for r in f.series():
  if r > 100: break
  print(r, end=' ')




