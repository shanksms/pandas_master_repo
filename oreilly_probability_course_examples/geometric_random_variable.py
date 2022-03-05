import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
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
    sns.set()
    #sns.displot(G)
    plt.hist(G, density=True, bins=100)
    sns.kdeplot(G, shade=True)
    plt.show()





