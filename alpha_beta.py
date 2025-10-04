tree={
    'A':['B','C'],
    'B':[3,5],
    'C':[6,9]
    }
def minimax_alpha_beta(node,depth,alpha,beta,max_player):
    if depth==0:
        if node in tree:
            return tree[node][0] if max_player else tree[node][0]
        else:
            return node
    if max_player:
        value=float('-inf')
        for child in tree[node]:
            value=max(value,minimax_alpha_beta(child,depth -1,alpha,beta,False))
            alpha=max(alpha,value)
            if alpha>=beta:
                print(f"Pruning branch at node {node}")
                break
        return value
    else:
        value=float('inf')
        for child in tree[node]:
            value=min(value,minimax_alpha_beta(child,depth -1,alpha,beta,True))
            beta=min(beta,value)
            if beta<=alpha:
                print(f"Pruning branch at node {node}")
                break
        return value
best_score=minimax_alpha_beta('A',1,float('-inf'),float('inf'),True)
print(f"The best score is: {best_score}")

#####
tree = {
    'A': ['B','C'],
    'B': ['D','E'],
    'C': ['F','G'],
    'D': [3,5],
    'E': [6,9],
    'F': [1,2],
    'G': [0,4]
}

def minimax_alpha_beta(node, depth, alpha, beta, max_player):
    # Leaf node
    if isinstance(node, int):
        return node
    
    # If node points to leaf values
    if node in tree and all(isinstance(x, int) for x in tree[node]):
        return max(tree[node]) if max_player else min(tree[node])

    if max_player:
        value = float('-inf')
        for child in tree[node]:
            value = max(value, minimax_alpha_beta(child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)
            if alpha >= beta:
                print(f"Pruning branch at node {node}")
                break
        return value
    else:
        value = float('inf')
        for child in tree[node]:
            value = min(value, minimax_alpha_beta(child, depth - 1, alpha, beta, True))
            beta = min(beta, value)
            if beta <= alpha:
                print(f"Pruning branch at node {node}")
                break
        return value

# ---- Input ----
source = input("Enter the source node: ")
try:
    depth = int(input("Enter the depth to search: "))
except ValueError:
    depth = 3  # default for 3-level tree

best_score = minimax_alpha_beta(source, depth, float('-inf'), float('inf'), True)
print(f"The best score is: {best_score}")
