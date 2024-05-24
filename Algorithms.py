from Phramacy import Pharmacy


def path_cost(path):
    if path == None:
        return
    return sum(cost for (node, cost) in path)  # total_cost


#############################################################
def ucs(graph, start: Pharmacy, goal):
    visited_nodes = []
    queue = [[(start, 0)]]
    while queue:
        queue.sort(key=path_cost)  # sorting by cost
        path = queue.pop(0)
        node: Pharmacy = path[-1][0]
        if node in visited_nodes:
            continue
        visited_nodes.append(node)
        if node.search_medicine(goal) != None:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for adjacent_node, cost in adjacent_nodes:
                new_path = path.copy()
                new_path.append((adjacent_node, cost))
                queue.append(new_path)


##############################################################
# fifo
def bfs(graph, start, goal):
    queue = [[(start, 0)]]
    visited_nodes = []
    while queue:
        # print("queue : " , queue)
        path = queue.pop(0)  # type : ignore
        # print("current_path : " )
        # for p in path:
        #     print(p[0], end="->")
        # print()
        node: Pharmacy = path[-1][0]
        if node in visited_nodes:
            continue
        visited_nodes.append(node)
        if node.search_medicine(goal) != None:
            return path
        else:
            adjacent_nodes = graph.get(node, [])  # graph[node]
            for adjacent_node in adjacent_nodes:
                new_path = path.copy()
                new_path.append(adjacent_node)
                queue.append(new_path)


# bfs_path = bfs(PharmacyMap.graph, start, goal)


##############################################################
# lifo
def dfs(graph, start, goal):
    stack = [[(start, 0)]]
    visited_nodes = []
    while stack:
        path: Pharmacy = stack.pop()
        node: Pharmacy = path[-1][0]
        if node in visited_nodes:
            continue
        visited_nodes.append(node)
        if node.search_medicine(goal) != None:
            return path
        else:
            adjacent_nodes = graph.get(node, [])
            for adjacent_node in adjacent_nodes:
                new_path = path.copy()
                new_path.append(adjacent_node)
                stack.append(new_path)


# bfs_path = bfs(PharmacyMap.graph, start, goal)

##############################################################
iteration_n = 5


def iter_deep(graph, start, goal, n):
    for i in range(n + 1):
        queue = [[(start, 0)]]
        visited_nodes = []

        while queue:
            # print(f"Level : {i}")

            # print(f"Queue : {queue}")
            cur_path: Pharmacy = queue.pop(-1)  # type: ignore

            # print(f"Current Path : {cur_path} \n")
            node: Pharmacy = cur_path[-1][0]  # type: ignore

            if node in visited_nodes:
                continue
            visited_nodes.append(node)

            if node.search_medicine(goal) != None:
                return cur_path

            else:
                # to stop the algorithm at a certain level
                if len(cur_path) > i:  # type: ignore
                    continue
                adj_nodes = graph.get(node, [])

                for adj_node in adj_nodes:  # the loop ends when there are no children
                    new_path = cur_path.copy()  # type: ignore
                    new_path.append(adj_node)
                    queue.append(new_path)


##############################################################


def __main__(graph, start: Pharmacy, goal):
    while True:
        print(
            """
Choose the Algorithm to find your Medicin:
    1. Uniform Cost Search
    2. Breadth First Search
    3. Depth First Search
    4. Depth-Limited and Iterative Deepening Searchss
"""
        )
        chose = input("Enter the number of algorithm: ").strip()
        if chose == "1":
            return ucs(graph, start, goal)
        elif chose == "2":
            return bfs(graph, start, goal)
        elif chose == "3":
            return dfs(graph, start, goal)
        elif chose == "4":
            return iter_deep(graph, start, goal, iteration_n)
        else:
            print("you entered error number")

    # pass
