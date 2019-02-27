from unittest import TestCase
from task1 import is_leap


class TestTask1(TestCase):

    def setUp(self):
        """Init"""
    def test_is_leap(self):
        """Test for is _prime"""
    self.assertFalse(is_leap(1900))
    self.assertTrue(is_leap(2000))

    def tearDown(self):
        """Finish"""
