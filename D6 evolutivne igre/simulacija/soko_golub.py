
import matplotlib.pyplot as plt
import numpy as np


# nagrade
V = 30
C = 70

xG = [0.02]
xS = [1 - xG[0]]
dt = 0.03


# funkcije dobiti goluba i sokola
u_golub = [(xG[0] * V/2)]
u_soko = [(xG[0] * V + xS[0] * (V-C)/2) * dt]


def simulation(N):
    # Srednja vrijednost dobiti
    u_avg = [(xG[0] * u_golub[0] + xS[0] * u_soko[0]) * dt]
    for i in range(N):

        # dobiti po iteraciji
        ug_i = (xG[i] * V/2)
        us_i = (xG[i] * V + xS[i] * (V-C)/2)
        u_avg_i = (xG[i] * ug_i + xS[i] * us_i)

        u_golub.append(ug_i*dt)
        u_soko.append(us_i*dt)

        u_avg.append(u_avg_i*dt)

        xG.append(xG[i] + (xG[i] * (ug_i - u_avg_i)) * dt)
        xS.append(xS[i] + (xS[i] * (us_i - u_avg_i)) * dt)
    return xG, xS


# broj iteracija
N = 100
golub, soko = simulation(N)
print('Odnos populacije goluba i sokola u 100 iteraciji:')
print('Golub:' + str(np.round(golub[-1], 5)))
print('Soko:' + str(np.round(soko[-1], 5)))
x_axis = np.arange(0, N+1).tolist()

# print(len(golub))
# print(golub)
plt.plot(x_axis, golub, 'r', label='populacija golubova')
plt.plot(x_axis, soko, 'g', label='populacija sokolova')


plt.legend(loc='best')
plt.xlabel('Broj iteracija')
plt.grid()
plt.savefig('plot.png')
plt.show()
