#!/usr/bin/env python3

# Index
#   1. Define a "dictionary".
#      a. Print Dictionary which doesn't print it in ascending
#         order. Or even in the order it was saved in.
#      b. Print out the Dictionaries keys and values.
#   2. Keyword Arguments might be a easier approach which is
#      explained in depth more in the "Functions" section.
#      - Keyword Arguments is a much easier, convenient, and
#        more common way.
#   3. Dictionaries are "mutable" objects. So a new value can
#      be added.
#

def main():
  # 1. Define a "dictionary" or "hash" or "Associative Array"
  print('a. Example of a "Python Dictionary":')
  d = { 'one': 1, 'two':2, 'three':3, 'four':4, 'five':5 }
  print(d)
  #=> {'one': 1, 'three': 3, 'two': 2, 'four': 4, 'five': 5}
  print()
  #
  print('b. print the Dictionaries keys and values:')
  for k in d:
    print(k, d[k])
  print()
#
  print('c. printed Dictionary in sorted order (alphabetical order) by keys:')
  for k in sorted(d.keys()):
    print(k, d[k])
  print()

  print('2. Keywword Arguments:')
  dka = dict(
             one =1, two =2,three =3, four='four', five='five'
  )
  for k in sorted(dka.keys()):
    print(k, dka[k])
  print()

  print('3. Dictionaries are "mutable" objects, so 7 can be added:')
  dka['seven'] = 7
  for k in sorted(dka.keys()):
    print(k, dka[k])
  print()



if __name__ == '__main__': main()