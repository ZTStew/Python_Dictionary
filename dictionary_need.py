"""
Problem:
  I have a string named, 'book'. I want to know how many of each character there is in this string.

This solution is for before being told about dictionaries

Number of characters:
  [a-z] - 26
  [A-Z] - 26
  [0-9] - 10
  [.-!] - 31
  Total: 93
"""

book = "This is a test string of book. Book is good test string"

"""
Option 1: create a variable for each character
Problems:
  cannot refer to a variable making it impossible to iterate
  lots of copy paste
  would need 93 unique variables, if checks, print statements
"""

"""
a = 0
b = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0

for it in range(len(book)):
  # print(book[it])
  if book[it] == 'a':
    a += 1
  elif book[it] == 'b':
    b += 1
  elif book[it] == 'c':
    c += 1
  elif book[it] == 'd':
    d += 1
  elif book[it] == 'e':
    e += 1
  elif book[it] == 'f':
    f += 1
  elif book[it] == 'g':
    g += 1
  elif book[it] == 'h':
    h += 1
  elif book[it] == 'i':
    i += 1

print('a = ' + str(a))
print('b = ' + str(b))
print('c = ' + str(c))
print('d = ' + str(d))
print('e = ' + str(e))
print('f = ' + str(f))
print('g = ' + str(g))
print('h = ' + str(h))
print('i = ' + str(i))
"""

"""
Option 2: Use an array to contain characters

this makes it so that there is far less copy pasting that is happening. no longer need to refer to variables by name

Problems:
  Still need to manually type each character
  ibc to clock cycle
  worst case number of iterations would be len(book)^93 || 55^93 -> 7.14052465 x 10^161
  assuming a processor can handle 20 actions a second, it would take 
  3.57026232 x 10^160 seconds
  or
  5.9504372 x 10^158 minutes
  or
  9.91739533 x 10^156 hours
  or
  4.13224806 x 10^155 days
  or
  1.13212275 x 10^153 years
  to process in the worst case scenerio
"""

"""
characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]

# loops through book's characters
for it in range(len(book)):
  # loops through characters
  for jt in range(len(characters)):
    if characters[jt] == book[it]:
      counts[jt] += 1

for it in range(len(characters)):
  print(characters[it] + ' = ' + str(counts[it]))
"""

"""
Option 3: Use a nested array to contain characters
  this makes it so that you only need to keep a single array

Problems:
  has the same issues as option 2
"""

"""
characters = [['a', 0], ['b', 0], ['c', 0], ['d', 0], ['e', 0], ['f', 0], ['g', 0], ['h', 0], ['i', 0]]
for it in range(len(book)):
  for jt in range(len(characters)):
    if characters[jt][0] == book[it]:
      characters[jt][1] += 1

for it in range(len(characters)):
  print(characters[it][0] + ' = ' + str(characters[it][1]))
"""

########################################################################################################################
########################################################################################################################
########################################################################################################################

"""
Option 4:
  use a dictionary
  removes nested loops
  can refer to and search for characters by name now
"""

"""
dict = {
  'a': 0,
  'b': 0,
  'c': 0,
  'd': 0,
  'e': 0,
  'f': 0,
  'g': 0,
  'h': 0,
  'i': 0
}

for it in range(len(book)):
  if book[it] in dict:
    dict[book[it]] += 1

for key in dict:
  print(key, '->', dict[key])
"""

"""
Option 4:
  use a dictionary
  removes nested loops
  can refer to and search for characters by name now
"""

dict = {}

for it in range(len(book)):
  if book[it] in dict:
    dict[book[it]] += 1
  else:
    dict[book[it]] = 1  

for key in dict:
  print(key, '->', dict[key])
