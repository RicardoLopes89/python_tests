import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy import interpolate

sns.set(color_codes=True)

if __name__ == '__main__':
    # Camera data
    fig, ax = plt.subplots(1)

    B = pd.read_csv('ladea_caM1_tESTp1.csv', header=None)
    B = B.to_numpy()
    T = pd.read_csv('ladea_caM1_tESTp2.csv', header=None)
    T = T.to_numpy()
    Y = pd.read_csv('ladea_caM1_tESTp3.csv', header=None)
    Y = Y.to_numpy()
    W = pd.read_csv('ladea_caM1_tESTp4.csv', header=None)
    W = W.to_numpy()
    C = np.vstack([B, T, Y, W])

    x = np.linspace(0, (np.pi) / 5, 24)
    xb2 = np.linspace((np.pi) / 5, (2 * np.pi) / 5, 33)
    xb3 = np.linspace((2 * np.pi) / 5, (3 * np.pi) / 5, 30)
    xb4 = np.linspace((3 * np.pi) / 5, (4 * np.pi) / 5, 9)
    xtotal = np.append(x, xb2)
    xtotal = np.append(xtotal, xb3)
    xtotal = np.append(xtotal, xb4)


    coefs = np.polyfit(xtotal, C, 4)
    print(coefs)
    aprox_temp = np.polyval(coefs, xtotal)
    print(aprox_temp)

    # TC data

    c = [82.4, 80.6, 62.4, 42.2, 40.4]
    x1 = np.linspace(0, (4 * np.pi) / 5, 5)
    x_vars = np.linspace(0, (4 * np.pi) / 5, 50)

    InterpolFunc = interpolate.interp1d(x1, c, 'cubic')

    c_vars = InterpolFunc(x_vars)
    coefs_2 = np.polyfit(x_vars, c_vars, 4)
    aprox_temp_2 = np.polyval(coefs_2, x_vars)

    # Plots

    ax.plot(xtotal, aprox_temp)
    plt.xlim(-0.1, ((4 * np.pi) / 5) + 0.1)
    ax.set_xticks(np.arange(0, ((4 * np.pi) / 5) + 0.01, np.pi / 5))
    labels = ['$0$', r'$\pi/5$', r'$2\pi/5$', r'$3\pi/5$', r'$4\pi/5$']
    ax.set_xticklabels(labels)

    #ax.plot(x_vars, aprox_temp_2)
    plt.scatter(xtotal, C,s=20)
    plt.scatter(x1, c)
    #plt.scatter(x_vars, c_vars)

    # plt.xlabel("radius angel")
    # plt.ylabel("Temperature")
    # plt.ylim(30, 90)
    plt.show()
