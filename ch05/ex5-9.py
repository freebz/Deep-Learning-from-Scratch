# Affine 계층

X = np.random.rand(2)   # 입력
W = np.random.rand(2,3) # 가중치
B = np.random.rand(3)   # 편향

X.shape # (2,)
W.shape # (2, 3)
B.shape # (3,)

Y = np.dot(X, W) + B
