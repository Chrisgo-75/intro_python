#!/usr/bin/env python3

# Index
#   1. Base or Parent Class
#   2. Duck is an Animal or Duck is inherting from Animal.
#

# 1. Base or Parent Class
class Animal:
  def talk(self): print('I have something to say!')
  def walk(self): print('Hey! I''m walkin'' here!')
  def clothes(self): print('I have nice clothes')

# 2. Duck is an Animal
class Duck(Animal):
  def quack(self):
    print('Quaaack!')
  # "walk" method in Duck overrides "walk" method in Animal.
  def walk(self):
    print('Walks like a duck.')


def main():
  donald = Duck()
  donald.quack()
  donald.walk() # "walk" method in Duck overrides "walk" method in Animal.
  donald.clothes() # calling method from Animal class.



if __name__ == '__main__': main()