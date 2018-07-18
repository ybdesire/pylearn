from deuces import Card
from deuces import Evaluator

# table cards
board = [
    Card.new('Ah'),
    Card.new('Kd'),
    Card.new('Jc'),
    Card.new('2d'),
    Card.new('3c'),
]

# self cards
hand = [
   Card.new('Qs'),
   Card.new('Th')
]

# evaluate
evaluator = Evaluator()
score = evaluator.evaluate(board, hand)

print(score)

# Hand strength is valued on a scale of 1 to 7462, 
# where 1 is a Royal Flush and 7462 is unsuited 7-5-4-3-2, 
# as there are only 7642 distinctly ranked hands in poker



