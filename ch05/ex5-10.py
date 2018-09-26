# 배치용 Affine 계층

X_dot_W = np.array([[0, 0, 0], [10, 10, 10]])
B = np.array([1, 2, 3])

X_dot_W
# array([[ 0,  0,  0],
#        [10, 10, 10]])
X_dot_W + B
# array([[ 1,  2,  3],
#        [11, 12, 13]])


dY = np.array([[1, 2, 3], [4, 5, 6]])
dY
# array([[1, 2, 3],
#        [4, 5, 6]])

dB = np.sum(dY, axis=0)
dB
# array([5, 7, 9])
