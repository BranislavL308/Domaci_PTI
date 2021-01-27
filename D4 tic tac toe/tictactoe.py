# Tic Tac Toe game in python
# %%
import numpy as np
import matplotlib.pyplot as plt
free_space = 0
player_X = 1
player_O = 2

win, draw, lose = 1, 0, -1

# create boad, list of 9 zeros, 0 represents empty,
board = [free_space for x in range(9)]

# model table
board_state = [free_space, free_space, free_space,
               free_space, free_space, free_space,
               free_space, free_space, free_space, ]

# Input: list of current state of board


def is_winner(board_state):
    # Odlucivanje pobjednika

    # horizontalne linije
    if board_state[0] != free_space and board_state[0] == board_state[1] and board_state[0] == board_state[2]:
        return board_state[0]
    if board_state[3] != free_space and board_state[3] == board_state[4] and board_state[3] == board_state[5]:
        return board_state[3]
    if board_state[6] != free_space and board_state[6] == board_state[7] and board_state[6] == board_state[8]:
        return board_state[6]

    # vetikalne linije
    if board_state[0] != free_space and board_state[0] == board_state[3] and board_state[0] == board_state[6]:
        return board_state[0]
    if board_state[1] != free_space and board_state[1] == board_state[4] and board_state[1] == board_state[7]:
        return board_state[1]
    if board_state[2] != free_space and board_state[2] == board_state[5] and board_state[2] == board_state[8]:
        return board_state[2]

    # dijagonale
    if board_state[0] != free_space and board_state[0] == board_state[4] and board_state[0] == board_state[8]:
        return board_state[0]
    if board_state[6] != free_space and board_state[6] == board_state[4] and board_state[6] == board_state[2]:
        return board_state[6]

    return free_space


def check_free_space(board_state):
    res = []
    for pos, player in enumerate(board_state):
        if player == free_space:
            res.append(pos)
    return res


def reward(player, board_state):
    if player == player_X:
        return lose
    elif player == player_O:
        return win
    elif len(check_free_space(board_state)) == 0:
        return draw
    else:
        return None


def best_move_O(board_state):

    s = {}  # Rjecnik sa potezima i ocjenama poteza
    return_list = []
    next_board_state = board_state[:]
    free = check_free_space(board_state)

    for pos in free:
        s[pos] = draw

    for pos in s:
        next_board_state[pos] = player_X

        # Ocjena kvaliteta poteza
        # Ako igrac O pobijedi, taj potez koji donosi pobjedu se nagradjuje
        # sa 1
        # Ako  je X pobjednik posle odigranog poteza O, taj potez se nagradjuje sa 0.5

        if is_winner(board_state) == player_X:
            s[pos] = 0.5

        next_board_state[pos] = player_O
        if is_winner(next_board_state) == player_O:
            s[pos] = 1
        # Resetujemo tablu
        next_board_state[pos] = free_space

    s = {k: v for k, v in sorted(
        s.items(), key=lambda item: item[1], reverse=True)}

    for ret in s:
        # ako mozemo pobijediti igramo taj potez
        # nagrada za taj potez je 1
        if s[ret] == 1:
            return ret
        # if we can lose we should play this move
        elif s[ret] == 0.5:
            return ret
        else:
            return_list.append(ret)

    return return_list[np.random.randint(0, len(return_list))]

# Najbolji potez igrac X
# Ulazni parametri:
# board_state Trenutno stanje na tabli
# last_move: poslednji potez (int)
#
# Ilzal:
# Najbolji potez igraca X


def best_move_X(board_state, lastMove):
    """Najbolji potez igraca X

    Ulaz:
        board_state ([list]): Trenutno stanje table
        lastMove: broj, Posto X igra 2. ako je X odigrao zadnji potez onda je nerijeseno
    Izlaz:
        [int]: Najbolji potez za X igraca
    """
    s = {}
    returnList = []
    nextboard_state = board_state[:]
    free = check_free_space(board_state)

    # Provjera  da li je kraj
    #
    if len(check_free_space(board_state)) == 0:
        return lastMove

    for pos in free:
        s[pos] = draw

    for pos in s:
        nextboard_state[pos] = player_O
        # Da li ce mi sledeci potez rezultovati poraz?
        if is_winner(nextboard_state) == player_O:
            s[pos] = 0.5
        # da li ce sledeci potez rezultovati pobjedom
        nextboard_state[pos] = player_X
        if is_winner(nextboard_state) == player_X:
            s[pos] = 1

        nextboard_state[pos] = free_space

    s = {k: v for k, v in sorted(
        s.items(), key=lambda item: item[1], reverse=True)}

    for ret in s:
        # If we can win we should play this move
        if s[ret] == 1:
            return ret
        # If we can lose we should play this move
        elif s[ret] == 0.5:
            return ret
        else:
            returnList.append(ret)

    return returnList[np.random.randint(0, len(returnList))]


