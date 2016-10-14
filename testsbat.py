import unittest
import sbat


taskExecuted = "sample task is executed successfully"

def sample_task():
    print "HEJ"

class TestSbat(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(sbat.dependsOn(sample_task), taskExecuted)

if __name__ == '__main__':
    unittest.main()