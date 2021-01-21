# %%
import numpy as np
import matplotlib.pyplot as plt
from numpy.lib.function_base import append
from numpy.lib.histograms import _unsigned_subtract
from numpy.random import rand
import random


def give_card():
    card_list = list(range(1, 11)) + [10, 10, 10]
    return np.random.choice(card_list)

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
    # state = [sum, ace, dealer]
    current_sum, ace, dealer = state
    if dealer == 1:
        dealer = 11
    if ace and current_sum <= 11:
        current_sum += 10
    if current_sum == 21:
        return 1, current_sum  # win
    if current_sum < 17:
        return 0, current_sum

    # Eps greedy policy
    # Random hit or hold
    if rand() < eps:
        tmp = rand()
        if tmp >= 0.5:
            # hit
            return 0, current_sum
        else:
            # hold
            return 1, current_sum
    else:
        # Greedy policy
        if current_sum <= 11 and dealer <= 7:
            return 0, current_sum
        elif 17 - dealer >= 21 - current_sum:
            return 1, current_sum
        elif dealer + 10 > current_sum and dealer < 7:
            return 0, current_sum
        else:
            pass

        arr = np.array(Q)
        # res su indeksi kada je niz jednak sumi
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
            # Try moves that you didn't play before
            if hit_moves == []:
                return 0, current_sum
            elif hold_moves == []:
                return 1, current_sum
            else:
                return 0, current_sum
# %%

# Funkcija koja simulira igru, porlijedimo joj listu Q(s,a)


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
        # akcija hit 0 or hodl 1 and sum of moves

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

# Funkcija za azuriranje Q tabele kod sarse
# Ulazni parametri:
# Q lista stanja i akcija
# q lista tuple-ova koji predstavljaju jedno stanje i akciju koja se igrala u tom stanju
# result: informacija i tome da li je igrac pobijedio> 1 ako je pobijedio, -1 ako je izgubio i 0 ako je nereseno

# Izlaz:
# Azurirana vrijednost Q liste


def update_Q_SARSA(Q, q, result):

    # parametri
    alpha = 0.1
    gamma = 0.9

    for cnt in range(len(q)):
        if cnt == len(q) - 1:
            new_state = result
        else:
            new_state, new_move = q[cnt+1]
        current_state, move = q[cnt]

        for current_Q in Q:
            if current_state == current_Q[0]:

                if move == 1:

                    current_Q[1] = current_Q[1] + alpha * \
                        (result + gamma * new_state - current_Q[1])
                else:
                    current_Q[2] = current_Q[2] + alpha * \
                        (result + gamma * new_state - current_Q[2])

    return Q

# %%


prev_res = 0
current_res = 0
num_of_win = []
num_of_draw = []
num_of_lost = []


tmp1_t = []  # win
tmp2_t = []  # draw
tmp3_t = []  # lost

final_sarsa = []

for x in range(100):
    results_SARSA = []
    result = None

    tmp_e1 = []  # win
    tmp_e2 = []  # draw
    tmp_e3 = []  # lost

    # Pocetna vrijednost Q liste
    Q = [[4, 1, 1], [5, 1, 1], [6, 1, 1], [7, 1, 1], [8, 1, 1], [9, 1, 1], [10, 1, 1],
         [11, 1, 1], [12, 1, 1], [13, 1, 1], [14, 1, 1], [
             15, 1, 1], [16, 1, 1], [17, 1, 1],
         [18, 1, 1], [19, 1, 1], [20, 1, 1], [21, 1, 1]]
    for i in range(10000):
        result, history, valid = play_game(Q)
        results_SARSA.append(result)
        Q = update_Q_SARSA(Q, history, result)
        print("Game: " + str(i) + ', Result: ' + str(result))

    print('-------------------------------------')
    print('SARSA')
    for index, res in enumerate(results_SARSA):
        if res == 0:
            num_of_draw.append(0)
            results_SARSA.remove(res)
        elif res == 1:
            num_of_win.append(1)
        elif res == -1:
            num_of_lost.append(-1)

    print(len(num_of_lost))
    print(len(num_of_draw))
    print(len(num_of_win))

    tmp_e1.append(len(num_of_win))
    tmp_e2.append(len(num_of_draw))
    tmp_e3.append(len(num_of_lost))

    tmp1_t.append(tmp_e1[0])
    tmp2_t.append(tmp_e2[0])
    tmp3_t.append(tmp_e3[0])

    print(tmp_e1)

    print(len(num_of_lost))
    print(len(num_of_draw))
    print(len(num_of_win))

    final_sarsa.append(sum(results_SARSA)/len(results_SARSA))
    print(sum(results_SARSA)/len(results_SARSA))


print(tmp1_t)
print(final_sarsa)


x_axis = np.arange(0, 100).tolist()
print(x_axis)


plt.plot(x_axis, tmp1_t, label="WIN")
plt.plot(x_axis, tmp2_t, label="DRAW")
plt.plot(x_axis, tmp3_t, label="LOST")
plt.xlabel('x - Number of episodes')
plt.ylabel('y - WIN/DRAW/LOST')


plt.legend()
plt.grid()
plt.savefig('sarsa.png')
plt.show()


# print(results_SARSA)


# %%
