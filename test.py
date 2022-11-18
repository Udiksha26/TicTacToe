import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_player_winner_0(self):
        board = [
            ['0', None, 'X'],
            [None, '0', None],
            [None, 'X', '0'],
        ]
        self.assertEqual(logic.check_win(board, '0'), '0')


        def test_draw(self):
            board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.check_win(board, 'X'), None)
        
    def test_get_winner_X(self):
        board = [
            ['0', '0', 'X'],
            [None, '0', 'X'],
            ['0', 'X', 'X'],
        ]
        self.assertEqual(logic.check_win(board, 'X'), 'X')
    

if __name__ == '__main__':
    unittest.main()