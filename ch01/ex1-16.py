# 원소 접근

import numpy as np

X = np.array([[51, 55], [14, 19], [0, 4]])
print(X)
X[0]      # 0행
X[0][1]   # (0, 1) 위치의 원소


for row in X:
    print(row)


X = X.flatten()         # x를 1차원 배열로 변환(평탄화)
print(X)
X[np.array([0, 2, 4])]  # 인덱스가 0, 2, 4인 원소 얻기


X > 15
X[X>15]

