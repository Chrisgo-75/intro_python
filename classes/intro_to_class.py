#!/usr/bin/env python3

# Index
#   1. Simple Constructor example.
#   1b. Setter & Getter example for use with Simple Constructor (accessor methods)
#      * This method does not scale well.
#      * It is better to use getters/setters to control getting and setting
#        values via code than allowing values to be set/get from outside.
#   2. A more scalable approach in Python is to use a dictionary in Constructor.
#   3. An even more scalable approach is to use dictionaries for all
#   3b. Accessor methods
#   3c. Accessor methods on steroids


class Duck:
  # 1. Simple Constructor example
  #    * it is always a good idea to assign default values.
  # def __init__(self, color = 'white'):
  #   self._color = color
  # 1b. Setter & Getter example for use with Simple Constructor.
  #def set_color(self, color):
  #  self._color = color
  #def get_color(self):
  #  return self._color
  
  # 2. A more scalable approach in Python is to use a dictionary in Constructor.
  #def __init__(self, **kwargs):
    # Depending upon what you have in kwargs ... and can set default value (white).
    #self._color = kwargs.get('color', 'white')
    # When creating new object and wishing to pass/set a color via constructor:
    #   donald = Duck(color = 'blue')

  # 3. An even more scalable approach is to use dictionaries for all
  def __init__(self, **kwargs):
    self.variables = kwargs
  # 3b. Accessor methods
  #def set_color(self, color):
  #  self.variables['color'] = color
  #def get_color(self):
  #  return self.variables.get['color', None]
  #
  # 3c. Accessor methods on steroids
  #def set_variable(self, k, v):
  #  self.variables[k] = v
  #def get_variable(self, k):
  #  return self.variables.get(k, None)
  # Setting variable even AFTER object has been created
  #donald.set_variable('color', 'blue')
  # Getting variable from outside of this object
  #print(donald.get_variable('color'))




def main():
  donald = Duck(feet = 2)
  #Print donald's color
  # print(donald.get_color())
  #Change donald's color
  # donald.set_color('blue')



if __name__ == '__main__': main()