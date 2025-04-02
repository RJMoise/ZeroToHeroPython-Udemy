#count_primes
#write a function that returns the number of prime numbers that exist up to and including a given number

def count_primes(num):
    num_primes = 0
    factor = 0
    for i in range(num+1):
        if i > 1:
            for k in range(i+1):
                if k >= 1:
                    if i % (k) == 0:
                        factor +=1
            if factor > 2:
                pass
            else:
                num_primes+=1
            factor = 0
    print(num_primes)

def optimal_count_primes(num):

    #check for 0 or 1 input
    if num <2:
        return 0
    
    #If two or greater, do the below

    #Store Prime Numbers
    primes = [2]
    x=3

    #x is going through every number up to the input num
    while x <= num:
        #check if Prime
        #We go in steps of two because no even number past 2 will be prime, we skip them
        for y in range (3,x,2):
            if x%y==0:
                x+=2
                break
        else:
            primes.append(x)
            x+=2

    print(len(primes))


count_primes(100)
optimal_count_primes(100)