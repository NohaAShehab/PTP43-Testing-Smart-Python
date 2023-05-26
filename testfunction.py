import unittest
from errors_exceptions import sumnum


class TestGenerative(unittest.TestCase):
    """Unit tests for the module generative.py"""

    def test_sum_num(self) -> None:
        """
        Verify output of flatten_image for at least three different sizes of images.
        """
        self.assertEqual(sumnum(2,2), 4)
        # self.assertEqual(res, expected_output)

    def test2(self):
        self.assertEqual(sumnum(4,6), 10)






if __name__ == "__main__":
    unittest.main()

