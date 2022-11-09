import unittest
import logic


class TestLogic(unittest.TestCase):

    def test_is_player_win(self):
        board = [
            ['O', None, 'X'],
            [None, 'O', None],
            [None, 'X', 'O'],
        ]
        self.assertEqual(logic.checking_winner(board, 'O'), 'O')
    
    def test_draw(self):
        board = [
            ['X', 'O', 'O'],
            ['O', 'X', 'X'],
            ['X', 'O', 'O'],
        ]
        self.assertNotEqual(logic.checking_winner(board, 'X'), 'X')
        self.assertEquals(logic.checking_winner(board, 'X'), None)

    def test_is_player_win_O(self):
        board = [['O', 'O', 'X'],
                [None, 'O', 'X'],
                ['O', 'X', 'X'],]
        self.assertEqual(logic.checking_winner(board, 'X'), 'X')

if __name__ == '__main__':
    unittest.main()