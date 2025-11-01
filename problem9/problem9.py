'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2.
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.


process:
find pythagorean triplets up to c = 961 = 31^2 because 961 is the highest square under 1000

upon finding a pythagorean triplet, check if it sums to 1000. If it does, find the product of a b and c
'''
import numpy as np
squares = [x**2 for x in range(1,961)] #list of squares to check values against

for c in range(961,0,-1): 

    for b in range(1,962):

        if c**2 - b**2 in squares: #this line checks whether a b and c are a pythagorean triplet

            if np.sqrt(c**2-b**2) + b + c == 1000:

                print(int(np.sqrt(c**2-b**2))*b*c) #31875000

                break

