import numpy as np
import matplotlib.pyplot as plt
from pymoo.core.problem import ElementwiseProblem
from pymoo.algorithms.moo.nsga2 import NSGA2
from pymoo.optimize import minimize
from pymoo.visualization.scatter import Scatter

# 多目标规划问题：资源分配优化
# 题目描述：
# 某公司计划分配两种资源到两个项目A和B，需同时优化以下目标：
# 1. 最大化总收益（万元）
# 2. 最小化总风险（风险指数，越小越好）
#
# 已知条件：
# - 项目A：每投入1单位资源产生5万元收益，伴随2单位风险
# - 项目B：每投入1单位资源产生3万元收益，伴随1单位风险
# - 总资源限制：两种项目投入的资源总和不超过10单位
# - 单个项目最低投入：每个项目至少投入2单位资源
# - 资源投入为非负实数（可分拆）
#
# 决策变量：
# x：分配给项目A的资源数量
# y：分配给项目B的资源数量
#
# 数学模型：
# 目标函数：
#   1. 最大化收益 f1(x,y) = 5x + 3y
#   2. 最小化风险 f2(x,y) = 2x + y
# 约束条件：
#   1. x + y ≤ 10 （总资源限制）
#   2. x ≥ 2, y ≥ 2 （单个项目最低投入）
#   3. x ≥ 0, y ≥ 0 （非负约束）


# 定义多目标优化问题
class ResourceAllocationProblem(ElementwiseProblem):
    def __init__(self):
        # 初始化问题：2个决策变量，2个目标函数，1个不等式约束
        super().__init__(
            n_var=2,          # 决策变量数量
            n_obj=2,          # 目标函数数量
            n_ieq_constr=1,   # 不等式约束数量
            xl=np.array([2.0, 2.0]),  # 变量下界（x≥2, y≥2）
            xu=np.array([8.0, 8.0])   # 变量上界（根据总资源约束推导）
        )

    def _evaluate(self, x, out, *args, **kwargs):
        x_a, x_b = x  # x_a为项目A资源，x_b为项目B资源
        
        # 目标函数：
        # 目标1（收益）需最大化，pymoo默认最小化，因此取负值
        f1 = -(5 * x_a + 3 * x_b)
        # 目标2（风险）需最小化，直接计算
        f2 = 2 * x_a + x_b
        
        # 约束条件：转为 ≤ 0 的形式（pymoo要求）
        # 约束1：x + y ≤ 10 → x + y - 10 ≤ 0
        g1 = (x_a + x_b) - 10
        
        out["F"] = [f1, f2]  # 目标函数结果
        out["G"] = [g1]       # 约束条件结果


# 初始化问题和算法（NSGA-II是多目标优化的经典算法）
problem = ResourceAllocationProblem()
algorithm = NSGA2(pop_size=50)  # 种群大小为50

# 运行优化
result = minimize(
    problem,
    algorithm,
    termination=('n_gen', 100),  # 迭代100代
    seed=42,                     # 随机种子，保证结果可复现
    verbose=False
)

# 处理结果（将收益目标转回正值）
pareto_front = []
for f in result.F:
    profit = -f[0]  # 还原为最大化的收益值
    risk = f[1]
    pareto_front.append((profit, risk))

# 输出帕累托最优解
print("帕累托最优解：")
print("收益(万元) | 风险指数 | 项目A资源 | 项目B资源")
print("-" * 50)
for i in range(len(result.X)):
    x, y = result.X[i]
    profit, risk = pareto_front[i]
    print(f"{profit:10.2f} | {risk:9.2f} | {x:11.2f} | {y:11.2f}")

# 可视化帕累托前沿
plot = Scatter(title="资源分配的帕累托前沿", labels=["风险指数", "收益(万元)"])
plot.add(np.array(pareto_front), color="red")
plot.show()