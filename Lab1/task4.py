weights = [1, 2, 3, 7]
capacity = 5
"""Data used for the problem."""


def max_weight(c, w):
    """Returns max weight of gold that fits into a knapsack with needed capacity."""

    knapsack = [[0 for i in range(capacity + 1)] for i in range(len(w) + 1)]
    """Matrix that contains calculations for the final answer."""

    for i in range(len(w) + 1):
        for j in range(c + 1):
            if i == 0 or j == 0:
                knapsack[i][j] = 0
            elif w[i - 1] <= j:
                knapsack[i][j] = max(w[i - 1] + knapsack[i - 1][j - w[i - 1]], knapsack[i - 1][j])
            else:
                knapsack[i][j] = knapsack[i - 1][j]
    """Puts different variants of result in places in matrix."""

    return knapsack[len(w)][c]


print(max_weight(capacity, weights))
"""Prints max weight of gold that fits into a knapsack with needed capacity."""
