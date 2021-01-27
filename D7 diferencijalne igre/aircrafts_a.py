# %%
from math import sqrt
import matplotlib.pyplot as plt

dc = 80


# agent info lista
# prvi element: cilj
# drugi element: pocetna pozicija
# treci element: max brzina
# cetvrti elemet: id letjelice

agents_info = [[[350, 350], [50, 50], 30, 0],
               [[350, 50], [50, 350], 30, 1]]

# pocetna pozicija na pocetku, kasnije se azurira
position_history = [[agents_info[0][1], agents_info[1][1]]]


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


def get_current_possition():
    return position_history[-1]

# %%


def collision_check(dc):
    tmp_pos = get_current_possition()
    destinations = destination(agents_info)
    vel_val = get_velocity(agents_info)
    x_current, y_current = tmp_pos[0][0], tmp_pos[0][1]

    x_j, y_j = tmp_pos[1][0], tmp_pos[1][1]
    V = sqrt(pow(x_j - x_current, 2) + pow(y_j - y_current, 2))

    if(V < dc):
        distance_from_dest_x, distance_from_dest_y = destinations[0][0] - \
            x_current, destinations[0][1] - y_current
        V1 = sqrt(pow(distance_from_dest_x, 2) +
                  pow(distance_from_dest_y, 2))
        move_vector_x, move_vector_y = distance_from_dest_x / \
            V1, distance_from_dest_y / V1
        update_position_x = x_current + vel_val[0] * move_vector_x
        update_position_y = y_current + vel_val[0] * move_vector_y

        distance_from_dest_x_j, distance_from_dest_y_j = destinations[1][0] - \
            x_j, destinations[1][1] - y_j
        V2 = sqrt(pow(distance_from_dest_x_j, 2) +
                  pow(distance_from_dest_y_j, 2))
        move_vector_x_j, move_vector_y_j = distance_from_dest_x_j / \
            V2, distance_from_dest_y_j / V2
        update_position_x_j = x_j + (1 * move_vector_x_j)
        update_position_y_j = y_j + (1 * move_vector_y_j)

    else:
        distance_from_dest_x, distance_from_dest_y = destinations[0][0] - \
            x_current, destinations[0][1] - y_current
        V1 = sqrt(pow(distance_from_dest_x, 2) +
                  pow(distance_from_dest_y, 2))
        move_vector_x, move_vector_y = distance_from_dest_x / \
            V1, distance_from_dest_y / V1
        update_position_x = x_current + (vel_val[0] * move_vector_x)
        update_position_y = y_current + (vel_val[0] * move_vector_y)

        distance_from_dest_x_j, distance_from_dest_y_j = destinations[1][0] - \
            x_j, destinations[1][1] - y_j
        V2 = sqrt(pow(distance_from_dest_x_j, 2) +
                  pow(distance_from_dest_y_j, 2))
        move_vector_x_j, move_vector_y_j = distance_from_dest_x_j / \
            V2, distance_from_dest_y_j / V2
        update_position_x_j = x_j + (vel_val[1] * move_vector_x_j)
        update_position_y_j = y_j + (vel_val[1] * move_vector_y_j)

    return update_position_x, update_position_y, update_position_x_j, update_position_y_j


# %% Simulacija
for i in range(400):
    i+1
    new_position = collision_check(dc)
    position_history.append([[new_position[0], new_position[1]], [
        new_position[2], new_position[3]]])


# %% crtanje grafika


def plot():
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

    plt.scatter(x1_data, y1_data, c='b', label="letjelica1")
    plt.scatter(x2_data, y2_data, c='r', label="letjelica2")
    plt.legend(["Start:(50, 50) Dest:(350, 350) Speed:30",
                "Start:(50, 350) Dest:(350, 50) Speed:30"])
    # dc range
    # crta krug oko letjelice sa poluprecnikom dc
    # Nije skalirano
    plt.scatter(x1_data, y1_data, s=dc **
                2, facecolors='none', edgecolors='b', )

    plt.xlabel('x', fontsize=18)
    plt.ylabel('y', fontsize=18)

    plt.grid()
    plt.savefig('plot_a.png')
    plt.show()


plot()

# %%
