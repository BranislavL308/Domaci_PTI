# %%
from math import sqrt
import matplotlib.pyplot as plt
dr = 90
dc = 50


# agent info lista
# prvi element: cilj
# drugi element: pocetna pozicija
# treci element: max brzina
# cetvrti elemet: id letjelice
agents_info = [[[350, 350], [50, 50], 12, 0],
               [[350, 50], [50, 350], 10, 1]]


def get_aircraf_id(agents_info):
    id_list = []
    for i in range(0, len(agents_info)):
        agents_info[i][3]
        id_list.append(agents_info[i][3])
    return id_list


def destination(agents_info):
    dest_list = []
    for i in range(0, len(agents_info)):
        agents_info[i][0]
        dest_list.append(agents_info[i][0])
    return dest_list


def get_velocity(agent_info):
    vel_list = []
    for i in range(0, len(agents_info)):
        agents_info[i][2]
        vel_list.append(agents_info[i][2])
    return vel_list


# print(get_aircraf_id(agents_info))

# agents_info[0][1] = 10
# Pocena vrednost istorije je pocetna pozicija letjelice
position_history = [[agents_info[0][1], agents_info[1][1]]]


# position_history.append([[150, 100], [-20, -100]])
# print(agents_info)


def get_current_possition():
    return position_history[-1]

# %%


# current_pos_x = []
# current_pos_x.append(curent_pos[0][0])

def collision_check(colision_distance, dr):

    a_i, a_j = 0, 0
    temp_pos = get_current_possition()
    destinations = destination(agents_info)
    vel_val = get_velocity(agents_info)
    x_current, y_current = temp_pos[0][0], temp_pos[0][1]
    x_j, y_j = temp_pos[1][0], temp_pos[1][1]
    print(x_j, y_j)
    V = sqrt(pow(x_j - x_current, 2) + pow(y_j - y_current, 2))
    print(V)

    distance_ij_X, distance_ij_Y = x_j - x_current, y_j - y_current
    V = sqrt(pow(distance_ij_X, 2) + pow(distance_ij_Y, 2))
    max_function = max(
        (pow(dr, 2) - pow(V, 2)) / (pow(V, 2) - pow(dc, 2)), 0)

    a_i, a_j = a_i + distance_ij_X * max_function, a_j + distance_ij_Y * max_function

    distance_from_dest_x, distance_from_dest_y = destinations[0][0] - \
        x_current, destinations[0][1] - y_current

    z_minus_x_i, z_minus_x_j = distance_from_dest_x - a_i, distance_from_dest_y - a_j
    V = sqrt(pow(z_minus_x_i, 2) + pow(z_minus_x_j, 2))

    move_vector_x, move_vector_y = z_minus_x_i / V, z_minus_x_j / V

    update_position_x = x_current + vel_val[0] * move_vector_x
    update_position_y = y_current + vel_val[0] * move_vector_y

    distance_from_dest_x_j, distance_from_dest_y_j = destinations[1][0] - \
        x_j, destinations[1][1] - y_j

    z_minus_x_ii, z_minus_x_jj = distance_from_dest_x_j - \
        a_i, distance_from_dest_y_j - a_j
    V = sqrt(pow(z_minus_x_ii, 2) + pow(z_minus_x_jj, 2))

    move_vector_x, move_vector_y = z_minus_x_ii / V, z_minus_x_jj / V

    update_position_x_j = x_j + vel_val[1] * move_vector_x
    update_position_y_j = y_j + vel_val[1] * move_vector_y

    return update_position_x, update_position_y, update_position_x_j, update_position_y_j
# %% simulacija


for i in range(400):
    i+1
    new_position = collision_check(dc, dr)
    position_history.append([[new_position[0], new_position[1]], [
        new_position[2], new_position[3]]])

    curent_pos = get_current_possition()
    print(curent_pos)


# %% crtanje grafika


def plot():
    # print(position_history)
    plt.xlim(0, 400)
    plt.ylim(0, 400)
    x1_data = []
    y1_data = []
    x2_data = []
    y2_data = []

    for i in range(0, len(position_history)):
        x1_data.append(position_history[i][0][0])
        y1_data.append(position_history[i][0][1])
        x2_data.append(position_history[i][1][0])
        y2_data.append(position_history[i][1][1])

    plt.scatter(x1_data, y1_data)
    plt.scatter(x2_data, y2_data)

    plt.legend(["Start:(50, 50) Dest:(350, 350) Speed:12",
                "Start:(50, 350) Dest:(350, 50) Speed:10", ])
    plt.scatter(x1_data, y1_data, s=dc **
                2, facecolors='none', edgecolors='r')

    # plt.scatter(x2_data, y2_data, s=3600, facecolors='none', edgecolors='b')

    plt.grid()
    plt.xlabel('x', fontsize=18)
    plt.ylabel('y', fontsize=18)
    plt.savefig('plot_b.png')
    plt.show()


plot()

# %%

# %%
