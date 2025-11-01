'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


process:
find pythagorean triplets up to c = 500 because a + b + c = 1000, a < b < c, and a + b > c so c < 500

upon finding a pythagorean triplet, check if it sums to 1000. If it does, calculate the product of a b and c
'''
import numpy as np
squares = [x**2 for x in range(1,500)] #list of squares to check values against

for c in range(500,0,-1): 

    for b in range(1,501):

        if c**2 - b**2 in squares: #this line checks whether a b and c are a pythagorean triplet

            if np.sqrt(c**2-b**2) + b + c == 1000:

                print(int(np.sqrt(c**2-b**2))*b*c) #31875000

                break

