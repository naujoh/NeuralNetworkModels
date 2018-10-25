from models import perceptron

# OR
print("OR")
perceptron.setup(2, 0.1, 5)
dataset = [[0, 0, 0],
	[0, 1, 1],
	[1, 0, 1],
	[1, 1, 1]]
perceptron.train(dataset)
print('1 OR 1 = %d' % (perceptron.predict([1, 1])))
print('1 OR 0 = %d' % (perceptron.predict([1, 0])))
print('0 OR 1 = %d' % (perceptron.predict([0, 1])))
print('0 OR 0 = %d' % (perceptron.predict([0, 0])))
perceptron.clear()


# AND
print("\nAND")
perceptron.setup(2, 0.1, 5)
dataset = [[0, 0, 0],
	[0, 1, 0],
	[1, 0, 0],
	[1, 1, 1]]
perceptron.train(dataset)
print('1 AND 1 = %d' % (perceptron.predict([1, 1])))
print('1 AND 0 = %d' % (perceptron.predict([1, 0])))
print('0 AND 1 = %d' % (perceptron.predict([0, 1])))
print('0 AND 0 = %d' % (perceptron.predict([0, 0])))
