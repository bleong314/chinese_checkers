from checker_map import ChineseCheckersBoard
from Point import Point

def jump_loop_test() -> None:
    red_positions = [[12, 0, "Red"], [13, 1, "Red"], [15, 3, "Red"], [15, 5, "Red"], [13, 5, "Red"], [13, 3, "Red"]]
    yellow_positions = [[9, 3, "Yellow"]]
    positions = red_positions + yellow_positions
    game = ChineseCheckersBoard([2, ["Yellow", "Red"], 1, positions])
    # Assuming that moves are counted correctly under the loop, we should have 26 
    for move in game.valid_player_moves(game.player_4):
        print(move)
    assert len(game.valid_player_moves(game.player_4)) == 29, "Jump Loop Test Failed!"
    print("Jump Loop Test Passed!")
    
def swapping_test_2p() -> None:
    """
    Determines if we able to make any swaps when we have two players
    """
    red_positions = [[8, 12, "Red"], [10, 14, "Red"], [11, 15, "Red"], [12, 16, "Red"], [11, 13, "Red"], [12, 14, "Red"], [13, 15, "Red"], [13, 13, "Red"], [14, 14, "Red"], [15, 13, "Red"]]
    yellow_positions = [[9, 13, "Yellow"]]
    positions = red_positions + yellow_positions
    game = ChineseCheckersBoard([2, ["Yellow", "Red"], 1, positions])
    # s = game.output_gamestate()
    # game = ChineseCheckersBoard(s)
    # game.display_board()
    for move in game.valid_player_moves(game.player_4):
        if move[1][0] == "S":
            print(move)

def swapping_test_6p() -> None:
    """
    Determines if we are able to make any swaps when we have six players
    """
    red_endzone_positions = [[8, 12, "Red"], [11, 15, "Red"], [11, 13, "Red"], [12, 14, "Red"], [13, 15, "Red"], [13, 13, "Red"]]
    red_remaining_positions = [[5, 9, "Red"], [8, 4, "Red"], [18, 10, "Red"], [18, 6, "Red"]]
    yellow_positions = [[9, 13, "Yellow"]] 
    green_positions = [[10, 14, "Green"]]
    blue_positions = [[12, 16, "Blue"]]
    orange_positions = [[14, 14, "Orange"]]
    purple_positions = [[15, 13, "Purple"]]
    positions = red_endzone_positions + red_remaining_positions + yellow_positions + green_positions + blue_positions + orange_positions + purple_positions
    game = ChineseCheckersBoard([6, ["Red", "Yellow", "Green", "Blue", "Orange", "Purple"], 1, positions])
    valid_swap_moves = [move for move in game.valid_player_moves(game.player_4) if move[1][0] == "S"]
    for swap in valid_swap_moves:
        print(swap)
    assert len(valid_swap_moves) == 11, "Six Player Swap Test Failed!"
    print("Six Player Swap Test Passed!")

def no_swap_test() -> None:
    """
    We should have no swaps allowed if there is an empty spot in the endzone
    """
    red_positions = [[8, 12, "Red"], [10, 14, "Red"], [11, 15, "Red"], [11, 13, "Red"], [12, 14, "Red"], [13, 15, "Red"], [13, 13, "Red"], [14, 14, "Red"], [15, 13, "Red"]]
    yellow_positions = [[9, 13, "Yellow"]]
    positions = red_positions + yellow_positions
    game = ChineseCheckersBoard([2, ["Yellow", "Red"], 1, positions])
    valid_swap_moves = [move for move in game.valid_player_moves(game.player_4) if move[1][0] == "S"]
    assert len(valid_swap_moves) == 0, "No Swap Test Failed!"
    print("No Swap Test Passed!")

if __name__ == "__main__":
    #jump_loop_test()
    #swapping_test_2p()
    swapping_test_6p()
    #no_swap_test()
    # game.display_board()
    # game.play_game()