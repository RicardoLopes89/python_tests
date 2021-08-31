import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


if __name__ == '__main__':
    # dummy image
    B = pd.read_csv('LADEA_RUN1 - Copy.csv')
    B = B.to_numpy()
    print(B)
    x = np.linspace(0, (4 * np.pi) / 5, 75)
    print(x)
    coefs = np.polyfit(x, B, 4)

    aprox_temp = np.polyval(coefs, x)


    plt.scatter(x, B)
    plt.plot(x, aprox_temp)
    plt.xlabel("radius angel")
    plt.ylabel("Temperature")
    plt.ylim(30, 90)
    plt.show()
