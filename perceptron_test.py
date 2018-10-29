from models import perceptron

#OR
dataset = [[0, 0, 0],
           [0, 1, 1],
           [1, 0, 1],
           [1, 1, 1]]
weights = perceptron.generate_weights(2)
weights = perceptron.train(0.01, 100, dataset, weights)

print("Predictions for OR")
print('1 OR 1 = %d' % (perceptron.predict([1, 1], weights)))
print('1 OR 0 = %d' % (perceptron.predict([1, 0], weights)))
print('0 OR 1 = %d' % (perceptron.predict([0, 1], weights)))
print('0 OR 0 = %d' % (perceptron.predict([0, 0], weights)))

#AND
dataset = [[0, 0, 0],
	       [0, 1, 0],
	       [1, 0, 0],
	       [1, 1, 1]]
weights = perceptron.generate_weights(2)
weights = perceptron.train(0.1, 20, dataset, weights)

print("\nPredictions for AND")
print('1 AND 1 = %d' % (perceptron.predict([1, 1], weights)))
print('1 AND 0 = %d' % (perceptron.predict([1, 0], weights)))
print('0 AND 1 = %d' % (perceptron.predict([0, 1], weights)))
print('0 AND 0 = %d' % (perceptron.predict([0, 0], weights)))