import numpy as np
import matplotlib.pyplot as plt

# 设置参数
c0 = 1
beta = 3

# 情况1: k ∈ [1, 10]
k1 = np.linspace(1, 10, 100)
p1 = c0 * k1 ** (-beta)
ln_p1 = np.log(p1)

# 情况2: k ∈ [1, 100]
k2 = np.linspace(1, 100, 100)
p2 = c0 * k2 ** (-beta)
ln_p2 = np.log(p2)

# 绘制p(k)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(k1, p1, label='p(k) = c0 * k^(-beta)')
plt.title('p(k) for k ∈ [1, 10]')
plt.xlabel('k')
plt.ylabel('p(k)')
plt.grid()
plt.legend()

# 绘制Ln(p(k))
plt.subplot(1, 2, 2)
plt.plot(k1, ln_p1, label='Ln(p(k)) = Ln(c0 * k^(-beta))', color='orange')
plt.title('Ln(p(k)) for k ∈ [1, 10]')
plt.xlabel('k')
plt.ylabel('Ln(p(k))')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()

# 绘制第二组情况
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(k2, p2, label='p(k) = c0 * k^(-beta)')
plt.title('p(k) for k ∈ [1, 100]')
plt.xlabel('k')
plt.ylabel('p(k)')
plt.grid()
plt.legend()

# 绘制Ln(p(k))
plt.subplot(1, 2, 2)
plt.plot(k2, ln_p2, label='Ln(p(k)) = Ln(c0 * k^(-beta))', color='orange')
plt.title('Ln(p(k)) for k ∈ [1, 100]')
plt.xlabel('k')
plt.ylabel('Ln(p(k))')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
