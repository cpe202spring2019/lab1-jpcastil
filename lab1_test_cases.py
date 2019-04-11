import unittest
from lab1 import *

class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """Tests for:   Exception is raised when None is inputted as a parameter.
                        Returning None when list is empty
                        Reversing a list of len 1.
                        Reversing a list of len 2. """
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(None)
        self.assertEqual(max_list_iter([]), None)
        self.assertEqual(max_list_iter([0]), 0)
        self.assertEqual(max_list_iter([0,1]), 1)

    def test_reverse_rec(self):
        """Tests for:   Exception is raised when None is inputted as a parameter.
                        Reversing a list of len 1
                        Reversing a list of len 3"""
        with self.assertRaises(ValueError):
            reverse_rec(None)
        self.assertEqual(reverse_rec([1]),[1])
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])

    def test_bin_search(self):
        """Tests for:   Exception is raised when None is inputted as a parameter.
                        Returns None when target is not in input list
                        Returns correct target with even list 
                        Returns correct target with odd list"""
        with self.assertRaises(ValueError):
            bin_search(0,0,1,None)
        self.assertEqual(bin_search(11, 0, len([0,1,2,3,4,5,6,7,8,9,10])-1, [0,1,2,3,4,5,6,7,8,9,10]), None )
        self.assertEqual(bin_search(4, 0, len([0,1,2,3,4,5,6,7,8,9])-1, [0,1,2,3,4,5,6,7,8,9]), 4 )
        self.assertEqual(bin_search(4, 0, len([0,1,2,3,4,5,6,7,8,9,10])-1, [0,1,2,3,4,5,6,7,8,9,10]), 4 )

if __name__ == "__main__":
    unittest.main()

    
