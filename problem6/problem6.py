'''
Sum Square Difference
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2+... +10^2 = 385.
The square of the sum of the first ten natural numbers is,
(1 + 2+... +10)^2 = 55^2 = 3025.
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''


#step 1: make function that sums squares of all values up to x

def square_cumulative(x):
    sum = 0
    for i in range (1,x+1):
        sum += i ** 2
    return sum


#step 2: find the difference between square_cumulative(100) and (sum of numbers 1-100)^2


print(sum(range(101))**2 - square_cumulative(100)) # 25164150