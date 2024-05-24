import numpy as np
from diff_coeff import diff_coeff
import matplotlib.pyplot as plt


def djpower(rate, coeff):
    base = 0.0

    if 90 < rate <= 94.5:
        base = (24 / 135 * np.e ** (8 / 9 * (rate - 95)) + 0.125)
    elif rate < 95.5:
        base = djpower(94.5, 1) + (djpower(95.5, 1) - djpower(94.5, 1)) * (rate - 94.5) + (rate - 94.5) * (rate - 95.5) / 30
    elif rate <= 96:
        base = (24 / 135 * np.e ** (2 / 3 * (rate - 95)) + 0.125)
    elif rate < 96.5:
        base = djpower(96, 1) + 2 * (djpower(96.5, 1) - djpower(96, 1)) * (rate - 96)
    elif rate < 97.5:
        base = (80 / 297 * (np.log(rate - 95) - np.log(5)) + 10 / 11) * (3 * rate - 250.5) / 40
    elif rate < 98:
        base = (80 / 297 * (np.log(rate - 95) - np.log(5)) + 10 / 11) * (rate - 76.5) / 20
    elif rate < 98.5:
        base = (80 / 297 * (np.log(rate - 95) - np.log(5)) + 10 / 11) * (3 * rate - 186.5) / 100
    elif rate < 99:
        base = (80 / 297 * (np.log(rate - 95) - np.log(5)) + 10 / 11) * (rate - 44) / 50
    elif rate < 100:
        base = 8 / 27 * (np.log(rate - 95) - np.log(5)) + 1
    elif rate == 100:
        base = 1

    return base * coeff

axis = plt.figure().add_subplot()
x = np.linspace(s := 90.01, e := 100.00, round((e - s) / 0.01))

for is_sc in range(2):
    for diff in range(1, 16):
        axis.plot(x, [djpower(_x, diff_coeff(diff, is_sc)) for _x in x], label=f'{'sc' if is_sc else ''}{diff}')

axis.legend()
plt.show()
