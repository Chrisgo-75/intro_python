#!/usr/bin/env python3

# Index
#   1. Catch any error examples.
#      1a. The else clause will only run if no exceptions/errors are caught.
#      1b. Don't necessarily need the else clause ... code could be put in the try area.
#   2. Catch IOError (triggered when can't find file or file doesn't exist)
#   3. Catch and print error message.
#   4. Can also "raise" exceptions/error manually.
#   5. Python has a predefined number of exceptions in it library at
#      http://docs.python.org/library/exceptions.html


def main():
#   # 1. Catch any error example.
#   # 1a. The else clause will only run if no exceptions/errors are caught.
#   try:
#     fh = open('xlines.txt')
#   except:
#     # Any errors/exceptions caught will run this suite.
#     print('could not open the file. come back tomorrow.')
#   else:
#     # IF no errors/exceptions caught THEN run this suite.
#     for line in fh: print(line.strip())
#   # 1b. Don't necessarily need the else clause ... code could be put in the try area.
#     try:
#     fh = open('xlines.txt')
#     for line in fh: print(line.strip())
#   except:
#     # Any errors/exceptions caught will run this suite.
#     print('could not open the file. come back tomorrow.')

#   # 2. Catch IOError (triggered when can't find file or file doesn't exist)
#   try:
#     fh = open('xlines.txt')
#   except IOError:
#     # 
#     print('could not open the file. come back tomorrow.')
#   else:
#     for line in fh: print(line.strip())

#   # 3. Catch and print error message.
#   try:
#     fh = open('xlines.txt')
#   except Exception as e:
#     # except Exception, e   ... should work too.
#     print('could not open the file.', e)
#   else:
#     for line in fh: print(line.strip())

#   # 4. Can also "raise" exceptions/error manually.
#   try:
#     for line in readfile('xlines.doc'): print(line.strip())
#   except IOError as e:
#     print('cannot read file:', e)
#   except ValueError as e:
#     print('bad filename', e)
# 
# def readfile(filename):
#   if filename.endswith('.txt'):
#     fh = open(filename)
#     return fh.readlines()
#   else: raise ValueError('Filename must end with .txt')





if __name__ == '__main__': main()