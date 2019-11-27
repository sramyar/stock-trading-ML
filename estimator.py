class Estimator:

    def __init__(self, estimator_type):
        '''
        Constructor that takes in the type of estimator as a parameter
        '''
        if estimator_type == 'linreg':
            from sklearn.linear_model import LinearRegression
            self.learner = LinearRegression()

    def get_data(self, start_date, end_date, tickers, data):
        '''
        INPUT - start and end dates as well as list of tickers for the data

        OUTPUT - a dictionary mapping the data for each corresponding ticker
        '''
        dataset = {}
        
        for ticker in tickers:
            try:
                xy = []

                frame = data[(data.ticker == ticker) & (data.date <= end_date) &
                (data.date >= start_date)]

                xy.append(frame[['open', 'high', 'low', 'close', 'volume']])
                
                xy.append(frame[['adj_close']])

                dataset[ticker] = xy
            except:
                print('No such date available in the dataset. Choose dates again.')
                break
        
        return dataset


    def trainer(self, start_date, end_date, tickers, data):
        '''
        INPUT - start and end date for date, list of tickers, and the data set

        OUTPUT - a list of (ticker, trained model) pairs
        '''
        train_data = self.get_data(start_date, end_date, tickers, data)

        output = []

        for ticker in tickers:
            X, y = train_data[ticker][0], train_data[ticker][1]
            model = LinearRegression().fit(X,y)
            output.append((ticker, model))
        
        return output