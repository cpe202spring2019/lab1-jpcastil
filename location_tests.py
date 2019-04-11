import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        """Tests for:   Repr returns correct information in format"""
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
    
    def test_eq(self):  
        """Tests for:   __eq__ function works as expected with different cities
                        __eq__ function doesn't equate different cities"""
        self.assertEqual(Location("SLO", 35.3, -120.7), Location("SLO", 35.3, -120.7))
        self.assertEqual(Location("Paris", 48.9, 2.4), Location("Paris", 48.9, 2.4))
        self.assertNotEqual(Location("Paris", 48.9, 2.4), Location("SLO", 35.3, -120.7))
        
    
if __name__ == "__main__":
    unittest.main()
