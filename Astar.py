

import collections

parent = dict()


def astar(graph, root, path, goal):
    visited, queue = list(), collections.deque([root])
    visited.append(root)
    path.append(root)
    var = 0
    totalCost = dict()
    while queue:
        vertex = queue.popleft()
        totalCost.clear()
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                var = cost[cityTranslation[neighbour]][cityTranslation[vertex]]
                var = var + heuristics[neighbour]
                totalCost[neighbour] = var
                visited.append(neighbour)
                # queue.append(neighbour)
                # parent[vertex] = neighbour
        x = min(totalCost, key=totalCost.get)
        # print(x)
        path.append(x)
        queue.append(x)
        if (x == goal):
            return path
    return path


graph = {'Arad': list(['Zerind', 'Timisoara', 'Sibiu']),
         'Zerind': list(['Oradea', 'Arad']),
         'Timisoara': list(['Arad', 'Lugoj']),
         'Lugoj': list(['Mehadia', 'Timisoara']),
         'Mehadia': list(['Lugoj', 'Drobeta']),
         'Drobeta': list(['Mehadia', 'Craiova']),
         'Craiova': list(['Drobeta', 'Pitesti', 'RimnicuVilcea']),
         'Pitesti': list(['Craiova', 'Bucharest']),
         'RimnicuVilcea': list(['Craiova', 'Pitesti', 'Sibiu']),
         'Oradea': list(['Zerind', 'Sibiu']),
         'Sibiu': list(['Fagaras', 'Oradea']),
         'Fagaras': list(['Sibiu', 'Bucharest']),
         'Bucharest': list(['Giurgiu', 'Urziceni']),
         'Giurgiu': list(['Bucharest']),
         'Urziceni': list(['Hirsova', 'Vaslui']),
         'Hirsova': list(['Urziceni', 'Eforie']),
         'Vaslui': list(['Iasi', 'Urziceni']),
         'Iasi': list(['Neamt']),
         'Neamt': list(['Iasi']),
         'Eforie': list(['Hirsova'])}

cost = [[0, 71, 0, 151, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [71, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 75, 0, 140, 118, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [151, 0, 140, 0, 0, 0, 0, 0, 0, 0, 80, 99, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 118, 0, 0, 111, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 111, 0, 70, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 70, 0, 75, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 75, 0, 120, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 120, 0, 138, 146, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 138, 0, 97, 0, 101, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 80, 0, 0, 0, 0, 146, 97, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 99, 0, 0, 0, 0, 0, 0, 0, 0, 211, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 101, 0, 211, 0, 90, 85, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 90, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 85, 0, 0, 0, 98, 142, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 86, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 98, 86, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 142, 0, 0, 0, 92, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 92, 0, 87],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 87, 0]]

cityTranslation = {
    'Oradea': 0,
    'Zerind': 1,
    'Arad': 2,
    'Sibiu': 3,
    'Timisoara': 4,
    'Lugoj': 5,
    'Mehadia': 6,
    'Drobeta': 7,
    'Craiova': 8,
    'Pitesti': 9,
    'RimnicuVilcea': 10,
    'Fagaras': 11,
    'Bucharest': 12,
    'Giurgiu': 13,
    'Urziceni': 14,
    'Eforie': 15,
    'Hirsova': 16,
    'Vaslui': 17,
    'Iasi': 18,
    'Neamt': 19}

heuristics = {
    'Oradea': 380,
    'Zerind': 374,
    'Arad': 366,
    'Sibiu': 253,
    'Timisoara': 329,
    'Lugoj': 244,
    'Mehadia': 241,
    'Drobeta': 242,
    'Craiova': 160,
    'Pitesti': 100,
    'RimnicuVilcea': 193,
    'Fagaras': 176,
    'Bucharest': 0,
    'Giurgiu': 77,
    'Urziceni': 80,
    'Eforie': 161,
    'Hirsova': 151,
    'Vaslui': 199,
    'Iasi': 226,
    'Neamt': 234}


z = list()
root = 'Arad'
Fpath = list()
goal = 'Bucharest'
astar(graph, root, Fpath, goal)
print("Path is")
print(Fpath)
path = Fpath

totalCost = 0
for i in range(0, len(path) - 1):
    x = i
    c = 0
    var1 = cityTranslation[path[x]]
    var2 = cityTranslation[path[x + 1]]
    var3 = cost[var1][var2]
    # path[i] returns city name

    # cityTranslation[path[i]] returns city index
    # cost[cityTranslation[path[i]][cityTranslation[path[i+1]] returns cost with neighbour
    if var3 != 0:
        totalCost += var3
    elif var3 == 0:
        while cost[cityTranslation[path[x]]][cityTranslation[path[i + 1]]] == 0 and c < 20:
            x = x - 1
            c = c + 1
        x1 = cityTranslation[path[x]]
        x2 = cityTranslation[path[i + 1]]
        totalCost += cost[x1][x2]

print("Total cost is", totalCost)
