import numpy as np

def grey_relational_analysis(data):
    """
    灰色关联分析函数
    :param data: 输入数据，二维数组，每一列代表一个变量
    :return: 关联度矩阵
    """
    # 数据标准化
    data = data / data[0, :]

    # 参考序列（第一列）
    reference_sequence = data[:, 0]

    # 计算差序列
    diff_matrix = np.abs(data - reference_sequence.reshape(-1, 1))

    # 计算最小差和最大差
    min_diff = np.min(diff_matrix)
    max_diff = np.max(diff_matrix)

    # 分辨系数
    rho = 0.5

    # 计算关联系数
    relational_coefficient = (min_diff + rho * max_diff) / (diff_matrix + rho * max_diff)

    # 计算关联度
    relational_degree = np.mean(relational_coefficient, axis=0)

    return relational_degree

# 示例数据
data = np.array([
    [10, 12, 15],
    [11, 13, 16],
    [12, 14, 17],
    [13, 15, 18],
    [14, 16, 19]
])

# 进行灰色关联分析
result = grey_relational_analysis(data)

# 输出结果
print("关联度：", result)