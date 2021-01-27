# %% Define environment
import numpy as np
from numpy.core.fromnumeric import argmax
from numpy.random import rand, randint
import matplotlib.pyplot as plt
import random


#TODO:
def environment(a, bandits):
    assert 0 <= a < len(bandits)
    mean, dev = bandits[a]
    return mean + (rand() * 2 - 1) * dev
# %% Decision policy: greedy, eps_greedy and softmax


def greedy(q):
    # # assert len(q) > 0
    # if len(q) == 0:
    #     return -1
    # elif len(q) == 1:
    #     return 0
    # else:
    #     maxval = q[0]
    #     maxindex = 0
    #     for i in range(1, len(q)):
    #         if maxval < q[i]:
    #             maxval = q[i]
    #             maxindex = i
    #     return maxindex
    return np.argmax(q)

# eps = 0.1, 0.5, 0.9
def eps_greedy(q, eps=0.1):
    if rand() < eps:
        # choose random action
        return randint(0, len(q))
    else:
        # choose greedy action
        return greedy(q)

def softmax(q): 
    e_q = np.exp(q - np.max(q)) 
    return e_q / e_q.sum(axis=0) 

def softmax_policy(q):
    prob = softmax(q)
    return np.random.choice(range(len(q)), p = prob)

# %% Learning algorithm

def learn(q, a, r, p = 0.9):
    # q(a)_novo = p * q(a)_staro + (1-p)*r
    assert 0 <= a < len(q)
    q[a] = p * q[a] + (1 - p) * r
    return q.copy()
# %% Generate variable bandits

def generate_bandits():
    g_bandits = [(random.randint(-30,30), 1), (random.randint(-30,30), 10), (random.randint(-30,30), 15), (random.randint(-30,30), 2), (random.randint(-30,30), 3)]
    return g_bandits

# %% Main loop -- Learning & Acting
#   Decision policy: greedy, eps_greedy, softmax

bandits = [(1, 1), (5, 10), (-3, 15), (15, 2), (-24, 3)]
#q = [0 for b in bandits]
q = [1, 5, -3, 15, -24]

actions = []
rewards = []
qs = [q]
a = []

for k in range(1000):
    # body of the main learning loop

    #greedy
    #a = greedy(q)
    
    #eps_greedy
    #a = eps_greedy(q)

    #softmax
    
    a =softmax_policy(q)
    #print(a)
    
    #print(a)
    r = environment(a, bandits)
    q = learn(q, a, r)
    #print(q)
    # logging functions
    actions.append(a)
    rewards.append(r)
    qs.append(q)
    #print(qs)

# actions
plt.plot(actions, ".")
plt.savefig('actions.png')

# rewards
plt.plot(rewards, ".")
plt.savefig('rewards.png') 

# %% Main loop -- Learning & Acting, na svakih 200 koraka menja se bandit


def eps_greedy(q, eps=0.9): # menjamo eps: 0.1,0.5,0.9
    if rand() < eps:
        # choose random action
        return randint(0, len(q))
    else:
        # choose greedy action
        return greedy(q)

q = [1, 5, -3, 15, -24]

actions = []
rewards = []
qs = [q]
a = []

for k in range(1000):
    # body of the main learning loop
    if k in [200, 400, 600, 800]:
        bandits = generate_bandits()
        
    #greedy
    #a = greedy(q)
    
    #eps_greedy
    a = eps_greedy(q)

    #softmax
    #a =softmax_policy(q)
    #print(a)
    
    r = environment(a, bandits)
    q = learn(q, a, r)
    #print(q)

    # logging functions
    actions.append(a)
    rewards.append(r)
    qs.append(q)
    #print(qs)

# actions
plt.plot(actions, ".")
plt.savefig('actions.png')

# rewards
plt.plot(rewards, ".")
plt.savefig('rewards.png')


# %% Plotting

q0 = [q[0] for q in qs]
q1 = [q[1] for q in qs]
q2 = [q[2] for q in qs]
q3 = [q[3] for q in qs]
q4 = [q[4] for q in qs]

plt.plot(q0, "b", label="q0")
plt.plot(q1, "r", label="q1")
plt.plot(q2, "g", label="q2")
plt.plot(q3, "k", label="q3")
plt.plot(q4, "m", label="q4")
plt.legend()

plt.grid()


# %%