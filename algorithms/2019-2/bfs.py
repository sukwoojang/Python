adj_list = [[2, 1], [3, 0], [3, 0], [9, 8, 2, 1], 
            [5], [7, 6, 4], [7, 5], [6, 5], [3], [3]]  
N = len(adj_list) 
visited = [False for x in range(N+1)]
 
def bfs(i):
    queue = [] # 큐 선언 (리스트로 큐 구현)
    visited[i] = True
    queue.append(i) # 큐에 시작정점 삽입        
    while len(queue) != 0: 
        v = queue.pop(0) # 큐에서 정점 v를 가져옴 
        print(v, ' ', end='') # 정점 v 출력
        for w in adj_list[v]: # 정점 v에 인접한 방문 안된 정점에 대해
            if not visited[w]: 
                visited[w] = True
                queue.append(w) # v에 인접한 정점을 큐에 삽입

print('BFS 방문 순서:')
for i in range(N):
    if not visited[i]:
        bfs(i)