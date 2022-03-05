import numpy as np
from oreilly_probability_course_examples.bernouli_random_variable import bernoulli_trial


def geometric_trial(p=0.5):
    X = 1
    while True:
        if bernoulli_trial(p):
            return X
        else:
            X += 1


if __name__ == '__main__':
    n = 1000
    p = 0.5
    G = np.zeros(n)
    for i in range(n):
        G[i] = geometric_trial(p)



