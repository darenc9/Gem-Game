# Main Author: Vincent Le
# Main Reviewer: Devon Chan, Foad Ozgoli

from a3_parta import evaluate_board
from a1_partd import get_overflow_list,overflow
from a1_partc import Queue

# This function duplicates and returns the board. You may find this useful
def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board

class GameTree:
    class Node:
        #This function would receive 4 total parameters in order to initalize a node and the current player.
        def __init__(self, board, depth, player, tree_height=4):
            self.board = copy_board(board)
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.children = []
    #This function will receive 3 parameters in order to initalize the currentplayer, make a a copy of the current board, and the root of the node using the tree height. 
    def __init__(self, board, player, tree_height=4):
        self.player = player
        self.board = copy_board(board)
        self.root = self.Node(self.board, 0, self.player, tree_height)
    #This fucntion will calculate all possible moves for the current player. This will return a array of x,y values indicating all of the possible moves on board. 
    def possible_moves(self):
        possible_moves=[]
        rows = len(self.board)
        cols = len(self.board[0])
        for r in range(rows):
            for c in range(cols):
                if self.board[r][c]>=0 and self.player == 1:
                    possible_moves.append((r,c))
                elif self.board[r][c]<=0 and self.player == -1:
                    possible_moves.append((r,c))
        return possible_moves
    #This function will check to the best possible move on the board for the AI to play.
    #This function will loop through all of the current player's possible moves and will calculate the best possible move it could play.
    #This function will return a x,y value indicating the best possible move to play
    def get_move(self):
        height = len(self.board)
        width = len(self.board[0])
        moves = self.possible_moves()
        the_queue = Queue()
        best_play = []
        best_score = None

        for i in range(len(moves)):
            (row, col) = moves[i]
            self.board[row][col] += self.player

            if get_overflow_list(self.board) is not None:
                temp = copy_board(self.board)
                rc = overflow(temp, the_queue)
                queue_len = len(the_queue)
                queue = [the_queue.dequeue() for _ in range(rc)]

                if queue_len != 0:
                    current_score = evaluate_board(queue[-1], self.player)
                    if best_score is None or best_score < current_score:
                        best_play = (row, col)
                        best_score = current_score

            self.board[row][col] -= self.player

        if len(best_play) == 0:
            best_play = moves[0]

        return best_play

    #This function will clear the tree by clearing the root and the root children
    def clear_tree(self):
        self.root.children = []
