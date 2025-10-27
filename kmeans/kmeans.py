import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans  # K-Means聚类算法
from sklearn.preprocessing import StandardScaler  # 数据标准化（重要！）
from sklearn.datasets import make_blobs  # 用于生成模拟数据（可选）

# 设置字体为SimHei（黑体），支持中文显示
plt.rcParams["font.family"] = ["SimHei"]
# 解决负号显示问题（可选）
plt.rcParams['axes.unicode_minus'] = False  # 正确显示负号

# 生成1000个样本，4个真实聚类中心，2个特征
X, y_true = make_blobs(n_samples=1000, centers=4, n_features=2, random_state=42)
# 转换为DataFrame方便查看
data = pd.DataFrame(X, columns=['feature1', 'feature2'])
print(data.head())

# # 加载数据
# data = pd.read_csv('your_data.csv')
# # 提取特征列（假设所有列都是特征，无需标签）
# X = data.values  # 转换为numpy数组

# 数据标准化（关键步骤！）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # 标准化后的特征矩阵

## 使用肘部法确定最佳k值
# 测试K=1到10的效果
sse = []
k_range = range(1, 11)
for k in k_range:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    sse.append(kmeans.inertia_)  # inertia_即SSE

# 绘制肘部图
plt.figure(figsize=(8, 4))
plt.plot(k_range, sse, 'bo-')
plt.xlabel('K (聚类数)')
plt.ylabel('SSE (簇内误差平方和)')
plt.title('肘部法确定最佳K值')
plt.show()

# 设定最佳K值（根据肘部图选择）
best_k = 4

# 初始化并训练模型
kmeans = KMeans(
    n_clusters=best_k,  # 聚类数
    init='k-means++',  # 智能初始化 centroids（避免随机偏差）
    n_init=10,  # 多次初始化取最优结果（默认10，避免局部最优）
    max_iter=300,  # 最大迭代次数
    random_state=42  # 固定随机种子，保证结果可复现
)

# 拟合数据并预测聚类标签
y_pred = kmeans.fit_predict(X_scaled)  # y_pred为每个样本的聚类标签（0,1,...,K-1）

# 将标签添加到原数据中
data['cluster'] = y_pred
print(data.head())

plt.figure(figsize=(8, 6))
# 绘制每个簇的点
for cluster in range(best_k):
    cluster_data = data[data['cluster'] == cluster]
    plt.scatter(
        cluster_data['feature1'], 
        cluster_data['feature2'],
        label=f'簇 {cluster}',
        alpha=0.7  # 透明度
    )

# 绘制聚类中心（centroids）
centroids = kmeans.cluster_centers_
# 注意：centroids是标准化后的坐标，如需还原为原始尺度，需用scaler.inverse_transform
centroids_original = scaler.inverse_transform(centroids)
plt.scatter(
    centroids_original[:, 0], 
    centroids_original[:, 1], 
    s=200,  # 点大小
    c='black', 
    marker='X', 
    label='聚类中心'
)

plt.xlabel('特征1')
plt.ylabel('特征2')
plt.title(f'K-Means聚类结果 (K={best_k})')
plt.legend()
plt.show()