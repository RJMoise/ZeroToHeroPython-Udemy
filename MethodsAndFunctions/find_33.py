#Find 33
#Given a list of ints, return True if the array contains two 3's next to each other.

def find_33(nums):
    current_value=int()
    for num in nums:
        if num == current_value and num == 3:
            print('True')
            return
        else:
            current_value = num
    print('False')
    return

def optimal_find_33(nums):

    #We stop at the second to last digit, because going forward once more, there would be nothing to compare against
    for i in range (0,len(nums)-1):
        #Compare side by side values to each other
        if nums[i] == 3 and nums[i+1] == 3:
            print("True")
            return
    print("False")

find_33([1,3,3])
find_33([1,3,1,3])
find_33([3,1,3])
find_33([3,2,7,1,9,1,1,3,3])

optimal_find_33([1,3,3])
optimal_find_33([1,3,1,3])
optimal_find_33([3,1,3])
optimal_find_33([3,2,7,1,9,1,1,3,3])