# %%
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import rand


def give_card():
    card_list = list(range(1, 11)) + [10, 10, 10]
    return np.random.choice(card_list)


cards = give_card()
print(cards)
# %%


# Ulazni parametri
# Q: lista stanja i akcija koje igra  Q(s,a)
# state: trenutna suma karata igraca i info o tome da li ima keca
# eps: eps parametar  0.01
#
# Izlazni parametri:
# (0 za hit , 1 za hold i suma karata)


def player_bot_eps_greedy(Q, state, eps=0.01):

    hit_moves = []
    hold_moves = []
    current_sum, ace, dealer = state
    if dealer == 1:
        dealer = 11
    if ace and current_sum <= 11:
        current_sum += 10
    if current_sum == 21:
        return 1, current_sum  # win
    if current_sum < 17:
        return 0, current_sum

    if rand() < eps:
        tmp = rand()
        if tmp >= 0.5:
            # hit
            return 0, current_sum
        else:
            # hold
            return 1, current_sum
    else:
        # Greedy politika odlicivanja
        if current_sum <= 11 and dealer <= 7:
            return 0, current_sum
        elif 17 - dealer >= 21 - current_sum:
            return 1, current_sum
        elif dealer + 10 > current_sum and dealer < 7:
            return 0, current_sum
        else:
            pass

        arr = np.array(Q)
        res = np.where(arr == current_sum)

        try:
            hit_moves = Q[res[0][0]][1]
            hold_moves = Q[res[0][0]][2]
            if sum(hit_moves) > sum(hold_moves):
                return 0, current_sum
            elif sum(hit_moves) > sum(hold_moves):
                return 1, current_sum
            elif len(hit_moves) > len(hold_moves):
                return 0, current_sum
        except:
            # Probamo poteze koje nismo igrali
            if hit_moves == []:
                return 0, current_sum
            elif hold_moves == []:
                return 1, current_sum
            else:
                return 0, current_sum


# %%


# Funkcija koja simulira igru
def play_game(Q):
    player_cards = []
    dealer_cards = []
    state = None
    state_history = []
    action = None
    dealer_card = None
    usable_ace = False
    dealer_state = None
    catch_me = True

    # Podeli karte
    drawn_card = give_card()
    player_cards.append(drawn_card)

    drawn_card = give_card()
    dealer_cards.append(drawn_card)
    dealer_card = drawn_card

    drawn_card = give_card()
    player_cards.append(drawn_card)

    drawn_card = give_card()
    dealer_cards.append(drawn_card)
    dealer_state = sum(dealer_cards)

    dealer_card = dealer_cards[0]  # Uzimamo prvu kartu

    if 1 in player_cards:
        usable_ace = True
    else:
        pass
    state = sum(player_cards), usable_ace, dealer_card

    current = 0  # Trenutna suma karata
    while(1):
        # akcija hit 0 or hold 1 i trenutna suma karata

        action, current = player_bot_eps_greedy(Q, state)
        if action == 0:
            state_history.append((current, 0))
            drawn_card = give_card()
            player_cards.append(drawn_card)
            if drawn_card == 1:
                usable_ace = True
            state = sum(player_cards), usable_ace, dealer_card
            if state[0] > 21:
                return -1, state_history, True  # lost
            else:
                pass
        else:
            state_history.append((current, 1))
            break

    usable_ace = False
    draw_more = True
    dealer_state = sum(dealer_cards)

    if dealer_state >= current:
        catch_me = False

    for idx, card in enumerate(dealer_cards):
        if card == 1:
            dealer_cards[idx] = 11
            usable_ace = True
            break

    if dealer_state >= 17 and catch_me:
        draw_more = False
    else:
        pass

    while (draw_more):
        drawn_card = give_card()
        if drawn_card == 1 and sum(dealer_cards) < 11:
            dealer_cards.append(11)
            usable_ace = True
        elif drawn_card + sum(dealer_cards) > 21 and usable_ace == True:
            for idx, card in enumerate(dealer_cards):
                if card == 11:
                    dealer_cards[idx] = 1
                    usable_ace = False
            dealer_cards.append(drawn_card)
        else:
            dealer_cards.append(drawn_card)

        dealer_state = sum(dealer_cards)

        if dealer_state >= current:
            catch_me = True

        if dealer_state >= 17 and catch_me:
            break
        elif dealer_state >= 21:
            break
        else:
            continue

    if dealer_state > 21:
        return 1, state_history, True

    elif dealer_state == current:
        return 0, state_history, True  # draw
    elif current > dealer_state:
        return 1, state_history, True  # Win
    elif current < dealer_state:
        return -1, state_history, True  # lost
    else:
        return 0, state_history, True  # draw

