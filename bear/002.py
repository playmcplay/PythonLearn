import numpy as np

# 定义节点邻接关系
adjacency_list = {
    1: ['2', '3'],
    2: ['1', '3', '4', '5'],
    3: ['1', '2', '5', '7', '8'],
    4: ['2', '5'],
    5: ['2', '3', '4', '6'],
    6: ['5'],
    7: ['3', '8'],
    8: ['3', '7'],
    9: ['10'],
    10: ['9', '11'],
    11: ['10'],
}

# 输出邻接关系
for node, neighbors in adjacency_list.items():
    print(f"{node} {neighbors}")

# 创建邻接矩阵
n = len(adjacency_list)
A = np.zeros((n, n), dtype=int)

# 填充邻接矩阵
for node, neighbors in adjacency_list.items():
    for neighbor in neighbors:
        A[node-1][int(neighbor)-1] = 1

# 输出A的幂
A_power = A.copy()
for i in range(1, 11):
    print(f"A^{i}:\n{A_power}\n")
    A_power = np.dot(A_power, A)
