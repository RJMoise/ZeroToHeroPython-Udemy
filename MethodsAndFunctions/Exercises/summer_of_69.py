#summer_of_69
#Return the sum of the numers in an array, except ignore sections of numbers starting with 6 and extending to the next 9.

def summer_of_69(arr):
    total = 0
    summer = False
    for i in arr:
        if i == 6:
            summer = True
        if summer == False:
            total +=i
        if  i == 9:
            summer = False        
    print(total)

#I'd argue how optimal this is
def optimal_summer_of_69(arr):
    total = 0
    summer = True
    for i in arr:
        while summer:
            if i != 6:
                total += i
                break
            else:
                summer = False
        while not summer:
            if i != 9:
                break
            else:
                summer = True
                break
    print(total)



summer_of_69([1,3,5])
summer_of_69([4,5,6,7,8,9])
summer_of_69([2,1,6,9,11])

optimal_summer_of_69([1,3,5])
optimal_summer_of_69([4,5,6,7,8,9])
optimal_summer_of_69([2,1,6,9,11])