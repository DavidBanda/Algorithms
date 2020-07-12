from typing import List
import math


def findNLargestNumbers(array: List[float], n: int) -> List[float]:
    """
    >>> findNLargestNumbers([-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7], 5)
    [7, -1, -2, -3, -7]
    >>> findNLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7], 4)
    [541, 141, 18, 17]
    >>> findNLargestNumbers([55, 43, 11, 3, -3, 10], 3)
    [55, 43, 11]
    """

    largest = [-math.inf for _ in range(n)]

    for number in array:

        for i in range(n):

            if largest[i] is None or number > largest[i]:
                    number = swap(largest, number, i)

    return largest


def swap(largest: List[float], number: int, idx: int) -> float:
    oldValue = largest[idx]
    largest[idx] = number
    return oldValue


if __name__ == '__main__':
    import doctest
    doctest.testmod()






