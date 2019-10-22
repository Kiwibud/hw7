# ----------------------------------------------------------------------
# Name:     HW7
# Purpose:  Applications of Unit Testing on homework4.py
#
# Author:   Kiwibud
# ----------------------------------------------------------------------
"""

"""
import unittest
import homework4 as hw4


class TestQ1(unittest.TestCase):
    def setUp(self):
        """Create some dictionaries for testing"""
        self.no_cities = {}
        self.norcal = {'Fresno': 77, 'Napa': 74, 'Palo Alto': 70,
                       'Sacramento': 75, 'San Francisco': 64, 'San Jose': 73,
                       'Oakland': 67, 'Los Altos': 71, 'Mountain View': 72}

    def test_hottest_empty(self):
        """Test hottest with empty dictionary"""
        self.assertEqual(hw4.hottest(self.no_cities, 6), [])

    def test_hottest_default(self):
        """Test hottest with default value"""
        self.assertEqual(hw4.hottest(self.norcal), ['Fresno', 'Sacramento',
                                                    'Napa', 'San Jose'])

    def test_hottest_small_n(self):
        """Test hottest with n < dictionary length"""
        self.assertEqual(hw4.hottest(self.norcal, 2), ['Fresno', 'Sacramento'])
        self.assertEqual(hw4.hottest(self.norcal, 8), ['Fresno', 'Sacramento',
                                                       'Napa', 'San Jose',
                                                       'Mountain View',
                                                       'Los Altos',
                                                       'Palo Alto', 'Oakland'])
        self.assertEqual(hw4.hottest(self.norcal, 2), ['Fresno', 'Sacramento'])
        self.assertEqual(self.norcal, {'Fresno': 77, 'Napa': 74,
                                       'Palo Alto': 70, 'Sacramento': 75,
                                       'San Francisco': 64,
                                       'San Jose': 73, 'Oakland': 67,
                                       'Los Altos': 71, 'Mountain View': 72})

    def test_hottest_large_n(self):
        """Test hottest with n > dictionary length"""
        self.assertEqual(hw4.hottest(self.norcal, 20), ['Fresno', 'Sacramento',
                                                        'Napa', 'San Jose',
                                                        'Mountain View',
                                                        'Los Altos',
                                                        'Palo Alto',
                                                        'Oakland',
                                                        'San Francisco'])


class TestQ2(unittest.TestCase):
    def setUp(self):
        """Create some strings for testing"""
        self.string1 = '''Simple is better than     complex and flat 
             is better than nested'''
        self.string2 = '''Complex is  better than complicated 
             and  Sparse is better than dense'''

    def test_common_words_empty_string(self):
        """Test common_words with empty string"""
        self.assertEqual(hw4.common_words('', ''), 0)

    def test_common_words_default(self):
        """Test common_words with default strings"""
        self.assertEqual(hw4.common_words('Hi Class', 'Hello world'), 0)
        self.assertEqual(hw4.common_words(self.string1, self.string2), 5)


class TestQ3(unittest.TestCase):
    def setUp(self):
        """Create some dictionaries for testing"""
        self.disney_class = {'Mickey': [78, 50, 100],
                             'Minnie': [88, 65, 99, 70],
                             'Pluto': [70, 49, 87, 66, 38], 'Donald': [40]}
        self.cs122 = {'Alex': [76, 90], 'Diana': [100, 100, 100],
                      'Zoe': [50, 87, 90, 100]}
        self.empty_class = {}

    def test_alert_empty(self):
        """Test alert with empty class"""
        self.assertEqual(hw4.alert(self.empty_class), set())
        self.assertEqual(self.empty_class, {})

    def test_alert_default(self):
        """Test alert with default values"""
        self.assertEqual(hw4.alert(self.disney_class), {'Donald', 'Pluto'})
        self.assertEqual(self.disney_class, {'Mickey': [78, 50, 100],
                                             'Minnie': [88, 65, 99, 70],
                                             'Pluto': [70, 49, 87, 66, 38],
                                             'Donald': [40]})
        self.assertEqual(hw4.alert(self.cs122), set())
        self.assertEqual(self.cs122, {'Alex': [76, 90],
                                      'Diana': [100, 100, 100],
                                      'Zoe': [50, 87, 90, 100]})


class TestQ4(unittest.TestCase):
    def test_make_password_empty_string(self):
        """Test make_password with empty string"""
        self.assertEqual(hw4.make_password(''), '')

    def test_make_password_default(self):
        """Test make_password with default values"""
        self.assertEqual(hw4.make_password('Simple is       better than \t '
                                           'complicated'), 'SIBTC')
        self.assertEqual(hw4.make_password('python'), 'P')


class TestQ5(unittest.TestCase):
    def setUp(self):
        """Create some dictionaries for testing"""
        self.empty_class = {}
        self.cs122 = {'Zoe': 90, 'Alex': 93, 'Dan': 79, 'Anna': 100}

    def test_extra_credit_empty(self):
        """Test extra_credit with empty dictionary"""
        self.assertEqual(hw4.extra_credit(self.empty_class, 5), {})

    def test_extra_credit_default(self):
        """Test extra_credit with default values"""
        self.assertEqual(hw4.extra_credit(self.cs122), {'Zoe': 91,
                                                        'Alex': 94, 'Dan':
                                                            80, 'Anna': 101})
        self.assertEqual(self.cs122, {'Zoe': 91, 'Alex': 94, 'Dan': 80,
                                      'Anna': 101})
        self.assertEqual(hw4.extra_credit(self.cs122, 2), {'Zoe': 93,
                                                           'Alex': 96,
                                                           'Dan': 82,
                                                           'Anna': 103})
        self.assertEqual(self.cs122, {'Zoe': 93, 'Alex': 96, 'Dan': 82,
                                      'Anna': 103})


if __name__ == "__main__":
    unittest.main(verbosity=2)
