# This is a patter problem project

n = 5

"""
1   * * * * *
    * * * * *
    * * * * *
    * * * * *
    * * * * *
"""

for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()

print()

"""
2   *
    * *
    * * *
    * * * *
    * * * * *
"""

for i in range(n):
    for j in range(i + 1):
        print("*", end=" ")
    print()

print()

"""
3   * * * * *
    * * * *
    * * *
    * *
    *
"""

for i in range(n):
    for j in range(n - i):
        print("*", end=" ")
    print()

print()

""" Hill pattern
4         *
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * *

"""

for i in range(5):
    for j in range(5 - i):
        print(" ", end=" ")

    for j in range(i + 1):
        print("*", end=" ")

    for j in range(i):
        print("*", end=" ")
    print()

print()

""" Reverse Hill pattern
5    * * * * * * * * *
       * * * * * * *
         * * * * *
           * * *
             *

"""

for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")

    for j in range(i + 1, n):
        print("*", end=" ")

    for j in range(i, n):
        print("*", end=" ")
    print()

print()

""" Diamond pattern
6         * 
        * * * 
      * * * * * 
    * * * * * * * 
  * * * * * * * * * 
    * * * * * * * 
      * * * * * 
        * * * 
          * 
"""
for i in range(n - 1):
    for j in range(n - i):
        print(" ", end=" ")

    for j in range(i + 1):
        print("*", end=" ")

    for j in range(i):
        print("*", end=" ")
    print()

for i in range(n):
    for j in range(i + 1):
        print(" ", end=" ")

    for j in range(i + 1, n):
        print("*", end=" ")

    for j in range(i, n):
        print("*", end=" ")
    print()
