import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_get_winner_X(self):
        board = [
            ['X', None, 'O'],
            [None, 'X', None],
            [None, 'O', 'X'],
        ]
        self.assertEqual(logic.check_win(board, 'X'), 'X')


        def test_draw(self):
        board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.check_win(board, 'X'), None)
    
    def test_get_winner_O(self):
        board = [
            ['X', 'X', 'O'],
            [None, 'X', 'O'],
            ['X', 'O', 'O'],
        ]
        self.assertEqual(logic.check_win(board, 'O'), 'O')
    

if __name__ == '__main__':
    unittest.main()