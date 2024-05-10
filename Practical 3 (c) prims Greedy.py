INF = 9999999
N = 5
G = [[0, 19, 5, 0, 0],
[19, 0, 5, 9, 2],
[5, 5, 0, 1, 6],
[0, 9, 1, 0, 1],
[0, 2, 6, 1, 0]]
selected_nodes = [0] * N
selected_nodes[0] = True
no_edges = 0
while(no_edges < N-1):
    minimum = INF
    a = 0
    b = 0
    for m in range(N):
        if selected_nodes[m]:
            for n in range(N):
                if((not selected_nodes[n]) and G[m][n]):
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + " -> " + str(b) + " : " + str(G[a][b]))
    selected_nodes[b] = True
    no_edges += 1
