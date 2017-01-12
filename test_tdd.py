import unittest
from tdd.primes import generate_prime_factors


class TestPrimes(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_1(self):
        self.assertEquals((), generate_prime_factors(1))

    def test_2(self):
        self.assertEquals((2,), generate_prime_factors(2))

    def test_3(self):
        self.assertEquals((3,), generate_prime_factors(3))

    def test_4(self):
        self.assertEquals((2, 2), generate_prime_factors(4))

    def test_6(self):
        self.assertEquals((2, 3), generate_prime_factors(6))

    def test_7(self):
        self.assertEquals((7,), generate_prime_factors(7))

    def test_8(self):
        self.assertEquals((2,2,2), generate_prime_factors(8))

    def test_9(self):
        self.assertEquals((3,3), generate_prime_factors(9))

    def test_10(self):
        self.assertEquals((2,5), generate_prime_factors(10))

    def test_16(self):
        self.assertEquals((2, 2, 2, 2), generate_prime_factors(16))

    def test_25(self):
        self.assertEquals((5, 5), generate_prime_factors(25))

    def test_49(self):
        self.assertEquals((7, 7), generate_prime_factors(49))

    def test_45(self):
        self.assertEquals((3, 3, 5), generate_prime_factors(3*3*5))

    def test_9889(self):
        self.assertEquals((11, 29, 31), generate_prime_factors(11*31*29))


if __name__ == '__main__':
    unittest.main()
