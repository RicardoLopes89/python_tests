import numpy as np
import matplotlib.pyplot as plt


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    B = 100 * np.random.rand(100, 32)
    plt.imshow(B)
    plt.show()

    section = B[57:63, :]
    x = np.linspace(0, np.pi / 2, 32)
    avg_temp = np.average(section, axis=0)

    plt.plot(x, avg_temp)
    plt.xlabel("angle")
    plt.ylabel("Temperature")
    plt.show()
