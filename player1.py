# In this file you will find the player class for player 1.
# You may add additional smarts if you wish... but just using the game tree once it is properly created is fine

from a3_partb import GameTree

class PlayerOne:

    def __init__(self, name = "P1 Bot"):
        self.name = name
        self.difficulty = 4
        
    def get_name(self):
        return self.name

    # Sets game difficulty
    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def get_play(self, board):
        # Generates GameTree with specified difficulty
        tree = GameTree(board, 1, self.difficulty)
        (row,col) = tree.get_move()
        return (row,col)