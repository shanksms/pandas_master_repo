import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def binomial_trial(n, p = 0.5):
    return sum(np.random.rand(n) <= p)


if __name__ == '__main__':
    N = 10000
    n = 1000
    p = 0.5
    B = np.zeros(N)
    for i in range(N):
        B[i] = binomial_trial(n, p)
    plt.hist(B, density=True, bins=20)
    sns.kdeplot(B, shade=True)
    plt.show()
