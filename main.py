import unittest
from Test.Test.Pages import LoginTest

login_test = unittest.TestLoader().loadTestsFromTestCase(LoginTest)

test_suite = unittest.TestSuite(LoginTest)

unittest.TextTestRunner(verbosity=1).run(test_suite)