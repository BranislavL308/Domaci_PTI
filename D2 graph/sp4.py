# %% Define
import numpy as np

# %%

# Graf:
# Matrica susjedstva

A = [[0, 2, 3, 0, 0],
     [2, 0, 0, 3, 2],
     [3, 0, 0, 1, 0],
     [0, 3, 1, 0, 1],
     [0, 2, 0, 1, 0]]

v = [-np.inf for i in range(len(A))]
v[-1] = 0


# %% Main

# Poslednji cvor je terminalni
nodes_to_check = [len(A)-1]

while True:
    if len(nodes_to_check) == 0:
        print("Kraj")
        break
    current_node = nodes_to_check.pop()
    neighbours = []
    # Fidns index of all neighbours of current node
    for (i, x) in enumerate(A[current_node]):
        if x >= 1:
            neighbours.append(i)

    for n in neighbours:
        new_value = v[current_node] - A[n][current_node]
        if v[n] >= new_value:
            continue
        else:
            v[n] = new_value
            nodes_to_check.append(n)

print("Najkraci put za graf A  od cvora A do cvora E sa razlicitim cijenama prelaza:")
print(v)

# %%
