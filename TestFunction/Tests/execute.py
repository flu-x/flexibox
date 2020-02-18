import unittest

from test_chrome import TestChrome
from test_chromeregress import Test_chromeregress
from test_firefoxregress import Test_firefoxregress
from test_gecko import TestGecko
from test_opera import TestOpera

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestOpera)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestChrome)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestGecko)
tc4 = unittest.TestLoader().loadTestsFromTestCase(Test_chromeregress)
tc5 = unittest.TestLoader().loadTestsFromTestCase(Test_firefoxregress)

# Execute unit test
if __name__ == "__main__":
    suite = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])
    unittest.TextTestRunner(verbosity=2).run(suite)
