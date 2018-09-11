# 배치 처리

x, _ = get_data()
network = init_network()
W1, W2, W3 = network['W1'], network['W2'], network['W3']

x.shape
# (10000, 784)
x[0].shape
# (784,)
W1.shape
# (784, 50)
W2.shape
# (50, 100)
W3.shape
# (100, 10)
