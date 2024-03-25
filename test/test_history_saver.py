from logic.history_saver import HistorySaver, BoardData

def test_get_board_data():
    board = BoardData(
        width=10,
        height=10,
        bacterias=[(1, 1), (2, 2)],
        foods=[(3, 3), (4, 4)],
        magic_door=(5, 5)
    )

    history_saver = HistorySaver()

    assert history_saver.save_turn(board) is None
    
    result = history_saver.get_turn(0)

    assert result is not board
    assert result.width == board.width
    assert result.height == board.height
    assert result.bacterias == board.bacterias
    assert result.foods == board.foods
    assert result.magic_door == board.magic_door