from models import perceptron

perceptron.setup(2, 0.1, 5)

# OR
print("OR")
dataset = [[0, 0, 0],
	[0, 1, 1],
	[1, 0, 1],
	[1, 1, 1]]
perceptron.train(dataset)
print('1 OR 1 = %d' % (perceptron.predict([1, 1])))
print('1 OR 0 = %d' % (perceptron.predict([1, 0])))
print('0 OR 1 = %d' % (perceptron.predict([0, 1])))
print('0 OR 0 = %d' % (perceptron.predict([0, 0])))


# AND
print("\nAND")
dataset = [[0, 0, 0],
	[0, 1, 0],
	[1, 0, 0],
	[1, 1, 1]]
perceptron.train(dataset)
print('1 AND 1 = %d' % (perceptron.predict([1, 1])))
print('1 AND 0 = %d' % (perceptron.predict([1, 0])))
print('0 AND 1 = %d' % (perceptron.predict([0, 1])))
print('0 AND 0 = %d' % (perceptron.predict([0, 0])))
