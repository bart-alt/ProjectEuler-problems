'''
Lychrel Numbers
Problem 55

If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
Not all numbers produce palindromes so quickly. For example,
349 + 943 = 1292
1292 + 2921 = 4213
4213 + 3124 = 7337
That is, 349 took three iterations to arrive at a palindrome.
Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. A number that never forms a palindrome through the reverse and add process is called a Lychrel number. Due to the theoretical nature of these numbers, and for the purpose of this problem, we shall assume that a number is Lychel until proven otherwise. In addition you are given that for every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations, or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).
Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
How many Lychrel numbers are there below ten-thousand?
'''


#step1: write a function that takes x, reverses its digits to make y and adds x + y

def reverse_and_add(x):
    #x = str(x)
    #y = int(x[::-1])
    
    return (x + int(str(x)[::-1]))



#step2: write a function that looks for palindromes


def pallindrome_finder(x):
    x = str(x)   

    for i in (range (int(len(x)//2))): #I'm making the assumption that single digit numbers count as pallindromes so I am intentionally not correcting the fact that this condition doesn't account for single digit numbers
        if x[i] != x[-(i+1)]: 
            return False

    return True


#step3: make the Lychrel function

def Lychrel(x):
    x = reverse_and_add(x)

    for i in range (50):

        if  pallindrome_finder(x)== True:
            return True

        else:
            x = reverse_and_add(x)

    return False


#step4: count how many times the function Lychrel(x) is wrong for values of x below 10000

Lychrel_counter = 0
for i in range(10000):
    if not Lychrel(i):
        Lychrel_counter += 1

print(f"Lychrel_counter = {Lychrel_counter}") #Lychrel_counter = 249
