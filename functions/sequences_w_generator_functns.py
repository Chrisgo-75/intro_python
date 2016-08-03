#!/usr/bin/env python3

# Description
# a. Generator functions are an incredibly useful pattern in Python. Generator functions actually creates an iterator.


# Index
#   Generator Function that generates an iterator suitable for use in a FOR loop.
#   Describes "yield"

# Utility Function
def isprime(n):
  if n == 1:
    return False
  for x in range(2, n):
    if n % x == 0:
      return False
  else:
    return True

# This is the "Generator".
def primes(n = 1):
  while(True):
    # yield is like "return".
    # So "yield" returns a  value, BUT then the next time the function is called, it
    #   continues execution after the yield.
    # "yield" returns an iterator object, that is suitable for use in a for loop. 
    if isprime(n): yield n
    n += 1


for n in primes():
  if n > 100: break
  print(n)

