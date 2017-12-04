import backend
import unittest
import getpass

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
		Checks that it properly checks if a user exists.
		Checks against current user using getpass.getuser()
		"""
		current_user = getpass.getuser()
		userThatExists = backend.check_user_exists(current_user)

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
        

class TestPasswdCheck(unittest.TestCase):
    """
    Unit test for the check_user_password_set() function from backend.py
    """

    def test_num4username(self):
        """
        Checks if function can handle number input for username.
        """
        num = backend.check_user_password_set(123)

        self.assertEqual(num, False)

    def test_root4passwd(self):
        """
        Checks if it returns False when running against root.
        Root should not have a password.
        """
        root = backend.check_user_password_set("root")

        self.assertEqual(root, False)

    def test_user4passwd(self):
        """
        Checks if it returns True for current user.
        Assumes current user has a password.
        """
        current_user = getpass.getuser()
        check_yourself = backend.check_user_password_set(current_user)

        self.assertEqual(check_yourself, True)


class TestPasswdPolicy(unittest.TestCase):
    """
    Unit test for the check_password_policy() function from backend.py
    Tester will need to check against their password policy to run test returning True.
    """

    def test_num4variables(self):
        """
        Checks if function properly runs with int variables.
        """
        num_vars = backend.check_password_policy(0, 0, 0, 0)

        self.assertEqual(num_vars, False)

    def test_str4variables(self):
        """
        Checks if function properly handles string input.
        Return False for anything not the password policy.
        """
        str_vars = backend.check_password_policy('the', 'best', 'tests', 'ever')

        self.assertEqual(str_vars, False)


class TestSudoUserPasswd(unittest.TestCase):
    """
    Unit test for the check_sudo_user_password() function from backend.py
    Tester will need to check against their /etc/sudoers.
    Assumed that you require passwords.
    """

    def test_needPasswd4Sudo(self):
        """
        Verifies current sudoers need a password to use sudo.
        """

        self.assertEqual(backend.check_sudo_user_password(), True)

        
if __name__ == '__main__':
    unittest.main()
