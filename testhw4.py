# --------------------------------------------------------------------
# Name: Homework 7
# Purpose: Unit Testing program for homework4.py
#
# Author: Kiwibud
# --------------------------------------------------------------------
"""
The application using Unit Testing to test homework4.py
"""
import unittest
import homework4 as hw4


class TestQ1(unittest.TestCase):
    """
    Test the normal execution of function hottest
    """
    def setUp(self) -> None:
        """Create some dictionaries for testing"""
        self.no_cities = {}
        self.norcal = {'Fresno': 77, 'Napa': 74, 'Palo Alto': 70,
                       'Sacramento': 75, 'San Francisco': 64, 'San Jose': 73,
                       'Oakland': 67, 'Los Altos': 71, 'Mountain View': 72}
        self.unchanged_norcal = {'Fresno': 77, 'Napa': 74, 'Palo Alto': 70,
                       'Sacramento': 75, 'San Francisco': 64, 'San Jose': 73,
                       'Oakland': 67, 'Los Altos': 71, 'Mountain View': 72}


    def test_hottest_empty(self):
        """Test hottest with empty dictionary"""
        self.assertEqual(hw4.hottest(self.no_cities, 6), [])
        # Test if the original dictionary is modified
        self.assertEqual(self.no_cities, {})


    def test_hottest_default(self):
        """Test hottest without specifying integer n"""
        self.assertEqual(hw4.hottest(self.norcal),
                         ['Fresno', 'Sacramento', 'Napa', 'San Jose'])
        # Test if the original dictionary is modified
        self.assertEqual(self.norcal,self.unchanged_norcal)


    def test_hottest_small_n(self):
        """Test hottest with n less than or equal length of dictionary"""
        self.assertEqual(hw4.hottest(self.norcal,2), ['Fresno', 'Sacramento'])
        # Test if the original dictionary is modified
        self.assertEqual(self.norcal, self.unchanged_norcal)
        self.assertEqual(hw4.hottest(self.norcal, 8),
                         ['Fresno','Sacramento','Napa','San Jose',
                          'Mountain View','Los Altos','Palo Alto','Oakland'])
        # Test if the original dictionary is modified
        self.assertEqual(self.norcal, self.unchanged_norcal)


    def test_hottest_big_n(self):
        """Test hottest with n greater than length of dictionary"""
        self.assertEqual(hw4.hottest(self.norcal,20),
                         ['Fresno', 'Sacramento', 'Napa', 'San Jose',
                          'Mountain View', 'Los Altos', 'Palo Alto',
                          'Oakland', 'San Francisco'])
        # Test if the original dictionary is modified
        self.assertEqual(self.norcal, self.unchanged_norcal)


class TestQ2(unittest.TestCase):
    """Test the normal execution of common_words function"""
    def setUp(self):
        """Create some strings for testing"""
        self.string1 = '''Simple is better than     complex and flat 
             is better than nested'''
        self.string2 = '''Complex is  better than complicated 
             and  Sparse is better than dense'''


    def test_common_words_empty_string(self):
        """Test common_words with empty strings"""
        self.assertEqual(hw4.common_words('',''), 0);


    def test_common_words(self):
        """Test common_words with some strings"""
        self.assertEqual(hw4.common_words('Hi Class', 'Hello world'), 0)
        self.assertEqual(hw4.common_words(self.string1, self.string2), 5)


class TestQ3(unittest.TestCase):
    """
    Test the normal execution of function alert
    """
    def setUp(self):
        """Create some dictionaries for testing"""
        self.disney_class = {'Mickey': [78, 50, 100],
                             'Minnie': [88, 65, 99, 70],
                             'Pluto': [70, 49, 87, 66, 38], 'Donald': [40]}
        self.cs122 = {'Alex': [76, 90], 'Diana': [100, 100, 100],
                      'Zoe': [50, 87, 90, 100]}
        self.empty_class = {}
        self.orginal_disney = {'Mickey': [78, 50, 100],
                               'Minnie': [88, 65, 99, 70],
                               'Pluto': [70, 49, 87, 66, 38], 'Donald': [40]}
        self.original_cs122 = {'Alex': [76, 90], 'Diana': [100, 100, 100],
                                'Zoe': [50, 87, 90, 100]}


    def test_alert_empty(self):
        """Test alert with empty dictionary"""
        self.assertEqual(hw4.alert(self.empty_class),set())
        # test if the dictionary unchanged
        self.assertEqual(self.empty_class, {});


    def test_alert(self):
        """Test alert with arbitrary dictionaries"""
        self.assertEqual(hw4.alert(self.disney_class), {'Donald', 'Pluto'})
        self.assertEqual(self.disney_class, self.orginal_disney)
        self.assertEqual(hw4.alert(self.cs122), set())
        self.assertEqual(self.cs122, self.original_cs122)


class TestQ4(unittest.TestCase):
    """
    Test the normal execution of make_password function
    """
    def test_make_password(self):
        """Test make_password with strings"""
        self.assertEqual(hw4.make_password
                        ('Simple is       better than \t complicated'),'SIBTC')
        self.assertEqual(hw4.make_password('python'), 'P')


    def test_make_password_empty_string(self):
        """Test make password with empty string"""
        self.assertEqual(hw4.make_password(''), '')


class TestQ5(unittest.TestCase):
    """
    Test the normal execution of the function extra_credit
    """
    def setUp(self):
        """Create some dictionaries for testing"""
        self.empty_class = {}
        self.cs122 = {'Zoe':90, 'Alex': 93, 'Dan':79, 'Anna':100}


    def test_extra_credit_empty(self):
        """Test extra_credit with empty dictionary"""
        self.assertEqual(hw4.extra_credit(self.empty_class, 5),{})
        self.assertEqual(self.empty_class, {})


    def test_extra_credit(self):
        """Test extra_credit with dictionary"""
        self.assertEqual(hw4.extra_credit(self.cs122),
                         {'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101})
        # check if the updated dictionary
        self.assertEqual(self.cs122,
                         {'Zoe':91, 'Alex': 94, 'Dan':80, 'Anna':101})
        self.assertEqual(hw4.extra_credit(self.cs122, 2),
                         {'Zoe': 93, 'Alex': 96, 'Dan': 82, 'Anna': 103})
        # check if the updated dictionary
        self.assertEqual(self.cs122,
                         {'Zoe': 93, 'Alex': 96, 'Dan': 82, 'Anna': 103})


if __name__ == '__main__':
    unittest.main(verbosity=2)