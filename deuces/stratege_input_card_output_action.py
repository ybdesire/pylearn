from deuces import Card
from deuces import Evaluator
from deuces import Deck
from itertools import combinations


def print_cards(cards, rank_class):
    s = []
    for x in cards:
        s.append(Card.int_to_str(x))
    print(s, rank_class)


def get_score_by_simulate(hand, board, iteration=100):
    if(len(hand)+len(board)<=5):
        score_list = []
        for i in range(iteration):
            evaluator = Evaluator()
            deck = Deck()
            random_cards = deck.draw(5-len(board)-len(hand))
            score = evaluator.evaluate(board+random_cards, hand)
            score_list.append(score)
            
        score_list.remove(max(score_list))    
        score_list.remove(min(score_list))    
        
        return sum(score_list)/float(len(score_list))
    else:
        score_min = 9999999
        for board_five_match in combinations(board,5-len(hand)):
            evaluator = Evaluator()
            score = evaluator.evaluate(tuple(board_five_match), tuple(hand))
            if(score<score_min):
                score_min=score
        return score_min



def get_action(board_cards=[],hand_cards=['AH', 'KD']):
    if(len(board_cards)+len(hand_cards)==0):
        return 'error'
    
    board = []
    for x in board_cards:
        c = Card.new('{0}{1}'.format(x[0], x[1].lower()))
        board.append(c)
    
    hand = []
    for x in hand_cards:
        c = Card.new('{0}{1}'.format(x[0], x[1].lower()))
        hand.append(c)
    
    score = get_score_by_simulate(hand,board)
    print(score)
    BAD_SCORE = 7000
    BEST_SCORE = 1000
    BETTER_SCORE = 2000
    GOOD_SCORE = 4000
    
    if(len(hand)+len(board)>5 and score>BAD_SCORE):
        action = 'fold'
    else:
        if(score<=BEST_SCORE):
            action = 'all_in'
        elif(score<=BETTER_SCORE):
            action = 'raise_max'
        elif(score>BETTER_SCORE and score<=GOOD_SCORE):
            action = 'raise_min'
        else:
            action = 'call'
    
    return action
    
print( get_action([],hand_cards=['4H', 'AD']) )    
print( get_action(['8H'],hand_cards=['8H', 'KD']) )    
print( get_action(['3D','2H','6c', '8c', '4c'],hand_cards=['7D', '8D']) )    