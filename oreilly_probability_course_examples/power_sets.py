from typing import Set
import numpy as np


def power_sets(s: Set) -> Set:
    A = np.array(list(s))
    result = set([])
    n = A.size
    for i in range(2**n):
        bin_str = np.binary_repr(i, width=n)
        boolean_mask = np.array(list(bin_str), dtype=int) == 1
        result.add(frozenset(A[boolean_mask]))
    return result

if __name__ == '__main__':
    print(power_sets({1, 2, 3}))