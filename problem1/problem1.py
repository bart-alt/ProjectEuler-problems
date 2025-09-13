#find the sum of all the multiples of 3 and 5 below 1000

#iterate through a for loop of 1000 and checking whether each value is a multiple of 3 or 5 and adding it

sum_of_multiples_3_5 = 0

for i in range(1000):
    if i%3==0 or i%5==0:
        sum_of_multiples_3_5 +=i

print(sum_of_multiples_3_5) #the sum is 233168