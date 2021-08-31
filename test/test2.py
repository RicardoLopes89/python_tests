import numpy as np
import matplotlib.pyplot as plt

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # dummy image
    aux = np.linspace(0,10,32)
    A = aux**2
    B = np.zeros((100,32))
    for i in range(100):
        noise = 40*np.random.rand(32)
        B[i,:] = A + noise

    section = B[57:63,:]
    x = np.linspace(0,np.pi/2,32)
    avg_temp = np.average(section,axis=0)

    coefs = np.polyfit(x,avg_temp,2)
    print(coefs)
    aprox_temp = np.polyval(coefs,x)

    plt.scatter(x,avg_temp)
    plt.plot(x,aprox_temp)
    plt.xlabel("angle")
    plt.ylabel("Temperature")
    plt.show()
