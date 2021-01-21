# %% Define environment

import numpy as np


# %%

# Graph:
# Matrica susjedstva za usmjerene grafove
A = [[0, -1, 1, 0, 0],
     [1, 0, 0, -1, 1],
     [-1, 0, 0, 1, 0],
     [0, 1, -1, 0, 1],
     [0, -1, 0, -1, 0]]


print(len(A))
v = [-np.inf for i in range(len(A))]
print(v)
v[-1] = 0


neighbours_list = []


def get_neighbours():
    for k in range(len(A) - 1):
        neighbours_1 = []
        for (i, x) in enumerate(A[k]):
            # Mozemo se kretati samo u pozitivnom smijeru
            if x == 1:
                neighbours_1.append(i)
        neighbours_list.append(neighbours_1)


get_neighbours()
print(neighbours_list)


# %%

# Poslednji cvor je terminalni
# get value of node
def get_val():
    nodes_to_check = [0]
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
            if x == -1:
                neighbours.append(i)
        print(neighbours)

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


get_val()

print(v)
# %%
print(neighbours_list)
print(v)

# %%
# Funkciji shortetst_path() prosledjujemo pocetni i krajni cvor


def shortetst_path(start_node_index, end_node):
    current_node = start_node_index
    #end_node = 4
    s_path = [start_node_index]
    while(current_node != end_node):

        val_list = []
        # check neighbours values of start_node_index
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


shortetst_path(0, 4)


# %%
