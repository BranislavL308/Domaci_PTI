# %%
from math import sqrt
import matplotlib.pyplot as plt

DISTANCE_COLLISION = 20  # a)


# agent info lista
# prvi element: cilj
# drugi element: pocetna pozicija
# treci element: max brzina
# cetvrti elemet: id letjelice
agents_info = [[[200, -100], [-200, 100], 100, 0],
               [[-100, 80], [-160, -45], 20, 1]]


def get_aircraf_id(agents_info):
    id_list = []
    for i in range(0, len(agents_info)):
        agents_info[i][3]
        id_list.append(agents_info[i][3])
    return id_list


def goal(agents_info):
    goal_list = []
    for i in range(0, len(agents_info)):
        agents_info[i][0]
        goal_list.append(agents_info[i][0])
    return goal_list


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


#position_history.append([[150, 100], [-20, -100]])
# print(agents_info)


def get_current_possition():
    return position_history[-1]

# %%


#current_pos_x = []
# current_pos_x.append(curent_pos[0][0])


for i in range(1000):
    i+1

    def colision_detected(colision_distance):
        temp_pos = get_current_possition()
        goals = goal(agents_info)
        vel_val = get_velocity(agents_info)
        x_current, y_current = temp_pos[0][0], temp_pos[0][1]

        x_j, y_j = temp_pos[1][0], temp_pos[1][1]
        print(x_j, y_j)
        norm = sqrt(pow(x_j - x_current, 2) + pow(y_j - y_current, 2))
        print(norm)
        if(norm < colision_distance):

            distance_from_goal_x, distance_from_goal_y = goals[0][0] - \
                x_current, goals[0][1] - y_current
            norm1 = sqrt(pow(distance_from_goal_x, 2) +
                         pow(distance_from_goal_y, 2))
            move_vector_x, move_vector_y = distance_from_goal_x / \
                norm1, distance_from_goal_y / norm1
            update_position_x = x_current + vel_val[0] * move_vector_x
            update_position_y = y_current + vel_val[0] * move_vector_y

            distance_from_goal_x_j, distance_from_goal_y_j = goals[1][0] - \
                x_j, goals[1][1] - y_j
            norm2 = sqrt(pow(distance_from_goal_x_j, 2) +
                         pow(distance_from_goal_y_j, 2))
            move_vector_x_j, move_vector_y_j = distance_from_goal_x_j / \
                norm2, distance_from_goal_y_j / norm2
            update_position_x_j = x_j + (1 * move_vector_x_j)
            update_position_y_j = y_j + (1 * move_vector_y_j)

        else:
            distance_from_goal_x, distance_from_goal_y = goals[0][0] - \
                x_current, goals[0][1] - y_current
            norm1 = sqrt(pow(distance_from_goal_x, 2) +
                         pow(distance_from_goal_y, 2))
            move_vector_x, move_vector_y = distance_from_goal_x / \
                norm1, distance_from_goal_y / norm1
            update_position_x = x_current + (vel_val[0] * move_vector_x)
            update_position_y = y_current + (vel_val[0] * move_vector_y)

            distance_from_goal_x_j, distance_from_goal_y_j = goals[1][0] - \
                x_j, goals[1][1] - y_j
            norm2 = sqrt(pow(distance_from_goal_x_j, 2) +
                         pow(distance_from_goal_y_j, 2))
            move_vector_x_j, move_vector_y_j = distance_from_goal_x_j / \
                norm2, distance_from_goal_y_j / norm2
            update_position_x_j = x_j + (vel_val[1] * move_vector_x_j)
            update_position_y_j = y_j + (vel_val[1] * move_vector_y_j)

        return update_position_x, update_position_y, update_position_x_j, update_position_y_j

    new_position = colision_detected(DISTANCE_COLLISION)
    position_history.append([[new_position[0], new_position[1]], [
        new_position[2], new_position[3]]])

    curent_pos = get_current_possition()
    print(curent_pos)


# %%


def draw():
    # print(position_history)
    plt.xlim(-150, 150)
    plt.ylim(-150, 150)
    x1_data = []
    y1_data = []
    x2_data = []
    y2_data = []

    for i in range(0, len(position_history)):
        x1_data.append(position_history[i][0][0])
        y1_data.append(position_history[i][0][1])
        x2_data.append(position_history[i][1][0])
        y2_data.append(position_history[i][1][1])

    #fig, ax = plt.subplots()

    plt.scatter(x1_data, y1_data)
    plt.scatter(x1_data, y1_data, s=DISTANCE_COLLISION **
                2, facecolors='none', edgecolors='r')
    plt.scatter(x2_data, y2_data)
    #plt.scatter(x2_data, y2_data, s=3600, facecolors='none', edgecolors='b')
    """ plt.plot(x1_data,
             y1_data, 'ro', marker=None, fill, markersize=1, label="letjelica1")
    #plt.Circle((x1_data, y1_data), 60, color='r', fill=False)
    plt.plot(x2_data,
             y2_data, 'go', markersize=1, label="letjelica2") """
    plt.xlabel('x', fontsize=18)
    plt.ylabel('y', fontsize=18)
    plt.show()


""" 
#fig, ax = plt.subplots()
#ax.scatter([1, 2, 1.5], [2, 1, 1.5])
#cir = plt.Circle((1.5, 1.5), 0.07, color='r', fill=False)
ax.set_aspect('equal', adjustable='datalim')
# ax.add_patch(cir)
plt.show() """


draw()

# %%

# %%
