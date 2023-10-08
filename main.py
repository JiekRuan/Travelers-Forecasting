import data_preparation
import linear_regression


path_to_csv = "/home/pita/Documents/python_projects/linear_regression/number of travelers.csv"

data_preparation_object = data_preparation.DataPreparation(path_to_csv)
linear_regression_object = linear_regression.LinearRegression(data_preparation_object)
linear_regression_object.fit(learning_rate=0.00001, epochs=1000)