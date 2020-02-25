import unittest

from regressiontest.test_chromeremote import Test_chromeremote
from regressiontest.test_firefoxremote import Test_firefoxremote
from unittests.test_chrome import TestChrome
from unittests.test_gecko import TestGecko
from unittests.test_opera import TestOpera

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestOpera)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestChrome)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestGecko)
tc4 = unittest.TestLoader().loadTestsFromTestCase(Test_chromeremote)
tc5 = unittest.TestLoader().loadTestsFromTestCase(Test_firefoxremote)

# Execute unit test
if __name__ == "__main__":
    # suite = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])
    suite = unittest.TestSuite([tc5])
    unittest.TextTestRunner(verbosity=2).run(suite)
