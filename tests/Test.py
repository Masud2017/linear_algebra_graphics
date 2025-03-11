import unittest
import logging

class Test(unittest.TestCase):
    def test(self):
        logging.info("Testing the logging")
        self.assertEqual(1,1)