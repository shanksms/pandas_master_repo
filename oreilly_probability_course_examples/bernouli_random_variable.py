import numpy as np


def bernoulli_trial(p=0.5):
    # np.random.rand() returns values between 0 and 1 and all values are equally likely.
    # in other words below returns uniformly distributed values.
    """
    p means probability of success.Half of the time, X will be 1.
    It can be thought of tossing a fair coin.
    If some one calls this function with p = 0.7 which means, coin is not fair. In this case,
    Now X will be 1,       70% of the time
    :param p:
    :return:
    """
    X = int(np.random.rand() <= p)
    return X


if __name__ == '__main__':
    count_ones = 0
    count_zeros = 0
    n = 1000000
    p = 0.5
    for _ in range(n):
        if bernoulli_trial(p):
            count_ones += 1
        else:
            count_zeros += 1
    print(count_ones)
    print(count_zeros)
