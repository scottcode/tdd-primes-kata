import unittest
from tdd.primes import generate_prime_factors


class TestPrimes(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEquals((1,), generate_prime_factors(1))

    def test_2(self):
        self.assertEquals((1,2), generate_prime_factors(2))

    def test_3(self):
        self.assertEquals((1, 3), generate_prime_factors(3))


if __name__ == '__main__':
    unittest.main()