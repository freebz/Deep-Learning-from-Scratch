net = TwoLayerNet(input_size=784, hidden_size=100, output_size=10)
net.params['W1'].shape # (784, 100)
net.params['b1'].shape # (100,)
net.params['W2'].shape # (100, 10)
net.params['b2'].shape # (10,)


x = np.random.rand(100, 784) # 더미 입력 데이터(100장 분량)
y = net.predict(x)
