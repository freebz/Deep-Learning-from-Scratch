f = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)
