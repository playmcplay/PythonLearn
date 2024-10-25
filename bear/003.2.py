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

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # 初始化父节点列表
        self.rank = [1] * size  # 初始化秩（用于优化合并）

    def find(self, u):
        if self.parent[u] != u:  # 路径压缩
            self.parent[u] = self.find(self.parent[u])  # 递归找到根节点
        return self.parent[u]  # 返回根节点

    def union(self, u, v):
        root_u = self.find(u)  # 找到u的根节点
        root_v = self.find(v)  # 找到v的根节点
        if root_u != root_v:  # 如果根节点不同，合并
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u  # 使rank高的根成为新根
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u  # 随机选择一个根
                self.rank[root_u] += 1  # 更新秩

def kruskal(graph):
    edges = sorted(graph.edges, key=lambda x: x[0])  # 按权重排序边
    uf = UnionFind(graph.num_nodes)  # 创建并查集实例
    mst_edges = []  # 存储最小生成树的边
    total_weight = 0  # 记录总权重

    for weight, u, v in edges:  # 遍历每条边
        if uf.find(u) != uf.find(v):  # 如果u和v不在同一集合中
            uf.union(u, v)  # 合并集合
            mst_edges.append((weight, u, v))  # 记录边
            total_weight += weight  # 加入权重

    return mst_edges  # 返回最小生成树的边集合

def run_kruskal(num_nodes):
    graph = Graph(num_nodes)  # 创建图实例
    mst = kruskal(graph)  # 计算最小生成树
    return graph.num_nodes, len(graph.edges), mst  # 返回节点数、边数和生成树边

# 示例用法
num_nodes = 10  # 定义节点数量
nodes, edges, mst = run_kruskal(num_nodes)
print(f"Kruskal Algorithm: Nodes = {nodes}, Edges = {edges}, MST Edges = {mst}")