def q_learning(player, s, Q, board_state, rew, alpha=0.1, gamma=0.9):

    best = 0
    if player == 2:
        best = best_move_O(board_state)
    elif player == 1:
        best = best_move_X(board_state, s)
    new_state = True

    for q in Q:
        if q[0] == board_state:
            q[1] = q[1] + alpha*(rew + gamma*best - q[1])
            new_state = False
        else:
            pass
    if new_state:
        Q.append([board_state, 0.5])
    return Q

# %% Decision policy

#


def eps_greedy_decision(player, board_state, Q, eps=0.01):
    """Politika odlucivanja

    Ulazni parametri:
        player: broj igraca koji igra: 1 X, 2 O

        board_state: trenutno stanje table_lista
        Q: Q tabela za trenutnog igraca
        eps : korisnik zadaje, po default-u 0.01.

    Izlaz:

        Potez trenutnog igraca, tj. broj koji predstavlja polje na tabli [0 - 9]
    """

    if np.random.rand() < eps:
        # Slucajan potez
        f = check_free_space(board_state)
        return f[np.random.randint(0, len(f))]
    else:
        # Pohlepna politika
        if player == 2:
            best = best_move_O(board_state)
        else:
            best = best_move_X(board_state, None)
        return best

# Simulacija igre
# Ulazni parametri
# Q lista igraca X i Q lista igraca O
# izlazni parametri:
# azurirana vrijednost Q za X i O, rezultat igre i stanje na tabli na kraju te igre


def play_game(Q_X, Q_O):

    board_state = [free_space, free_space, free_space,
                   free_space, free_space, free_space,
                   free_space, free_space, free_space, ]
    rew = None
    state = None

    while True:
        x = eps_greedy_decision(1, board_state, Q_X)
        board_state[x] = player_X

        rew = reward(is_winner(board_state), board_state)
        if rew == None:
            Q_X = q_learning(1, x, Q_X, board_state, rew=0.5)
        else:
            if rew == lose:
                # Nova vrednost Q-a
                Q_X = q_learning(1, x, Q_X, board_state, rew)
                break
            elif rew == draw:
                Q_X = q_learning(1, x, Q_X, board_state, rew)
                break

        o = eps_greedy_decision(2, board_state, Q_O)
        board_state[o] = player_O

        rew = reward(is_winner(board_state), board_state)

        if rew == win:
            # Nova vrednost Q-a
            Q_O = q_learning(2, o, Q_O, board_state, rew)
            break
        elif rew == lose:
            Q_O = q_learning(2, o, Q_O, board_state, rew)
            break
        elif rew == draw:
            Q_O = q_learning(2, o, Q_O, board_state, rew)
            break
        else:
            Q_O = q_learning(2, o, Q_O, board_state, rew=0.5)

    return Q_X, Q_O, rew, board_state


# %%

x_axis = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000]

win_X = []
win_O = []

draw_X = []
draw_O = []

lost_X = []
lost_O = []


board = []
result_X = []
result_O = []
Q_X = []
Q_O = []

for i in range(10000):
    Q_X, Q_O, r, board = play_game(Q_X, Q_O)

    result_O.append(r)
    result_X.append(-1*r)

    # print('Number of  game : ' + str(i))


for index, res in enumerate(result_O):
    if res == 0:
        draw_O.append(0)
    elif res == 1:
        win_O.append(1)
    elif res == -1:
        lost_O.append(-1)


for index, res in enumerate(result_X):
    if res == 0:
        draw_X.append(0)
    elif res == 1:
        win_X.append(1)
    elif res == -1:
        lost_X.append(-1)


print('Results for 10000 iterations:')
print("-----------------")

print('Player O')
print('Number of wins' + str(len(win_O)))
print('Number of draws:' + str(len(draw_O)))
print('Number of lost:' + str(len(lost_O)))
print("-----------------")
print('Player X')
print('Number of wins:' + str(len(win_X)))
print('Number of draws:' + str(len(draw_X)))
print('Number of lost:' + str(len(lost_X)))
print("-----------------")


# plot
labels = ['WIN', 'DRAW', 'LOST']
sizes = [len(win_X), len(draw_X), len(lost_X)]

colors = ['gold', 'yellowgreen', 'lightcoral']
explode = (0.1, 0, 0)  # explode 1st slice

plt.title('Results for player X')
# Pie plot za jednu igru
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)

plt.axis('equal')
plt.savefig('q_learning.png')
plt.show()
