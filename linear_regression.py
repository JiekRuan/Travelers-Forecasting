
class LinearRegression:
	def __init__(self, data_preparation_object):
		self.data_preparation_object = data_preparation_object
		self.a = 0 # it's coeff
		self.b = 0 # it's bias

	def fit(self, learning_rate, epochs):
		
		x_train = self.data_preparation_object.x_train
		y_train = self.data_preparation_object.y_train
		
		x_test = self.data_preparation_object.x_test
		y_test = self.data_preparation_object.y_test

		train_length = len(x_train)
		test_length = len(x_test)

		forecast = lambda index_time : self.a * index_time + self.b
		mse = lambda x_list, y_list : 1/(train_length) * sum([(forecast(x_i) - y_i)**2 for x_i, y_i in zip(x_list, y_list)])


		for index_epoch in range(epochs): # une itération de cette boucle for est une backprogation
			dmse_da = 2/(train_length) * sum([x_i * (forecast(x_i) - y_i) for x_i, y_i in zip(x_train, y_train)])
			dmse_db = 2/(train_length) * sum([(forecast(x_i) - y_i) for x_i, y_i in zip(x_train, y_train)])

			self.a = self.a - learning_rate * dmse_da
			self.b = self.b - learning_rate * dmse_db