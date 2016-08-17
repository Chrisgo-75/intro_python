#!/usr/bin/env python3

# Index
#   Intro
#     a. Regular Expressions in Python are implemented with the "re" module. And
#        is distrubted with Python.
#     b. "import re" # imports the module.
#     c. PRECOMPILE your patterns if using them more than once, in loops, etc.
#     
#     1. Searching a file for Lenore or Nevermore example
#          - searching with regular expressions is done using re Module's search method.
#
#     2. Print out the "match" of the regular expression
#          - useful for searching for patterns in text.
#          - useful for looking at replacing patterns in text.
#
#     3. Search and replace
#          - "sub" is the search and replace method.
#        3a. Prints the whole file and if match found replaces with hashes.
#        3b. Print those lines where the match was found.
#            - doing the search and replace in two different steps.
#
#     4. Precompile Regular Expression when you will be using it over and over again.
#        - more effecient.
#        - allows access to some of its more advanced functionalities.
#          - have regex ignore case via "re.IGNORECASE"


def main():
#   # 1. Searching a file for Lenore or Nevermore example
#   fh = open('raven.txt') # this file doesn't exist!
#   for line in fh:
#     if re.search('(Len|Neverm)ore', line):
#       print(line, end='')
#       # The above prints out the whole lines containing Lenore or Evermore.

#   # 2. Print out the "match" of the regular expression
#   fh = open('raven.txt') # this file doesn't exist!
#   for line in fh:
#     match = re.search('(Len|Neverm)ore', line)
#     if match:
#       print(match.group())
#       # above prints out just Lenore or Nevermore ... where it found matches.

#   # 3. Search and replace
#   #   3a. Prints the whole file and if match found replaces with hashes.
#   fh = open('raven.txt') # this file doesn't exist!
#   for line in fh:
#     print(re.sub('(Len|Neverm)ore', '###', line), end='')
#     # above prints the whole file and if match found replaces with hashes.
#   #   3b. Print those lines where the match was found.
#   fh = open('raven.txt') # this file doesn't exist!
#   for line in fh:
#     match = re.search('(Len|Neverm)ore', line)
#     if match:
#       print(line.replace(match.group(), '###'), end='')

#   # 4. Precompile Regular Expression when you will be using it over and over again.
#   fh = open('raven.txt') # this file doesn't exist!
#   pattern = re.compile('(Len|Neverm)ore')
#   # Have regex ignore case via "re.IGNORECASE"
#   #   pattern = re.compile('(Len|Neverm)ore', re.IGNORECASE)
#   for line in fh:
#     if re.search(pattern, line):
#       print(line, end='')
#       # OR add in substition.
#       print(pattern.sub('###', line), end='')
#       # above prints just lines where matches was found and replaces matches w/hashes.
      



if __name__ == '__main__': main()