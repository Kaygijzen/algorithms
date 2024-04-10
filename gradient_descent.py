import numpy as np
import matplotlib.pyplot as plt

def func(x): return x ** 2

def grad(x): return 2 * x


if __name__ == '__main__':
    budget = 1000
    lr = 0.05
    threshold = 0.1 # threshold for convergence

    X = [x for x in range(-100, 101)]
    Y = [func(x) for x in range(-100, 101)]

    fig = plt.figure() 
    plt.plot(X, Y, label="f(x)")   
    plt.xlabel("x")
    plt.ylabel("f(x)")

    # x_0 and y_0
    sign = (1 if np.random.random() < 0.5 else -1)
    x = sign * np.random.uniform(80, 90)
    y = func(x)

    print("x_0 =", x, "y_0 =", y)
    plt.plot(x, y, "go", label="initial point")

    while budget > 0 and y > threshold:
        budget -= 1

        # update x by preforming gradient descent
        x -= lr * grad(x)
        y = func(x)

        plt.plot(x, func(x), 'ro')

    print("remaining budget:", budget)    

    plt.legend()
    plt.show() 