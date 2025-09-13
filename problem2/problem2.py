#By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

#step1: compute the highest fibonacci number below 4million


def fibonacci(f_iteration_UB): #f_iteration_UB be the Upper Bound for finding a fibonacci number and its position in the sequence
    f1 = 1
    f2 = 2
    f_position = 2

    while f2<=f_iteration_UB:
        placeholder = f2
        f2 += f1
        f1 = placeholder
        f_position+=1

    return [f2,f_position]

#print(fibonacci(4000000)) #this gives us 3524578, as the 33rd term. 

#since the first two terms are odd and even respectively, we can deduct that every 3rd term after 2 is even as
#odd + even = odd
#even + odd = odd
#odd + odd = even
#with this, we can alter our fibonacci function to create a variable that increases by the amount of f2 every 3 iterations


def fibonacci2(f_iteration_UB):
    f1 = 1
    f2 = 2
    f_position = 2
    cumulative_even = 0
    while f2<=f_iteration_UB:
        if (1+ f_position)%3 == 0:
            cumulative_even +=f2
        placeholder = f2
        f2 += f1
        f1 = placeholder
        f_position+=1

    return [cumulative_even]

print(fibonacci2(4000000)) #gives us 4613732

