#master_yoda
#return the given sentence in reverse

# My Solution
def master_yoda(text):
    newtext = text.split()
    reversedtext = ""
    x=1
    for i in range(len(newtext)):   
        reversedtext += newtext[len(newtext)-x] + " "
        x+=1
    print (reversedtext)

# Given optimal solution
def optimal_master_yoda(text):
    newtext = text.split()
    reversedtext = newtext[::-1]
    print (" ".join(reversedtext))

print("\nMy Solution Results")
master_yoda("I am home now")
master_yoda('We are ready')

print ("\nGiven Solution Results")
optimal_master_yoda("I am home now")
optimal_master_yoda('We are ready')