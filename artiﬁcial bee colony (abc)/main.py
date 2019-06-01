from cost_functions import *
from abc_algorithm import ArtificialBeeColony


# initialize:
cost_func = NQueen(15)
# cost_func = TravellingSalesmanProblem(10, 5)  # The problem to solve!
artificialBeeColony = ArtificialBeeColony(cost_func, 50)

max_iteration = 2000

# <1><use following code for while loop instead of for loop>:
# iteration = 0
# threshold = 10
# best_cost = np.inf
# while best_cost > threshold:
#     iteration += 1
# <1><end>

for iteration in range(max_iteration):
    # (a) Place the employed bees on the food sources in the memory:
    artificialBeeColony.place_employed_bees()

    # (b) Place the onlooker bees on the food sources in the memory:
    artificialBeeColony.place_onlooker_bees()

    # (c) Send the scouts to the search area for discovering new food sources:
    artificialBeeColony.send_scout_to_search()

    artificialBeeColony.store_best_iteration_foodsource()

    # <1><use following code for while loop instead of for loop>:
    # best_cost = min(artificialBeeColony.employees_cost)
    # <1><end>

artificialBeeColony.print_overall_result()


# this algorithm it doesnt fall into local minimal.
# it dose exploration and exploitation at the same time.
