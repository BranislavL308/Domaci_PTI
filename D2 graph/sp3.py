# %% Define environment

import numpy as np


# %%

# Graph:
# Zadatak sa vise terminalnih cvorova
# Cvorovi se zadaju u listu terminal_nodes_list
# A = [
#    [0, 1, 1, 0, 0],
#    [1, 0, 0, 1, 1],
#    [1, 0, 0, 1, 0],
#    [0, 1, 1, 0, 1],
#    [0, 1, 0, 1, 0]
# ]
A = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
]
print(len(A))
v = [-np.inf for i in range(len(A))]
print(v)
#v[-1] = 0
# Lista terminalnih c
terminal_nodes_list = [0, 5]
current_term_node = terminal_nodes_list[0]
v[current_term_node] = 0

neighbours_list = []


def get_neighbours():
    for k in range(len(A)-1):
        neighbours_1 = []
        for (i, x) in enumerate(A[k]):
            if x == 1:
                neighbours_1.append(i)
        neighbours_list.append(neighbours_1)


get_neighbours()
print(neighbours_list)


# %%

# Last node is the terminal one!!!!
nodes_to_check = [len(A) - 1]
print(nodes_to_check)

while True:

    if len(nodes_to_check) == 0:
        break

    current_node = nodes_to_check.pop()
    print(current_node)
    # ---
    # Finds indices of all neighbours of current node
    neighbours = []

    for (i, x) in enumerate(A[current_node]):
        if x == 1:
            neighbours.append(i)

    # print(neighbours)

    # ---
    for n in neighbours:
        # new_value = The value that the neighbor
        # would have if this is OK path
        new_value = v[current_node] - 1
        if v[n] >= new_value:
            # If old value batter or equal, skip
            continue
        else:
            # If new value better, schedule for checking
            v[n] = new_value
            nodes_to_check.append(n)

# print(v)
# %% provjera
# print(neighbours_list)
# print(v)

# %%


def shortetst_path(start_node, end_node):
    current_node = start_node

    s_path = [start_node]
    while(current_node != end_node):

        val_list = []
        # check neighbours values of start_node
        # neighbour with better value is next_node

        n = neighbours_list[current_node]

        for i in range(len(n)):
            neigh = n[i]
            val_list.append(v[neigh])
            best = np.argmax(val_list)
            # print(best)
            current_node = n[best]

            if current_node == end_node:
                print("Kraj")
                break
        s_path.append(current_node)
        # print(current_node)
        # print(val_list)
        # print(current_node)
    print(s_path)


#shortetst_path(1, 5)


# %% # Test
shortetst_path(1, 5)
print(v)

# %%
