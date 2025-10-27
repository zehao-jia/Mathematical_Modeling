# kmeans介绍
- kmeans分为三个步骤:
- 1. 选择初始质心,基本的方法是从x个样本中选择k个样本,kmeans的实现由其他两个步骤的循环组成
- 2. 将每个样本分配到离他最近的质心
- 3. 通过取分配给每个质心的样本的平均值创建新的质心,计算新的质心之间的差异,重复最后的步骤,直到该值小于阈值,质心不在显著移动

## 1. 数据准备与预处理
- kmeans的计算对数据尺度敏感,需要先标准化(均值为0方差为1)

## 2. 实际数据处理
data = pd.read_csv('your_data.csv')
- 提取特征列（假设所有列都是特征，无需标签）
X = data.values  # 转换为numpy数组

- 数据标准化（关键步骤！）
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)  # 标准化后的特征矩阵

## 3.确定最佳k值
- K-Means 需要提前指定聚类数K，常用肘部法（Elbow Method）选择最佳K：
- 原理：计算不同K对应的误差平方和（SSE，簇内总距离），SSE 随K增大而减小，当K超过某个值后 SSE 下降变缓，形成 “肘部”，该点即为最佳K。

## 关键参数:
```python
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
```


# 注意
1. 记得数据标准化
2. k值的选择,肘部法是基础,但也要结合实际
3. kmeans对非球形簇和密度差异大的簇效果较差,可尝试DBSCAN算法
