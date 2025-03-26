#blackjack
#given 3 ints between 1-11, if their sum is = 21, return the sum. If it is > 21 and there is an eleven, reduce total sum by 10. Finally if the sum exceeds 21, return BUST

def blackjack(a,b,c):
    total=a+b+c
    if total > 21 and (a == 11 or b == 11 or c ==11):
        total=total-10
    if total <= 21:
        print(total)
    else:
        print('BUST')

def optimal_blackjack(a,b,c):
    #Use Sum instead
    if sum([a,b,c]) <= 21:
        print(sum([a,b,c]))
    elif sum([a,b,c]) >= 21 and 11 in [a,b,c]:
        print(sum([a,b,c])-10)
    else:
        print("BUST")

blackjack(5,6,7)
blackjack(9,9,9)
blackjack(9,9,11)

optimal_blackjack(5,6,7)
optimal_blackjack(9,9,9)
optimal_blackjack(9,9,11)