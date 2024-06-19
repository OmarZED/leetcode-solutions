import unittest
import pytest

from Solution import Solution
class TestSolution(unittest.TestCase):


    def setUp(self):
        """Set up the solution instance before each test."""
        self.solution = Solution()
    def test_empty_matrix(self):
        """Test case for an empty matrix and a matrix with an empty row."""
        self.assertEqual(self.solution.longestIncreasingPath([]), 0)
        self.assertEqual(self.solution.longestIncreasingPath([[]]), 0)

    def test_single_element_matrix(self):
        """Test case for a matrix with a single element."""
        self.assertEqual(self.solution.longestIncreasingPath([[1]]), 1)

    def test_increasing_path(self):
        """Test case for a matrix with a known increasing path length."""
        matrix = [
            [9, 9, 4],
            [6, 6, 8],
            [2, 1, 1]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 4)

    def test_decreasing_path(self):
        """Test case for a matrix with a different known increasing path length."""
        matrix = [
            [3, 4, 5],
            [3, 2, 6],
            [2, 2, 1]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 4)

    def test_no_increasing_path(self):
        """Test case for a matrix where all elements are the same."""
        matrix = [
            [7, 7, 7],
            [7, 7, 7],
            [7, 7, 7]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 1)

    def test_large_matrix(self):
        """Test case for a larger matrix with a more complex path."""
        matrix = [
            [1, 2, 3, 4, 5],
            [16, 17, 18, 19, 6],
            [15, 24, 25, 20, 7],
            [14, 23, 22, 21, 8],
            [13, 12, 11, 10, 9]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 25)

    def test_disjoint_increasing_paths(self):
        """Test case for a matrix with multiple disjoint increasing paths."""
        matrix = [
            [1, 2, 6],
            [5, 3, 7],
            [4, 6, 8]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 6)

    def test_diagonal_increase(self):
        """Test case for a matrix where the longest path is diagonal."""
        matrix = [
            [1, 2, 3],
            [6, 5, 4],
            [7, 8, 9]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)

    def test_multiple_paths_same_length(self):
        """Test case for a matrix with multiple paths of the same maximum length."""
        matrix = [
            [1, 2, 3],
            [2, 3, 4],
            [3, 4, 5]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)

    def test_row_wise_increasing(self):
        """Test case for a matrix with all elements increasing row-wise."""
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)

    def test_column_wise_increasing(self):
        """Test case for a matrix with all elements increasing column-wise."""
        matrix = [
            [1, 4, 7],
            [2, 5, 8],
            [3, 6, 9]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)

    def test_random_values(self):
        """Test case for a matrix with random values to test general performance."""
        matrix = [
            [9, 6, 3],
            [7, 1, 8],
            [2, 4, 5]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)

    def test_negative_numbers(self):
        """Test case for a matrix with only negative numbers."""
        matrix = [
            [-9, -6, -3],
            [-7, -1, -8],
            [-2, -4, -5]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 4)

    def test_mix_negative_positive(self):
        """Test case for a matrix with a mix of negative and positive numbers."""
        matrix = [
            [-1, 2, -3],
            [4, -5, 6],
            [-7, 8, -9]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 4)

    def test_large_performance(self):
        """Test case for a larger matrix to test efficiency and performance."""
        matrix = [
            [i for i in range(100)]
            for _ in range(100)
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 100)

    def test_single_row(self):
        """Test case for a matrix with a single row."""
        matrix = [
            [1, 2, 3, 4, 5]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)

    def test_single_column(self):
        """Test case for a matrix with a single column."""
        matrix = [
            [1],
            [2],
            [3],
            [4],
            [5]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)

    def test_same_negative_numbers(self):
        """Test case for a matrix with all elements being the same negative number."""
        matrix = [
            [-1, -1, -1],
            [-1, -1, -1],
            [-1, -1, -1]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 1)

    def test_descending_order(self):
        """Test case for a matrix with elements in descending order."""
        matrix = [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 1)

    def test_peaks_and_valleys(self):
        """Test case for a matrix with multiple peaks and valleys."""
        matrix = [
            [5, 1, 6],
            [2, 9, 3],
            [7, 4, 8]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)

    def test_very_large_numbers(self):
        """Test case for a matrix with very large numbers."""
        matrix = [
            [100000, 100001, 100002],
            [99999, 100003, 100004],
            [99998, 100005, 100006]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)

    def test_very_small_numbers(self):
        """Test case for a matrix with very small numbers (close to zero)."""
        matrix = [
            [0.1, 0.2, 0.3],
            [0.0, 0.4, 0.5],
            [-0.1, 0.6, 0.7]
        ]
        self.assertEqual(self.solution.longestIncreasingPath(matrix), 5)

if __name__ == "__main__":
    unittest.main()