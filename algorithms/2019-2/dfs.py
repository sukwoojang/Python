adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], 
            [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]  
N = len(adj_list) # 그래프 정점 수
visited = [False for x in range(N+1)] # 방문되면 True로
 
def dfs(v):
    visited[v] = True # 정점 v 방문
    print(v, ' ', end='') # 정점 v 출력
    for w in adj_list[v]: # 정점 v에 인접한 각 정점에 대해
        if not visited[w]: 
            dfs(w) # v에 인접한 방문 안된 정점 재귀호출

print('DFS 방문 순서:')     
for i in range(N): 
    if not visited[i]: 
        dfs(i)