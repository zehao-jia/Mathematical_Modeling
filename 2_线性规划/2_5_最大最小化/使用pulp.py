'''某工厂生产两种产品 A 和 B，生产这两种产品需要用到两种原材料甲和乙
。生产一件产品 A 需要 3 单位的甲材料和 2 单位的乙材料，生产一件产品 B 
需要 2 单位的甲材料和 4 单位的乙材料。工厂每天可使用的甲材料最多为 120
 单位，乙材料最多为 160 单位。产品 A 每件的利润为 50 元，
 产品 B 每件的利润为 60 元。现在要求在满足原材料限制的条件下，
 安排生产产品 A 和产品 B 的数量，
使得生产过程中单位利润最小的产品的总利润最大化。'''

from pulp import LpMaximize, LpProblem, LpVariable

# 创建问题实例，目标是最大化
prob = LpProblem("Maximize_Min_Profit", LpMaximize)

# 定义决策变量
x = LpVariable("x", lowBound=0, cat="Integer")  # 产品 A 的生产数量
y = LpVariable("y", lowBound=0, cat="Integer")  # 产品 B 的生产数量
z = LpVariable("z", lowBound=0, cat="Integer")  # 引入辅助变量 z 表示 min(50x, 60y)

# 定义目标函数
prob += z

# 定义约束条件
prob += 50 * x >= z  # z <= 50x
prob += 60 * y >= z  # z <= 60y
prob += 3 * x + 2 * y <= 120  # 甲材料限制
prob += 2 * x + 4 * y <= 160  # 乙材料限制

# 求解问题
prob.solve()

# 输出结果
print("Status:", prob.status)
print("最优解：")
print(f"产品 A 的生产数量: {x.value()}")
print(f"产品 B 的生产数量: {y.value()}")
print(f"最小单位利润产品的最大总利润: {z.value()}")