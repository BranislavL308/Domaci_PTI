# %% Define environment
import numpy as np
import matplotlib.pyplot as plt

# %%
# Cvorovi A B C D E
#
# Susjedni cvorovi cvora A: B i C
# Susjedni covorvi cvora B: E i D
# Susjedni Cvorovi cvora C: A i D
# Susjedni cvorovi cvora D: B i E

# A B C D E
#
# B A A B B
# C D D C D
#   E   E
# Its adjecency matrix (matrica susedstva)
#    A B C D E
# A [0 1 1 0 0]
# B [1 0 0 1 1]
# C [1 0 0 1 0]
# D [0 1 1 0 1]
# E [0 1 0 1 0]

# A je adjecency matrix
A = [[0, 1, 1, 0, 0],
     [1, 0, 0, 1, 1],
     [1, 0, 0, 1, 0],
     [0, 1, 1, 0, 1],
     [0, 1, 0, 1, 0]]
print(len(A))
# V je vektor vrednosti cvorova
v = [-np.inf for i in range(len(A))]
v[-1] = 0  # poslednji element niza ima vrednost 0

# %% Algoritam
# Lista +cvorova koje trebamo proveriti
# Last node is the terminal one !
nodes_to_check = [len(A) - 1]

while True:
    if len(nodes_to_check) == 0:
        break
    # Uzmi poslednji
    current_node = nodes_to_check.pop()  # pop uklanja element i vraca ga
    neighbours = []
    for (i, x) in enumerate(A[current_node]):  # pamtimo index i element niza
        if x == 1:  # da li je taj element = 1 ako jeste dodaj index susjedu
            neighbours.append(i)

    for n in neighbours:
        # new_value = The value that the neighbor would have if this is OK path
        new_value = v[current_node] - 1
        if v[n] >= new_value:
            # if old value better or equal, skip
            continue
        else:
            # if new value better, schedule for checking
            v[n] = new_value
            nodes_to_check.append(n)


# %%
