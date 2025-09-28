"""问题描述
某公司要对 5 个投资项目（项目 A、项目 B、项目 C、项目 D、项目 E）进行综合评价，考虑了 4 个评价指标：投资回报率（）、市场占有率（）、技术创新性（）、管理团队能力（）。以下是这 5 个项目在 4 个指标上的表现数据：
项目	投资回报率（）	市场占有率（）	技术创新性（）	管理团队能力（）
A	0.15	0.20	0.30	0.25
B	0.12	0.25	0.25	0.30
C	0.18	0.15	0.35	0.20
D	0.10	0.30	0.20	0.35
E	0.20	0.10	0.40	0.15"""

import numpy as np
m=5
n=4
def mylog(arr):
    a_arr=np.zeros(shape=arr.shape)
    for i in range(len(arr)):
        if(arr[i]==0):
            a_arr[i]=1
        else:
            a_arr[i]=np.log(arr[i])
    return a_arr

X = np.array([[0.15, 0.20, 0.30, 0.25],
              [0.12, 0.25, 0.25, 0.30],
              [0.18, 0.15, 0.35, 0.20],
              [0.10, 0.30, 0.20, 0.35],
              [0.20, 0.10, 0.40, 0.15]])

x_min=np.min(X,axis=0)
x_max=np.max(X,axis=0)

x_normalized=X/np.sqrt(np.sum(X*X,axis=0))

p=x_normalized/np.sum(x_normalized,axis=0)

d=np.zeros(n)
for i in range(n):
    x=X[:,i]
    e=-np.sum(x*np.log(x))/np.log(n)
    d[i]=1-e
w=np.zeros(n)
for i in range(n):
    w[i]=d[i]/np.sum(d)
print(w)
