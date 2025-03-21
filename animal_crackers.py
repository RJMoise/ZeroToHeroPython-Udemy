#animal crackers
#check if the first letter of two words is the same

def animal_crackers(crackers):
    twocrackers = crackers.split(" ")

    if twocrackers[0][0] == twocrackers[1][0]:
        print ("True")
    else:
        print ("False")

def better_animal_crackers(crackers):
    #ADD UPPER TO ACCOUNT FOR DIFFERENT CHARACTER CASES
    twocrackers = crackers.upper().split()
    #PRINT THE BOOLEAN RESULT ITSELF
    print(twocrackers[0][0] == twocrackers[1][0])



better_animal_crackers("Levelheaded llama")
better_animal_crackers('Crazy Kangaroo')