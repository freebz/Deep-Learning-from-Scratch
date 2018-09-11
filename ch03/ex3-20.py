a = np.array([1010, 1000, 990])
np.exp(a) / np.sum(np.exp(a)) # 소프트맥스 함수의 계산
# array([nan, nan, nan])      # 제대로 계산되지 않는다.

c = np.max(a)                 # c = 1010 (최대값)
a - c
# array([  0, -10, -20])

np.exp(a - c) / np.sum(np.exp(a - c))
# array([9.99954600e-01, 4.53978686e-05, 2.06106005e-09])
