import numpy as np
A=np.array([[1,2,3,5],[1/2,1,1/2,2],[1/3,2,1,2],[1/5,1/2,1/2,1]])
eig_val,eig_vec=np.linalg.eig(A)#特征值和特征向量
lamda=max(eig_val)#最大特征值


#一致性检验
CI=(lamda-np.shape(A)[0])/(np.shape(A)[0]-1)#CI
RI=np.array([0,0,0.58,0.9,1.12,1.24,1.32,1.41,1.45,1.49,1.51])#RI
CR=CI/RI[(np.shape(A)[0])-1]#CR
if CR<0.1:
    print ('通过')
else:
    print ('不通过')

#求权重
b=A.sum(axis=0)#按列求和
copy_a=A.copy()
copy_a=copy_a/b
copy_a=np.sum(copy_a,axis=1)#按行求和
w=copy_a/np.sum(copy_a)#归一化
print (w)

tar_1 = np.array([1, 4, 12, 14])
tar_2 = np.array([2, 4, 6, 8])
tar_1 = tar_1/np.sum(tar_1)
tar_2 = tar_2/np.sum(tar_2)

grades_1 = (tar_1*w).sum()
grades_2 = (tar_2*w).sum()

print (grades_1)
print (grades_2)