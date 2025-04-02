#almost_there
#check if a given number is within 10 of 100 or 200

def almost_there(num):
    print((num - 200 <= 10 and num - 200 >= -10 ) or (num - 100 <= 10 and num - 100 >= -10))

def optimal_almost_there(num):
    print((abs(100-num) <= 10) or (abs(200-num) <=10))

print("\nMy Solution Results")
almost_there(90)
almost_there(104)
almost_there(150)
almost_there(209)

print ("\nGiven Solution Results")
optimal_almost_there(90)
optimal_almost_there(104)
optimal_almost_there(150)
optimal_almost_there(209)