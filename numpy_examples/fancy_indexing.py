import numpy as np

def using_boolean_mask():
    a = np.arange(25).reshape(5, 5)
    # fetch all numbers divisible by 3
    mask = a % 3 == 0
    return a[mask]


def using_index():
    a = np.arange(25).reshape(5, 5)
    # fetch 2, 13, 16, 19
    return a[[0, 2, 3, 3], [2, 3, 1, 4]]



if __name__ == '__main__':
    #print(using_boolean_mask())
    print(using_index())
