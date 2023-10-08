import pandas
import numpy

class DataPreparation:
	def __init__(self, path_to_csv,):
		self.dataset_df = pandas.read_csv(path_to_csv, sep=',')
		self.get_prepared_data()


	def get_prepared_data(self):
		self.add_index_time_column()
		self.standard_normalisation()
		self.split_dataset()


	def add_index_time_column(self):
		self.dataset_df["index_time"] = numpy.arange(1, len(self.dataset_df)+1, 1)



	def standard_normalisation(self):
		self.dataset_mean = self.dataset_df["passengers"].mean()
		self.dataset_std = self.dataset_df["passengers"].std()
		
		self.dataset_df["passengers"] = (self.dataset_df["passengers"] - self.dataset_mean)/self.dataset_std



	def split_dataset(self):
		dataset_length = len(self.dataset_df)
		index_split = int(dataset_length*0.75)

		train_df = self.dataset_df[ : index_split]
		test_df = self.dataset_df[index_split: ]


		self.x_train = train_df[["index_time"]].values
		self.y_train = train_df[["passengers"]].values


		self.x_test = test_df[["index_time"]].values
		self.y_test = test_df[["passengers"]].values