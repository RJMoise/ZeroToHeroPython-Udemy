#spy_game
#Write a function that takes in a list of ints and returns True if it contains 007 in order


def spy_game(nums):
    spy = [0,0,7]
    checklist = nums[0:3]
    for i in range(len(nums)):
        if checklist == spy:
            print("Spy has been found")
            return
        else:
            checklist = nums[i:i+3]
    print("There was no spy...or were they that good?")

def optimal_spy_game(nums):
    #I hadn't understood that the 007 didn't have to be beside each other, and still pass the test
    spy = [0,0,7,'x']
    for num in nums:
        if num == spy[0]:
            spy.pop(0)
    print (len(spy)==1)



spy_game([1,2,4,0,0,7,5])
spy_game([1,0,2,4,0,5,7])
spy_game([1,7,0,7,4,5,0])

optimal_spy_game([1,2,4,0,0,7,5])
optimal_spy_game([1,0,2,4,0,5,7])
optimal_spy_game([1,7,0,7,4,5,0])