#makes_twenty
#are any of the given values 20, and do any of the sums equal 20

def makes_twenty(a,b):
    if a == 20 or b == 20 or a+b == 20:
        print ('True')
    else:
        print("False")

def better_makes_twenty(a,b):
    #RETURN THE BOOLEAN ITSELF
    print( a == 20 or b == 20 or a+b == 20)


better_makes_twenty(20,10)
better_makes_twenty(12,8)
better_makes_twenty(2,3)