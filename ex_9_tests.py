from unittest import TestCase
from unittest.mock import Mock, patch

from ex_9_guess_number import *


class Tests(TestCase):

    def setUp(self):
        self.player = Mock()
        self.game = Game(self.player)

    def test_min_number_is_one(self):
        result = min([self.game.choose_random_number() for y in range(50)])
        self.assertEqual(1, result)

    def test_max_number_is_nine(self):
        result = max([self.game.choose_random_number() for x in range(50)])
        self.assertEqual(9, result)

    # @patch('ex_9_guess_number.Game.choose_random_number', return_value=2)
    # def test_randomized_number_is_passed(self, mock_choose_random_number):
    #     self.game.play()
    #     self.assertEqual(self.game.random_number, 2)

    # def test_user_number_is_passed(self):
    #     self.player.guess.return_value = 5
    #     self.game.play()
    #     self.assertEqual(self.game.user_number, 5)

    def test_whether_check_function_with_the_same_numbers_is_zero(self):
        self.game.random_number = 4
        self.game.user_number = 4
        self.assertEqual(0, self.game.check())

    def test_whether_check_function_with_user_number_one_and_random_number_four_gives_minus_three(self):
        self.game.random_number = 4
        self.game.user_number = 1
        self.assertEqual(-3, self.game.check())

    def test_whether_check_function_with_user_number_nine_and_random_number_four_gives_five(self):
        self.game.random_number = 4
        self.game.user_number = 9
        self.assertEqual(5, self.game.check())


