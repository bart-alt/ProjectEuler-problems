#1-9 pandigital

#find the highest 1-9 9 number pandigital that can be formed as a concatenated product of an intiger with (1,2,...,n) where n>1

#step1: 1-9 pandigital creator function

def pandigital1_9(n):
    pandigital = "" #setting the pandigital variable as a string. this will be the pandigital number for each iteration
    i=1
    while len(pandigital) < 9:
        a = str(i * n) #a refers to the product to be concatenated onto pandigital
        if a.count("0") != 0: #if one of the numbers within the product is a 0, the final value wont be a 1-9 pandigital so the function must not return a value upon this condition
            return
        pandigital = pandigital + a #this line of code concatinates the product onto pandigital
        if len(pandigital) > 9: #if a 2, 4, or >5 digit value undergoes this function, the number of digits of pandigital will exceed 9 and therefore the value wont be a 1-9 pandigital so the function must not return a value upon this condition
            return
        i += 1
        '''
        print ("pandigital:",pandigital,"len(pandigital):",len(pandigital),"i:",i,"a:",a,"n:",n)
        '''

    for j in range(9):
        if pandigital.count(str(pandigital[j])) != 1: #this section checks that each 1-9 digit occurs only once. if a digit occurs twice, the value wont be a 1-9 pandigital so the function must not return a value upon this condition
            return


    return pandigital

#step2 brute force iterate through all possible values to find the highest pandigital

highest = 0
'''
highest_iteration = 0
pandigitals = []
'''
for j in range (1,9500):
    val = pandigital1_9(j)
    if val != None:
        checker = int(pandigital1_9(j))

        if checker > highest:
            highest = checker
            '''
            pandigitals.append(checker)
            pandigitals.append(j)
            ighest_iteration = j
            '''

print(highest) #the highest 1-9 pandigital is 932718654