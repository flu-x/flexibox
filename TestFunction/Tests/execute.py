import unittest

from test_chrome import TestChrome
from test_gecko import TestGecko
from test_opera import TestOpera

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestOpera)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestChrome)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestGecko)

# Execute unit test
if __name__ == "__main__":
    suite = unittest.TestSuite([tc1, tc2, tc3])
    unittest.TextTestRunner(verbosity=2).run(suite)
