import unittest
from unit_tests.test_opera import TestOpera
from unit_tests.test_chrome import TestChrome
from unit_tests.test_gecko import TestGecko

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestOpera)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestChrome)
tc3 = unittest.TestLoader().loadTestsFromTestCase(TestGecko)

# Run unit tests
unitTest = unittest.TestSuite([tc1, tc2, tc3])

# Execute unit test
unittest.TextTestRunner(verbosity=2).run(unitTest)