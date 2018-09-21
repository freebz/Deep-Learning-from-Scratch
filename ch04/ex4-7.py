# 미분

# 나쁜 구현의 예
def numerical_diff(f, x):
    h = 10e-50
    return (f(x + h) - f(x)) / h


np.float32(1e-50)
# 0.0


def numerical_diff(f, x):
    h = 1e-4 #0.0001
    return (f(x+h) - f(x-h)) / (2*h)
