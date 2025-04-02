#lesser_of_two_evens
#if both nums are even, return smallest
#if any num is odd, return largets

def lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        if a<b:
            return a
        else:
            return b
    else:
        if a>b:
            return a
        else:
            return b
        
def better_lesser_of_two_evens(a,b):
    if a%2==0 and b%2==0:
        #BOTH NUMBERS ARE EVEN, RETURN SMALLEST
        return min(a,b)
    else:
        #ONE OR MORE IS ODD, RETURN LARGEST
        return max(a,b)
        

num = better_lesser_of_two_evens(10,4)
num2 = better_lesser_of_two_evens(9,5)

print (str(num) + " " + str(num2))