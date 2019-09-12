def odd_even(n):
    if n % 2 == 0:
        return 'EVEN'
    else: 
        return 'ODD'

def pos_neg(n):
    if n == 0:
        print('NULL')
    elif n > 0:
        print(odd_even(n) + ' POSITIVE')
    else:
        print(odd_even(n) + ' NEGATIVE')

for x in  range(int(input())):    
    pos_neg(int(input()))