# %%


def update_Q_learning(Q, q, result):

    alpha = 0.1
    gamma = 0.9

    for cnt in range(len(q)):
        if cnt == len(q) - 1:
            # Terminal state, value of new state if we used greedy policy
            new_state = q[cnt][0]+5
        else:
            new_state, new_move = q[cnt+1]
        current_state, move = q[cnt]

        for current_Q in Q:
            if current_state == current_Q[0]:
                # Move based on greedy policy
                if current_Q[1] >= current_Q[2]:
                    current_Q[1] = current_Q[1] + alpha * \
                        (result + gamma*new_state - current_Q[1])
                else:
                    current_Q[2] = current_Q[2] + alpha * \
                        (result + gamma*new_state - current_Q[2])
                break
    return Q

# %%


prev_res = 0
current_res = 0


tmp1_t = []  # win
tmp2_t = []  # draw
tmp3_t = []  # lost

final_q = []

for x in range(100):
    results_Q_lerning = []
    result = None
    tmp_e1 = []  # win
    tmp_e2 = []  # draw
    tmp_e3 = []  # lost

    num_of_win = []
    num_of_draw = []
    num_of_lost = []

    Q = [[4, 1, 1], [5, 1, 1], [6, 1, 1], [7, 1, 1],
         [8, 1, 1], [9, 1, 1], [10, 1, 1], [11, 1, 1],
         [12, 1, 1], [13, 1, 1], [14, 1, 1], [15, 1, 1],
         [16, 1, 1], [17, 1, 1], [18, 1, 1], [19, 1, 1],
         [20, 1, 1], [21, 1, 1]]

    for i in range(10000):
        result, history, valid = play_game(Q)
        results_Q_lerning.append(result)
        Q = update_Q_learning(Q, history, result)

    for index, res in enumerate(results_Q_lerning):
        if res == 0:
            num_of_draw.append(0)
            results_Q_lerning.remove(res)
        elif res == 1:
            num_of_win.append(1)
        elif res == -1:
            num_of_lost.append(-1)

    tmp_e1.append(len(num_of_win))
    tmp_e2.append(len(num_of_draw))
    tmp_e3.append(len(num_of_lost))

    tmp1_t.append(tmp_e1[0])
    tmp2_t.append(tmp_e2[0])
    tmp3_t.append(tmp_e3[0])

    print('-------------------------------------')
    print('Results in episode:' + str(x))
    print('Q-learning bot:')
    print('Number of win:' + str(tmp_e1[-1]))
    print('Number of draw:' + str(tmp_e2[-1]))
    print('Number of lost:' + str(tmp_e3[-1]))
    print("Result" + str(sum(results_Q_lerning)/len(results_Q_lerning)))
    print('-------------------------------------')

    # final_q.append(sum(results_Q_lerning)/len(results_Q_lerning))


x_axis = np.arange(0, 100).tolist()
# print(x_axis)

# print(results_Q_lerning)

plt.plot(x_axis, tmp1_t, label="WIN")
plt.plot(x_axis, tmp2_t, label="DRAW")
plt.plot(x_axis, tmp3_t, label="LOST")

plt.xlabel('x - Number of episodes')
plt.ylabel('y -Q_learning_result')

plt.grid()
plt.legend()
plt.savefig('q_learning.png')
plt.show()
