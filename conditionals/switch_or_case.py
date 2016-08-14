#!/usr/bin/env python3

# Index
#   Python does not have a "switch" or "case" control structure which
#   allows you to select from multiple choices of a single variable.
#   But there are strategies that can simulate it.
#
#   1. 



def main():
  # 1. 
  choices = dict(
      one = 'first',
      two = 'second',
      three = 'third',
      four = 'fourth',
      five = 'fifth'
  )

  print('Looking for "seven" in dictionary. If it doesn\'t exist then print "other":')
  v = 'seven'
  print(choices.get(v, 'other'))
  print()

  print('Looking for a key of "five" and if found print it\'s value:')
  v = 'five'
  print(choices.get(v, 'other'))
  print()



if __name__ == '__main__': main()