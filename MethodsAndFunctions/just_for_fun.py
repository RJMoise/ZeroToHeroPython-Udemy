#just_for_fun
#write a function that takes a single letter and returns a 5x5 representation of that letter.
#Note: we can stop at E for this excersize

def just_for_fun(letter):
    letterdict={"A": ["A","  *  "," * * ","*****","*   *","*   *"],
                "B": ["B","*****","*   *","***","*   *","*****"],
                "C": ["C","*****","*    ","*    ","*    ","*****"],
                "D": ["D","***  ","*   *","*   *","*   *","***"],
                "E": ["E","*****","*    ","*****","*    ","*****"]}
    for i in range (6):
        print(letterdict[letter][i])

def optimal_just_for_fun(letter):
    patterns = {1: '  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*  * ',9:'*    '}
    alphabet= {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}

    for pattern in alphabet[letter.upper()]:
        print(patterns[pattern])

just_for_fun('A')
just_for_fun('B')
just_for_fun('C')
just_for_fun('D')
just_for_fun('E')

optimal_just_for_fun('A')
optimal_just_for_fun('B')
optimal_just_for_fun('C')
optimal_just_for_fun('D')
optimal_just_for_fun('E')