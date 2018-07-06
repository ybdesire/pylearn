from deuces import Card
from deuces import Evaluator
from deuces import Deck


def print_cards(cards, rank_class):
    s = []
    for x in cards:
        s.append(Card.int_to_str(x))
    print(s, rank_class)


def is_good(board_cards=[],hand_cards=['AH', 'KD']):
    if(len(board_cards)+len(hand_cards)==0):
        return False
    
    board = []
    for x in board_cards:
        c = Card.new('{0}{1}'.format(x[0], x[1].lower()))
        board.append(c)
    
    hand = []
    for x in hand_cards:
        c = Card.new('{0}{1}'.format(x[0], x[1].lower()))
        hand.append(c)
    
    evaluator = Evaluator()
    deck = Deck()
    random_cards = deck.draw(5-len(board)-len(hand))
    score = evaluator.evaluate(board+random_cards, hand)
    rank_class = evaluator.get_rank_class(score)
    
    print_cards(board+random_cards+hand, rank_class)
    
    if(rank_class<9):
        return True
    return False
    
    
print( is_good([],hand_cards=['AH', 'AD']) )    
print( is_good(['AH'],hand_cards=['AH', 'KD']) )    
print( is_good(['2D','4D','6D'],hand_cards=['AH', 'KD']) )    