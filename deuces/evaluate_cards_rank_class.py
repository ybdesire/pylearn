from deuces import Card
from deuces import Evaluator

# table cards
board = [
    Card.new('Ad'),
    Card.new('Kd'),
    Card.new('Jd')
]

# self cards
hand = [
   Card.new('Qd'),
   Card.new('Td')
]

# evaluate, can only evaluate 5 cards
evaluator = Evaluator()
score = evaluator.evaluate(board, hand)
rank_class = evaluator.get_rank_class(score)
print(rank_class)


rank_class_str = evaluator.class_to_string(rank_class)
print(rank_class_str)


# for score
# Hand strength is valued on a scale of 1 to 7462, 
# where 1 is a Royal Flush and 7462 is unsuited 7-5-4-3-2, 
# as there are only 7642 distinctly ranked hands in poker



# for rank_class
# 1-9
# 9, High Card
# 8, Pair
# 7, Two Pair
# 5, Straight
# 1, Straight Flush