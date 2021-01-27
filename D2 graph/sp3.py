import numpy as np


# Graph:
# Zadatak sa vise terminalnih cvorova
# Cvorovi se zadaju u listu terminal_nodes_list

# A B C D E F
A = [
    [0, 1, 1, 0, 0, 0],
    [1, 0, 1, 1, 1, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0],
]


v = [-np.inf for i in range(len(A))]

#v[-1] = 0
# Lista terminalnih cvorova
# Terminalni covorovi C i F
terminal_nodes_list = [2, 5]
#terminal_number = len(terminal_nodes_list)


current_term_node = terminal_nodes_list[0]

for current_terminal in terminal_nodes_list:
    v[current_terminal] = 0
    nodes_to_check = [current_terminal]
    while True:
        if len(nodes_to_check) == 0:
            # print("Kraj")
            break
        current_node = nodes_to_check.pop()
        neighbours = []

        for (i, x) in enumerate(A[current_node]):
            if x == 1:
                neighbours.append(i)

        for n in neighbours:
            new_val = v[current_node] - 1
            if v[n] >= new_val:
                continue
            else:
                v[n] = new_val
                nodes_to_check.append(n)

print('Broj terminalnih cvorova 2: C i F')
print('Najkraci put:' + str(v))
