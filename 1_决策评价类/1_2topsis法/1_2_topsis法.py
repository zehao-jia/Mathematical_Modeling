'''题目描述：企业综合竞争力评估
企业的综合竞争力受到多个维度因素的影响。现收集了 5 家企业在 4 种不同类型指标上的数据，需使用 TOPSIS(Technique for Order Preference by Similarity to Ideal Solution）法对这 5 家企业的综合竞争力进行评估和排名。
指标说明
市场占有率（）：反映企业在市场中的地位，属于正向指标（极大性指标），数值越大表示企业市场竞争力越强。
次品率（）：衡量企业产品质量的稳定性，是负向指标（极小性指标），数值越小意味着产品质量越好。
员工满意度（）：该指标存在一个合适的区间，当员工满意度处于  时，企业的运营状态较为良好，属于区间性指标。
企业与行业平均规模比值（）：期望该比值接近 1，属于中间型指标，越接近 1 表示企业规模与行业平均规模越匹配。
数据信息
企业编号	市场占有率（%，）	次品率（%，）	员工满意度（%，）	企业与行业平均规模比值（）
企业 1	30	2	75	0.9
企业 2	35	1.5	80	1.1
企业 3	25	2.5	65	0.8
企业 4	40	1	90	1.2
企业 5	28	1.8	72	0.95
任务要求
使用 Python 编写代码实现 TOPSIS 法，对 5 家企业的综合竞争力进行评估。
针对不同类型的指标（极大性、极小性、区间性、中间型）进行相应的数据预处理。
计算每家企业与正理想解和负理想解的距离，并计算相对贴近度。
根据相对贴近度对企业进行排名，相对贴近度越高，说明该企业的综合竞争力越强。
输出每家企业的相对贴近度和排名结果。'''
import numpy as np
def min_to_max(maxx,x):
    x=list(x)
    ans=[[(maxx-i)] for i in x]
    return np.array(ans)

def mid_to_max(bestx,x):
    x=list(x)
    h=[abs(bestx-i) for i in x]
    M=max(h)
    if M==0:
        m=1
    ans=[(1-i/M) for i in h]
    return np.array(ans)

def reg_to_max(low,high,x):
    x=list(x)
    M=max(low-min(x),max(x)-high)
    ans=[]
    if M==0:
        M=1
    for i in range(len(x)):
        if x[i]<low:
            ans.append(1-((low-x[i])/M))
        elif x[i]>high:
            ans.append(1-((x[i]-high)/M))
        else:
            ans.append(1)
    return np.array(ans)

n=int(input("请输入参评数"))
m=int(input("请输入指标数"))
kind=input('请输入各指标的指标类型，中间用空格隔开，1：极大，2：极小，3：中间，4：区间').split(" ")

A=np.zeros((n,m))
for i in range(n):
    A[i]=input(f'请输入样品{i+1}的参数,其间以空格分').split(" ")
    A[i]=list(map(float,A[i]))


print(f'输入矩阵为：\n{A}')
X=np.zeros((n,1))
for i in range(m):
    if kind[i]=='1':
        v=A[:,i]
    elif kind[i]=='2':
        maxx=max(A[:,i])
        v=np.array(list(min_to_max(maxx,A[:,i])))
    elif kind[i]=='3':
        bestx=float(input('请输入中间值'))
        v=np.array(list(mid_to_max(bestx,A[:,i])))
    elif kind[i]=='4':
        low=float(input('请输入区间左端点'))
        high=float(input('请输入区间右端点'))
        v=np.array(list(reg_to_max(low,high,A[:,i])))
    if i==0:
        X=v.reshape(-1,1)
    else:
        X=np.hstack((X,v.reshape(-1,1)))

print(f'统一指标后，矩阵为、\n{X}')

X=X/np.sqrt(np.sum(X**2,axis=0))

print(f'标准化后的矩阵为\n{X}')

z_p=np.max(X,axis=0)
z_n=np.min(X,axis=0)

d_p=np.sqrt(np.sum(np.square(X-np.tile(z_p,(n,1))),axis=1))
d_n=np.sqrt(np.sum(np.square(X-np.tile(z_n,(n,1))),axis=1))
print(f'每个指标的最大值\n{z_p}')
print(f'每个指标的最小值\n{z_n}')
print(f'到最大值距离\n{d_p}')
print(f'到最小值距离\n{d_n}')

s_i=d_n/(d_p+d_n)
score=(s_i/sum(s_i))*100
for i in range(len(s_i)):
    print(f'第{i+1}个样本得分为{score[i]}\n')

