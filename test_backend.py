import backend
import unittest

class TestUserCheck(unittest.TestCase):
    """
    Unit test for the check_user_exists() function from backend.py
    """
    
    def test_num_input(self):
        """
        Checks if function can handle number input
        """
        num = backend.check_user_exists(123)
        
        
        self.assertEqual(num, False)
        
        
    def test_user_exists(self):
        """
        Checks that it properly checks if a user exists
        """
        userThatExists = backend.check_user_exists("ubuntu")
        
        
        self.assertEqual(userThatExists, True)
        
        
    def test_bool_input(self):
        """
        Checks to see if it can handle bool input
        """    
        boolean = backend.check_user_exists(False)
        self.assertEqual(boolean, False)
        
    def test_user_not_exist(self):
        """
        Checks if it returns False when user does not exists
        """
        userThatDoesNotExist = backend.check_user_exists("nope")
        self.assertEqual(userThatDoesNotExist, False)
        
if __name__ == '__main__':
    unittest.main()