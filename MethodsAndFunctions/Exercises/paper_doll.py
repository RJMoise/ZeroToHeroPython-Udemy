#paper_doll
#given a string, return a string where every character in the orignal are 3 characters

def paper_doll(text):
    new_text = ''
    for i in text:
        for k in range(3):
            new_text += i
    print(new_text)

def optimal_paper_doll(text):
    new_text = ''
    for i in text:
        #Just multiply the letter by 3 instead of looping through and adding it 3 times
        new_text += i*3
    print(new_text)


paper_doll('Hello')
paper_doll('Mississippi')

optimal_paper_doll('Hello')
optimal_paper_doll('Mississippi')