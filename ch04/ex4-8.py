# 수치 미분의 예

def function_1(x):
    return 0.01*x**2 +0.1*x


import numpy as np
import matplotlib.pylab as plt

x = np.arange(0.0, 20.0, 0.1) # 0에서 20까지 0.1 간격의 배열 x를 만든다.
y = function_1(x)
plt.xlabel("x")
plt.ylabel("f(x)")
plt.plot(x, y)
plt.show()


numerical_diff(function_1, 5)
# 0.1999999999990898
numerical_diff(function_1, 10)
# 0.2999999999986347
