graph = { 
    "S" : ({"A":5,"B":4},10),
    "A":({"C":6,"D":8},8),
    "B":({"E":2,"G":3},2),
    "C":({},4),
    "D":({"G":4},5),
    "E":({},6),
    "G":({},0)
}

def get_min(q):
    mn = (0, (0, float("INF")))
    for i in q:
        if sum(q[i] , sum(mn[1])):
            mn = (i, q[i])
            # print(mn)
    return mn[0]
def a_star(graph, prev, dst, path, pcost, q):
    # n : (h(n), g(n)) of current vertex
    print("connected nodes of current node ", prev, " with h(n) values : ") # and
    for n in graph[prev][0]: # neighbours list n = Z, S, T
        if n not in path:
            q[n] = (graph[n][1], graph[prev][0][n])
            print(n, "->", q[n])
            add1 = sum(q[n])
            path_cost = pcost + add1 # a to c = a + b ?? b to c?? tot a* value
            print("a* value for ", n, " is : ", path_cost)
    while q:
        mn = get_min(q)
        print("selecting minimum vertex : ", mn)
        print("_")
        if dst == mn:
            return path + [dst]
        pc = pcost + q[mn][1]
        print("previous path cost : ", pc)
        # del q[mn]
        new_path = a_star(graph, mn, dst, path + [mn], pc, q)
        if new_path:
            return new_path
    return []
source = input("enter source vertex : ")

dest = input("enter destination vertex : ")
heuristic = int(input("enter given heuristic value for source : "))
path = a_star(graph, source, dest, [], 0, {source : (heuristic, 0)})
if path:
    print(path)
else:
    print("path not found!")
print("->".join(a_star(graph, "S", "G", [], 0, {"S" : (399, 0)})))

####

graph = { 
    "S" : ({"A":5,"B":4},10),
    "A":({"C":6,"D":8},8),
    "B":({"E":2,"G":3},2),
    "C":({},4),
    "D":({"G":4},5),
    "E":({},6),
    "G":({},0)
}

def get_min(q):
    mn_node = None
    mn_value = float("inf")
    for node in q:
        h, g = q[node]
        f = h + g  # f(n) = g(n) + h(n)
        if f < mn_value:
            mn_value = f
            mn_node = node
    return mn_node

def a_star(graph, prev, dst, path, pcost, q):
    print("Connected nodes of current node", prev, "with h(n) values:")
    for n in graph[prev][0]:
        if n not in path:
            g_cost = pcost + graph[prev][0][n]
            h_cost = graph[n][1]
            q[n] = (h_cost, g_cost)
            print(f"{n} -> (h={h_cost}, g={g_cost})")
            print(f"A* value for {n} is: {h_cost + g_cost}")

    while q:
        mn = get_min(q)
        print("Selecting minimum f(n) vertex:", mn)
        print("_")
        if mn == dst:
            return path + [dst]
        pc = q[mn][1]
        del q[mn]
        new_path = a_star(graph, mn, dst, path + [mn], pc, q)
        if new_path:
            return new_path
    return []

# ---- Input ----
source = input("Enter source vertex: ")
dest = input("Enter destination vertex: ")
heuristic = int(input(f"Enter heuristic value for {source}: "))

path = a_star(graph, source, dest, [], 0, {source : (heuristic, 0)})

if path:
    print("Path found:", " -> ".join(path))
else:
    print("Path not found!")

