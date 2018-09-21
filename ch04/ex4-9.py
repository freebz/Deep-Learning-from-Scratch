# 편미분

def function_2(x):
    return x[0]**2 + x[1]**2
    # 또는 return np.sum(x**2)


def function_tmp1(x0):
    return x0*x0 + 4.0**2.0

numerical_diff(function_tmp1, 3.0)
# 6.00000000000378


def function_tmp2(x1):
    return 3.0**2.0 + x1*x1

numerical_diff(function_tmp2, 4.0)
# 7.999999999999119
