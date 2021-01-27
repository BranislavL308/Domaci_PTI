import sympy as sym
# symbolic math

# a1 broj proizvoda prvog proizvodjaca
# a2 broj proizvoda drugog proizvodjaca
#  cijena proizvodnje
# d - potraznja
# p jedinicna cijena


def duopoly():
    # Dobit
    a1, a2 = sym.symbols('a1,a2')

    cost_first_player = 0.5/a1*a1
    cost_second_player = 30/a2

    # Jedinicna cijena
    unit_price = 100 - (a1 + a2)

    player1_utility = unit_price*a1 - cost_first_player
    player2_utility = unit_price*a2 - cost_second_player

    duda1 = sym.Derivative(player1_utility, a1).doit()
    duda2 = sym.Derivative(player2_utility, a2).doit()

    # Nesov ekvilibrijum
    # du1/da1 = 0
    # du2/da2 = 0
    du_1 = sym.Eq((duda1), 0)
    du_2 = sym.Eq((duda2), 0)

    # Rjesenje sistema jednacina a1, i a2
    a1, a2 = sym.nsolve((du_1, du_2), (a1, a2), (100, 100))
    print('Players equilibriums:')
    print("Player 1 equilibrium : " + str(a1))
    print("Player 2 equilibrium : " + str(a2))

    # Dobit za igrace
    cost_first_player = 0.5/a1*a1
    cost_second_player = 30/a2
    unit_price = 100-(a1+a2)

    print('------------------------------')
    utility1 = unit_price*a1 - cost_first_player
    utility2 = unit_price*a2 - cost_second_player
    print('Players utilities:')
    print("Player 1 utility:" + str(utility1))
    print("Player 2 utility:" + str(utility2))


duopoly()
