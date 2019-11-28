# Installation
Python 3 is used for coding. Packages used are numpy, pandas, and scikit-learn.

# Files
The estimator class is contained in `estimator.py`. This is the backbone of the analysis and contains the *Estimator* class with the required fields and methods. It follows the PEP8 guidelines.

The `expoloration.ipynb` is the jupyter notebook that was used throughout the project merely as scratch paper.

# Motivation
Using machine learning to predict stock adjusted closed price. We address the following questions:

1. What is the complexity of the underlying data generating process?
2. What machine learning algorithms perform better?
3. What can we conclude from the results?

# Descriptions

The approach taken in this project follows the CRISP-DM framework. Particularly, the following steps have been taken:

1. Business Understanding: The business understanding is motivated by and focused on the three questions discussed above. Mainly, we seek to predict adjusted close price based on a set of features and use supervised (regression) ML techniques to address the problem.

2. Data Understanding: We use the Quandl WIKI Prices [data](https://www.quandl.com/databases/WIKIP/documentation?anchor=database-overview) that contains information on stock prices, dividends and splits for 3000 US publicly-traded companies.

3. Data Preparation: Data is imported using Quandl python API.

4. Data Modeling: We use linear regression, Gradient Boosting Regressor, and Random Forest Regressor for modeling and training the data.

5. Evaluating results: The main metric for evaluation is R-squred on the train and test data to assess the learning as well as generalizability of the model. The Gradient Boosting model has the highest performance.

# Results
The findings are posted in this [article](https://medium.com/@sepehr.ramyar/stock-price-prediction-with-machine-learning-ddc4087ddecd) on medium.

# Acknowledgments
Credits to Quandl for the data.
