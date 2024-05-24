import numpy as np
import PharmacyMap
from Phramacy import Pharmacy
from Medicine import Medicine


# Calculate the total cost of a path
def path_cost(path):
    if path == None:
        return
    return sum(cost for (node, cost) in path)  # total_cost


# using uniform cost search to find distances between all pharmacies
def ucs(graph, start: Pharmacy, goal: Pharmacy):
    visited_nodes = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)  # sorting by cost
        path = queue.pop(0)
        node: Pharmacy = path[-1][0]
        if node in visited_nodes:
            continue
        visited_nodes.append(node)
        if node == goal:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for adjacent_node, cost in adjacent_nodes:
                new_path = path.copy()
                new_path.append((adjacent_node, cost))
                queue.append(new_path)


# find the distance between all pharmacies
def cal_distances(pharmacies):
    distances = []
    for i in range(len(pharmacies)):
        distance = []
        for j in range(len(pharmacies)):
            goal_path = ucs(PharmacyMap.graph, pharmacies[i], pharmacies[j])
            distance.append(path_cost(goal_path))
        distances.append(distance)

    return distances


def ant_colony_optimization(
    pharmacies, n_ants, n_iterations, alpha, beta, evaporation_rate, Q, goal
):
    n_pharmacies = len(pharmacies)
    pheromone = np.ones((n_pharmacies, n_pharmacies))
    best_path = None
    best_path_length = np.inf
    distances = cal_distances(pharmacies)
    minPrice = np.inf
    goal_pharmacy: Pharmacy = None

    for iteration in range(n_iterations):
        paths = []
        path_lengths = []

        for ant in range(n_ants):
            visited = [False] * n_pharmacies
            current_index_pharmacy = np.random.randint(n_pharmacies)
            visited[current_index_pharmacy] = True
            current_pharmacy: Pharmacy = pharmacies[current_index_pharmacy]
            medicine: Medicine = current_pharmacy.search_medicine(goal)
            if medicine is not None:
                if medicine.get_priceOfMedicine() < minPrice:
                    minPrice = medicine.get_priceOfMedicine()
                    goal_pharmacy = current_pharmacy

            path = [current_index_pharmacy]
            path_length = 0

            while False in visited:
                unvisited = np.where(np.logical_not(visited))[0]
                probabilities = np.zeros(len(unvisited))
                # print(unvisited)
                # print(probabilities)
                for i, unvisited_point in enumerate(unvisited):
                    # print(unvisited_point, " -> ", current_index_pharmacy)
                    # print(distances[current_index_pharmacy][unvisited_point])
                    probabilities[i] = (
                        pheromone[current_index_pharmacy, unvisited_point] ** alpha
                        / distances[current_index_pharmacy][unvisited_point] ** beta
                    )

                probabilities /= np.sum(probabilities)

                next_index_pharmacy = np.random.choice(unvisited, p=probabilities)
                path.append(next_index_pharmacy)
                path_length += distances[current_index_pharmacy][next_index_pharmacy]
                visited[next_index_pharmacy] = True
                current_point = next_index_pharmacy

                paths.append(path)
                path_lengths.append(path_length)

                if path_length < best_path_length:
                    best_path = path
                    best_path_length = path_length

            pheromone *= evaporation_rate

            for path, path_length in zip(paths, path_lengths):
                for i in range(n_pharmacies - 1):
                    pheromone[path[i], path[i + 1]] += Q / path_length
                pheromone[path[-1], path[0]] += Q / path_length

    return (goal_pharmacy, minPrice)


def __main__(goal):
    n_ants = 6
    iterations = 20

    goal_pharmacy, minPrice = ant_colony_optimization(
        PharmacyMap.pharmacies,
        n_ants,
        iterations,
        alpha=1,
        beta=1,
        evaporation_rate=0.5,
        Q=1,
        goal=goal,
    )

    if goal_pharmacy is not None:
        print(
            f"The medicine {goal} has the best price you can find it at {goal_pharmacy.get_nameOfPharmacy()}",
            f"in {goal_pharmacy.get_streetName()} with {minPrice} $",
        )
    else:
        print(f"The Medicine {goal} not found")
