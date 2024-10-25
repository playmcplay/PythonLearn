import random
import heapq

class Graph:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes  # 初始化节点数量
        self.edges = []  # 存储边的列表
        self.adj_list = {i: [] for i in range(num_nodes)}  # 邻接列表
        self._generate_random_graph()  # 生成随机图

    def _generate_random_graph(self):
        # 生成无向加权图的边
        for i in range(self.num_nodes):
            for j in range(i + 1, self.num_nodes):
                weight = random.randint(1, 10)  # 随机生成边的权重
                self.edges.append((weight, i, j))  # 将边加入边列表
                self.adj_list[i].append((j, weight))  # 更新邻接列表
                self.adj_list[j].append((i, weight))  # 更新邻接列表

    def prim(self):
        mst_edges = []  # 存储最小生成树的边
        visited = [False] * self.num_nodes  # 记录访问过的节点
        min_heap = [(0, 0)]  # 最小堆，初始化为第一个节点，权重为0
        total_weight = 0  # 记录总权重

        while min_heap:
            weight, u = heapq.heappop(min_heap)  # 从堆中取出权重最小的边
            if visited[u]:  # 如果节点已经访问，跳过
                continue
            visited[u] = True  # 标记节点为已访问
            total_weight += weight  # 加入权重

            for v, w in self.adj_list[u]:  # 遍历邻接节点
                if not visited[v]:  # 如果邻接节点未被访问
                    heapq.heappush(min_heap, (w, v))  # 将边加入堆
                    mst_edges.append((weight, u, v))  # 记录边

        return mst_edges  # 返回最小生成树的边集合


def run_prim(num_nodes):
    graph = Graph(num_nodes)  # 创建图实例
    mst = graph.prim()  # 计算最小生成树
    return graph.num_nodes, len(graph.edges), mst  # 返回节点数、边数和生成树边


# 示例用法
num_nodes = 10
nodes, edges, mst = run_prim(num_nodes)
print(f"Prim Algorithm: Nodes = {nodes}, Edges = {edges}, MST Edges = {mst}")
