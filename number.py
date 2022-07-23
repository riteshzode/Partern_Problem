# This is a number patter problem project

n = 5

"""
Q 1:

    1
    1  2
    1  2  3
    1  2  3  4
    1  2  3  4  5
"""


for i in range(n):
    no = 1
    for j in range(i + 1):
        print(no, end="  ")
        no += 1
    print()

print()

"""
Q 2:

    1
    2  3
    4  5  6
    7  8  9  10
    11  12  13  14  15
"""

no = 1

for i in range(n):

    for j in range(i + 1):
        print(no, end="  ")
        no += 1
    print()
print()

"""
Q 3:

    1
    2  1
    3  2  1
    4  3  2  1
    5  4  3  2  1
"""

for i in range(n):

    for j in range(i, -1, -1):
        print(j + 1, end="  ")

    print()

print()

"""
Q 4:

    5
    5  4
    5  4  3
    5  4  3  2
    5  4  3  2  1
"""

for i in range(n):

    for j in range(i + 1):
        print(n - j, end="  ")

    print()

print()

"""
Q 5:

    5  4  3  2  1
    5  4  3  2
    5  4  3
    5  4
    5

"""
for i in range(5):

    for j in range(5, i, -1):
        print(j, end="  ")

    print()

print()

"""
Q 6:
          1
        2 2 2
      3 3 3 3 3
    4 4 4 4 4 4 4
  5 5 5 5 5 5 5 5 5
    4 4 4 4 4 4 4
      3 3 3 3 3
        2 2 2
          1
"""

for i in range(n - 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(i + 1):
        print(i + 1, end=" ")

    for j in range(i):

        print(i + 1, end=" ")
    print()

for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")

    for j in range(i + 1, n):
        print(n - i, end=" ")

    for j in range(i, n):
        print(n - i, end=" ")
    print()

print()

"""
Q 7:
          1
        2 2 2
      3 3 3 3 3
    4 4 4 4 4 4 4
  5 5 5 5 5 5 5 5 5
"""

for i in range(n):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(i + 1):
        print(i + 1, end=" ")

    for j in range(i):
        print(i + 1, end=" ")
    print()

print()

"""
Q 8:

  5 5 5 5 5 5 5 5 5 
    4 4 4 4 4 4 4 
      3 3 3 3 3 
        2 2 2 
          1 

"""


for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")

    for j in range(i + 1, n):
        print(n - i, end=" ")

    for j in range(i, n):
        print(n - i, end=" ")
    print()

print()