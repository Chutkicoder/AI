graph={
    'M':['N','Q','R'],
    'N':['O','Q','M'],
    'R':['M'],
    'O':['P','N'],
    'Q':['M','N'],
    'P':['O','Q']
    }
def dfs(g,n,seen,d):
    if n not in seen:
        seen.append(n)
        for i in g[n]:
            if seen[-1] is d:
                break
            dfs(g,i,seen,d)
    return seen
print(dfs(graph,'M',[],'R'))

###
graph = {
    'M': ['N','Q','R'],
    'N': ['O','Q','M'],
    'R': ['M'],
    'O': ['P','N'],
    'Q': ['M','N'],
    'P': ['O','Q']
}

def dfs(g, n, seen, d):
    if n not in seen:
        seen.append(n)
        for i in g[n]:
            if seen[-1] == d:  # use == instead of 'is'
                break
            dfs(g, i, seen, d)
    return seen

# Taking input from user
start_node = input("Enter the starting node: ")
stop_node = input("Enter the node to stop at: ")

result = dfs(graph, start_node, [], stop_node)
print("DFS traversal:", result)
