# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 13:51:27 2020

To test the class and functions
"""
import unittest
import Sample_Test as s

class TestAdd(unittest.TestCase):
    """
    Testing Sample_Test module
    
    Test runner observes the code and find out the method starts with test.
    It will be run those methods alone when test class main() gets called.
    Each test case should have atleast one assert statement
    """
    
    def test_add_integers(self):
        self.assertEqual(s.add(4,5), 9)
        return
    
    def test_add_integers(self):
        self.assertEqual(s.add(4,5), 19)
        return
    
    def test_add_float(self):
        result = s.add(4,1.5)
        self.assertEqual(result, 5.5)
        return
    
    def test_add_strings(self):
        self.assertEqual(s.add('ab','cd'), 'abcd')
        return


"""
__main__ will be entry point if it is defined in a class. 
Compiler looks for __main__. If found, it will run __main__ first.
"""    
if __name__ == "__main__":
    unittest.main()
   
"""
unittest.main() will run without main function also. But that is not a right way.
If this file is imported into another file, if main is defined, it won't trigger the test cases.
If main is not there, by default it(unittest.main()) will call all the testt cases.
"""