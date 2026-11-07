import unittest

from game import GUN, SNAKE, WATER, decide_winner


class TestDecideWinner(unittest.TestCase):
    def test_draws(self):
        for choice in (SNAKE, WATER, GUN):
            self.assertEqual(decide_winner(choice, choice), "draw")

    def test_player_wins(self):
        self.assertEqual(decide_winner(SNAKE, WATER), "win")  # snake drinks water
        self.assertEqual(decide_winner(WATER, GUN), "win")    # water drowns gun
        self.assertEqual(decide_winner(GUN, SNAKE), "win")    # gun shoots snake

    def test_player_loses(self):
        self.assertEqual(decide_winner(WATER, SNAKE), "lose")
        self.assertEqual(decide_winner(GUN, WATER), "lose")
        self.assertEqual(decide_winner(SNAKE, GUN), "lose")


if __name__ == "__main__":
    unittest.main()
