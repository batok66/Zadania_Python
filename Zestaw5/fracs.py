import math
import unittest

# Dla sprawdzenie czy mianownik jest rozny od zera, dla funkcji wykorzystujacych jeden ulamek
def validate1(M):
    if M == 0:
        raise ValueError('Mianownik nie moze byc rowny 0.')

# Dla sprawdzenia czy mianowniki sa rozne od zera, dla fukcji wykorzystujacych dwa ulamki
def validate2(M1, M2):
    if M1 == 0 or M2 == 0:
        raise ValueError('Mianownik nie moze byc rowny 0.')

# Dla sprawdzenia czy mianowniki sa rozne od zera oraz czy licznik2 jest rozny od zera (mnozenie na krzyz) dla dzielania
def validate_div(M1, M2, L2):
    if M1 == 0 or M2 == 0:
        raise ValueError('Mianownik nie moze byc rowny 0.')
    if L2 == 0:
        raise ValueError('Nie mozna dzielic przez 0.')

# Skracanie ulamkow
def reducing_frac(licznik, mianownik):
    if mianownik < 0:
        licznik = -licznik
        mianownik = -mianownik
    nwd = math.gcd(licznik, mianownik)
    return [licznik // nwd, mianownik // nwd]

def add_frac(frac1, frac2):
    L1, M1 = frac1
    L2, M2 = frac2
    validate2(M1, M2)
    licznik = L1 * M2 + L2 * M1
    mianownik = M1 * M2
    return reducing_frac(licznik, mianownik)

def sub_frac(frac1, frac2):
    L1, M1 = frac1
    L2, M2 = frac2
    validate2(M1, M2)
    licznik = L1 * M2 - L2 * M1
    mianownik = M1 * M2
    return reducing_frac(licznik, mianownik)

def mul_frac(frac1, frac2):
    L1, M1 = frac1
    L2, M2 = frac2
    validate2(M1, M2)
    licznik = L1 * L2
    mianownik = M1 * M2
    return reducing_frac(licznik, mianownik)

def div_frac(frac1, frac2):
    L1, M1 = frac1
    L2, M2 = frac2
    validate_div(M1, M2, L2)
    licznik = L1 * M2
    mianownik = M1 * L2
    return reducing_frac(licznik, mianownik)

def is_positive(frac):
    L, M = frac
    validate1(M)
    if L * M > 0: return True
    else: return False

def is_zero(frac):
    L, M = frac
    validate1(M)
    if L == 0: return True
    else: return False

def cmp_frac(frac1, frac2):
    L1, M1 = frac1
    L2, M2 = frac2
    validate2(M1, M2)
    roznica = L1 * M2 - L2 * M1
    if roznica < 0:
        return -1
    elif roznica > 0:
        return 1
    else:
        return 0

def frac2float(frac):
    L, M = frac
    validate1(M)
    return float(L / M)

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([1, 2], [1, 2]), [1, 1])
        self.assertEqual(div_frac([1, 2], [-1, 2]), [-1, 1])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertTrue(is_positive([-1, -2]))
        self.assertFalse(is_positive([-1, 2]))
        self.assertFalse(is_positive([1, -2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 2]))
        self.assertTrue(is_zero([0, -2]))
        self.assertFalse(is_zero([1, 2]))
        self.assertFalse(is_zero([-1, 2]))
        self.assertFalse(is_zero([1, -2]))
        self.assertFalse(is_zero([-1, -2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 3], [1, 2]), -1)
        self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
        self.assertEqual(cmp_frac([1, 2], [-1, 2]), 1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)
        self.assertEqual(frac2float([1, 4]), 0.25)
        self.assertEqual(frac2float([-1, 2]), -0.5)
        self.assertEqual(frac2float([3, 1]), 3.0)
        self.assertEqual(frac2float([0, 1]), 0.0)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()