import pandas as pd

points_df = pd.read_csv(r'single_independent_variable_linear_small.csv')


number_of_iterations = 100_000
learning_rate = .001

m = 0
b = 0

for _ in range(number_of_iterations):
    # sum of slopes wrt m
    dm = sum([(2 * x * ((m * x + b) - y)) for x, y in zip(points_df['x'], points_df['y'])])
    # sum of slopes wrt b
    db = sum([(2 * ((m * x + b) - y)) for x, y in zip(points_df['x'], points_df['y'])])

    # update m and b
    m -= learning_rate*dm
    b -= learning_rate*db

print("y = {0}x + {1}".format(m, b))



