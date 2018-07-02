from deuces import Card

# define one card
card = Card.new('Ah')

# table cards
board = [
    Card.new('Ah'),
    Card.new('Kd'),
    Card.new('Jc')
]

# self cards
hand = [
   Card.new('Qs'),
   Card.new('Th')
]

# card is presented as int at deuces: https://github.com/worldveil/deuces/blob/master/deuces/card.py
print(card)# 268446761
# int to string
print(Card.int_to_str(card))#Ah


for c in board+hand:
    print(Card.int_to_str(c))
    
'''
Ah
Kd
Jc
Qs
Th
'''    