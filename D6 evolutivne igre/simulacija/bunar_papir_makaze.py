import matplotlib.pyplot as plt
import numpy as np


xB = [0.2]
xP = [0.3]
xM = [0.5]
dt = 0.005


def simulation(N):

    for i in range(N):

        # dobiti
        u_bunar = xP[i] * -1 + xM[i] * 1
        u_papir = xB[i] * 1 + xM[i] * -1
        u_makaze = xB[i] * -1 + xP[i] * 1
        uAvg = xB[i] * u_bunar + xP[i] * u_papir + xM[i] * u_makaze
        xB.append(xB[i] + (xB[i] * (u_bunar - uAvg)) * dt)
        xP.append(xP[i] + (xP[i] * (u_papir - uAvg)) * dt)
        xM.append(xM[i] + (xM[i] * (u_makaze - uAvg)) * dt)

    return xB, xP, xM


N = 10000
bunar, papir, makaze = simulation(N)
x_axis = np.arange(0, N+1).tolist()

plt.plot(x_axis, bunar, 'g', label='bunar')
plt.plot(x_axis, papir, 'b', label='papir')
plt.plot(x_axis, makaze, 'r', label='makaze')
plt.xlabel("Broj iteracija")

plt.legend(loc='best')
plt.grid()
plt.savefig('bpm.png')
plt.show()
