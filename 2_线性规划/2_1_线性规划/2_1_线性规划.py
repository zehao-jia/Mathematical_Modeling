'''某工厂生产两种产品 A 和 B,需使用三种资源：劳动力、原材料和设备。
生产每件产品 A 需要 2 小时劳动力、3 千克原材料和 1 小时设备时间，利润为 50 元；
生产每件产品 B 需要 3 小时劳动力、2 千克原材料和 2 小时设备时间，利润为 80 元。
工厂每日可用资源为：劳动力不超过 120 小时，原材料不超过 150 千克，设备时间不超过 80 小时。
试建立线性规划模型，确定每日生产计划使总利润最大。'''

import numpy as np
from scipy.optimize import linprog

c=np.array([-50,-80])#目标函数系数
A_ub=np.array([[2,3],[3,2],[1,2]])#不等式约束系数
b_ub=np.array([120,150,80])#不等式约束值
bounds=[[0,50],[0,40]]#变量上下界
result=linprog(c=c,A_ub=A_ub,b_ub=b_ub,bounds=bounds)

y1=result.x
y2=-(result.fun)
print('最优解为：')
print(y1)
print('最大利润为：')
print(y2)