"""
For the function f(x)=(x-3)**2+4, let’s find the x-value that produces the lowest point of that function.
While we could solve this algebraically, let’s use gradient descent to do it.

"""
import random

def f(x):
    return (x - 3) ** 2 + 4


def d_f(x):
    return 2*(x - 3)


learning_rate = 0.0001
number_of_iterations = 100_000

x = random.randint(-15, 15)
for _ in range(number_of_iterations):
    gradient = d_f(x)
    x -= learning_rate * gradient

print(x)

