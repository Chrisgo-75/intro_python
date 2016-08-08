#!/usr/bin/env python3

#
# Index
#   1- Before Python runs any code.
#   2- IF __name__ == '__main__'
#
#

# 1- Before Python runs any code.
#   a. Before Python runs any code, Python creates a few special variables.
#   b. "name" is one of those special variables.
#   c. When Python runs a Python file DIRECTLY, it sets this "__name__" variable to __main__.
#   d. 
#
#print("First Module's Name: {}".format(__name__))
# => First Module's Name: __main__


# 2- IF __name__ == '__main__'
#   a. Use if you want to run code when this file is called directly.
#   b. Very common line written in Python.
print('This print statement will always be called. No matter if this file is called directly or imported.')
def main():
  print('main_script.py was called directly.')

# 
# if __name__ == "__main__": main()
if __name__ == "__main__":
  main()
else:
  print('main_script.py ran via Import.')