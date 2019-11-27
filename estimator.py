class Estimator:

    def __init__(estimator_type):
        if estimator_type == 'linreg':
            from sklearn.linear_model import LinearRegression
            self.learner = LinearRegression()

    def trainer(start_date, end_date, tickers, data):
        '''
        INPUT - start and end date for date, list of tickers, and the data set

        OUTPUT - a dictionary mapping each ticker to its trained model
        '''
        train_data = {}
        
        for ticker in tickers:
            try:
                xy = []

                frame = data[(data.ticker == ticker) & (data.date <= end_date) &
                (data.date >= start_date)]

                xy[0] = frame[['open', 'high', 'low', 'close', 'volume']]
                
                xy[1] = frame[['adj_close']]

            except:
                print('No such date available in the dataset. Choose dates again.')

        models = {}

        for ticker in tickers:
            X, y = train_data[ticker][0], train_data[ticker][1]
            models[ticker] = LinearRegression().fit(X,y)
        
        return models

        