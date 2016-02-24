factors = [600851475143]
stop = False
i = 1
a = 0

def checkIfAllPrime(ListToCheck):
    for x in ListToCheck:
        for i in range(2, int(x)):
            if((x%i == 0) and (i!=1 or i!=x)):
                return False
    return True

#Main loop, run as long as all the number in the list aren't prime
while stop == False:

    #Check if all the number in the factors list are prime
    if checkIfAllPrime(factors) == True: #if it's true, we end our main "while" loop
        stop = True

    #loop runs as long as i is smaller than factor[a]
    while (i < factors[a]):
        if (factors[a]%i == 0 and i != 1): #check if factors[a]/i results in a natural number
            factors.append(i) #add i to the list
            factors.append(factors[a]/i) #add factors[a]/i to the lists
            factors.pop(a) #delete factors[a] from the list
        else:
            i = i + 1

    #if a got bigger than the amount of number in the factors list, we reset it to 0
    #otherwise we add 1 to a.
    if a < len(factors):
        a = a + 1
    else:
        a = 0

#Remove the "1.0" in the list
t = []
for y in factors:
    if y != 1.0:
        t.append(y)
#show list
print(t)
