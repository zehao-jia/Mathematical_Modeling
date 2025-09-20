'''一家工厂生产两种产品：产品 A 和产品 B。生产产品 A 每件需要
 2 小时的劳动力和 3 单位的原材料，生产产品 B 每件需要 3 小时的
 劳动力和 2 单位的原材料。工厂每周有 60 小时的劳动力和 50 单位
 的原材料可用。产品 A 每件的利润是 40 元，产品 B 每件的利润是 30 元。
请问工厂每周应该生产多少件产品 A 和产品 B 才能使总利润最大化？'''

import pulp
from pulp import LpProblem, LpVariable, LpMaximize, LpStatus, lpSum, LpBinary

problem = LpProblem("example", LpMaximize)
#设生产产品A为x1，产品B为x2
x1 = LpVariable("x1", lowBound=0, cat=pulp.LpInteger)
x2 = LpVariable("x2", lowBound=0, cat=pulp.LpInteger)

#目标函数
problem += 40*x1 + 30*x2

#约束条件
problem += 2*x1 + 3*x2 <= 60
problem += 3*x1 + 2*x2 <= 50

#求解
problem.solve()
print("Status:", LpStatus[problem.status])#输出结果状态
print("x1:", x1.varValue)#产品A的产量
print("x2:", x2.varValue)#产品B的产量
