import numpy as np
from matplotlib import pyplot as plt


def estimate_coefs(x, y):
    n = np.size(x)
    x_mean = np.mean(x)
    y_mean = np.mean(y)

    # sum of cross-deviations of y and x
    SSxy = np.sum(y * x) - n * x_mean * y_mean
    # sum of squared deviations of x
    SSxx = np.sum(x * x) - n * x_mean * x_mean
    
    slope = SSxy / SSxx
    y_intercept = y_mean - slope * x_mean

    return slope, y_intercept


def plot_regression(x, y, slope, y_intercept):
    plt.scatter(x, y)

    y_pred = slope * x + y_intercept

    plt.plot(x, y_pred)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.show()


if __name__ == "__main__":
    n = 10
    x = np.array(range(n))
    y = np.random.rand(n)

    slope, y_intercept = estimate_coefs(x, y)
    print(f"slope: {slope}, y_intercept: {y_intercept}")

    a,b = np.polyfit(x, y, 1)
    print("NumPy predicted", a, b) # 2,1

    plot_regression(x ,y, slope, y_intercept)
