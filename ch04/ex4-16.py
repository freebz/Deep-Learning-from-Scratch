def f(W):
    return net.loss(x, t)

dW = numerical_gradient(f, net.W)
print(dW)
# [[ 0.52399681  0.01555913 -0.53955594]
#  [ 0.78599522  0.02333869 -0.80933391]]
