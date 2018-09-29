import unittest
from unit_tests.test_opera import TestOpera

tc3 = unittest.TestLoader().loadTestsFromTestCase(TestOpera)

# Run unit tests
unitTest = unittest.TestSuite([tc3])

# Execute unit test
unittest.TextTestRunner(verbosity=2).run(unitTest)