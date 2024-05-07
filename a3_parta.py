# Main Author: Devon Chan
# Main Reviewer: Foad Ozgoli
## Link to video for part c: https://youtu.be/ECgmYb3AEzc?si=EV4ZLeOqXD8Rum6C
# this function is your evaluation function for the board
def evaluate_board(board, player):
    winning_score = 100

    # Check for winner
    if has_won(board, player):
        return winning_score

    # Calculate the score based on the number of pieces on the board
    player_score = sum(cell * (1 if cell > 0 else -1) for row in board for cell in row if abs(cell) > 0 and (cell / abs(cell)) == player)
    return player_score

def has_won(board, player):
    # Check if the board contains only positive numbers for player 1 or negative numbers for player 2
    return (player == 1 and all(cell >= 0 for row in board for cell in row)) or (player == -1 and all(cell <= 0 for row in board for cell in row))
    
