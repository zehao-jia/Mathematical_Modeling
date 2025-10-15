import numpy as np
import pandas as pd
from scipy.linalg import eigh

def pca(data, n_components):
    """
    实现主成分分析
    :param data: 输入数据，形状为 (n_samples, n_features)
    :param n_components: 保留的主成分数量
    :return: 降维后的数据
    """
    # 数据中心化
    mean = np.mean(data, axis=0)
    centered_data = data - mean

    # 计算协方差矩阵
    cov_matrix = np.cov(centered_data, rowvar=False)

    # 计算协方差矩阵的特征值和特征向量
    eigenvalues, eigenvectors = eigh(cov_matrix)

    # 对特征值进行降序排序，并获取对应的索引
    sorted_indices = np.argsort(eigenvalues)[::-1]
    sorted_eigenvalues = eigenvalues[sorted_indices]
    sorted_eigenvectors = eigenvectors[:, sorted_indices]

    # 选择前 n_components 个特征向量
    top_eigenvectors = sorted_eigenvectors[:, :n_components]

    # 数据投影到主成分上
    reduced_data = np.dot(centered_data, top_eigenvectors)

    return reduced_data

# 示例数据
data = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 4, 3, 2, 1],
    'feature3': [2, 3, 4, 5, 6]
})

# 提取数据矩阵
X = data.values

# 设置保留的主成分数量
n_components = 2

# 执行主成分分析
reduced_data = pca(X, n_components)

# 将降维后的数据转换为 DataFrame
reduced_df = pd.DataFrame(reduced_data, columns=[f'PC{i+1}' for i in range(n_components)])

print("降维后的数据：")
print(reduced_df)