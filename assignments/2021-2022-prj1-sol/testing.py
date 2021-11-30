import unittest
from algorithms_max_sub_array import (
    brute_force,
    prefix_sums,
    kadane,
    prefix_sums_table_generator,
    kadane_table_generator,
)


class MyTestCase(unittest.TestCase):
    # test brute force method
    def test_brute_force(self):
        self.assertEqual(brute_force([2, 13, 18, -22, -12]), (33, 0, 2))
        self.assertEqual(brute_force([0, -10, -3, 4, -10, 7]), (7, 5, 5))
        self.assertEqual(brute_force([90, -10, 20, 4, -10, 7]), (104, 0, 3))

    # test prefix table generation
    def test_prefix_table_generation(self):
        self.assertEqual(
            prefix_sums_table_generator([2, 13, 18, -22, -12]), [2, 15, 33, 11, -1]
        )
        self.assertEqual(
            prefix_sums_table_generator([0, -10, -3, 4, -10, 7]),
            [0, -10, -13, -9, -19, -12],
        )
        self.assertEqual(
            prefix_sums_table_generator([90, -10, 20, 4, -10, 7]),
            [90, 80, 100, 104, 94, 101],
        )

    # test prefix method
    def test_prefix(self):
        self.assertEqual(prefix_sums([2, 13, 18, -22, -12]), (33, 0, 2))
        self.assertEqual(prefix_sums([0, -10, -3, 4, -10, 7]), (7, 5, 5))
        self.assertEqual(prefix_sums([90, -10, 20, 4, -10, 7]), (104, 0, 3))

    # test kadane table generation
    def test_kadane_table_generation(self):
        self.assertEqual(
            kadane_table_generator([2, 13, 18, -22, -12]), [2, 15, 33, 11, 0]
        )
        self.assertEqual(
            kadane_table_generator([0, -10, -3, 4, -10, 7]),
            [0, 0, 0, 4, 0, 7],
        )
        self.assertEqual(
            kadane_table_generator([90, -10, 20, 4, -10, 7]),
            [90, 80, 100, 104, 94, 101],
        )

    # test kadane method
    def test_kadane(self):
        self.assertEqual(kadane([2, 13, 18, -22, -12]), (33, 0, 2))
        self.assertEqual(kadane([0, -10, -3, 4, -10, 7]), (7, 5, 5))
        self.assertEqual(kadane([90, -10, 20, 4, -10, 7]), (104, 0, 3))


if __name__ == "__main__":
    unittest.main()
