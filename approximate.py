import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
from djpower_perfect import djpower_pp


def approximate(rate, diff, is_sc):
    if rate <= 90:
        return 0.0
    elif rate > 100:
        return -1

    coeff = djpower_pp(diff, is_sc)

    # maybe there's more segments...
    if rate < 99.5:
        return (0.872179 * norm.cdf(rate, loc=96.4807, scale=1.75853) + 0.129851) * coeff
    else:
        return (0.0668204 * rate - 5.67899) * coeff

if __name__ == '__main__':
    axis = plt.figure().add_subplot()
    x = np.linspace(s := 90.01, e := 100.00, round((e - s) / 0.01))

    for is_sc in range(2):
        for diff in range(1, 16):
            axis.plot(x, [approximate(_x, diff, is_sc) for _x in x], label=f'{'sc' if is_sc else ''}{diff}')

    axis.legend()
    plt.show()
