# leetcode-solutions
This repository contains solutions to LeetCode problems and their corresponding unit tests.

## Solution: Longest Increasing Path in a Matrix

### Problem Statement
Given an integer matrix, find the length of the longest increasing path. From each cell, you can either move to four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

### Solution Explanation
The solution uses dynamic programming with memoization to efficiently find the longest increasing path starting from each cell. The memoization table (`dp`) stores the length of the longest increasing path for each cell to avoid redundant calculations.

### Testing Techniques
- **Boundary Testing**: Ensures the solution handles edge cases like empty matrices or single-element matrices.
- **Path Testing**: Tests various paths in the matrix, including straight, diagonal, and complex paths.
- **Stress Testing**: Evaluates the performance and efficiency of the solution with larger matrices.
- **Negative Testing**: Includes matrices with negative numbers to ensure the solution correctly handles them.
