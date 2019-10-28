from unittest import TestCase

from parameterized import parameterized

from ex_11_check_primality_functions import is_prime


class Tests(TestCase):

    @parameterized.expand([
        (1,),
        (2,),
        (3,),
        (5,),
        (7,),
        (19,),
        (31,)
    ])
    def test_if_prime_number_returns_true(self, number):
        self.assertTrue(is_prime(number))

    @parameterized.expand([
        (-3,),
        (0,),
        (4,),
        (10,),
        (27,),
        (45,),
        (63,)
    ])

    def test_if_non_prime_number_returns_false(self, number):
        self.assertFalse(is_prime(number))
