class Estimator:

    def __init__(self, estimator_type, trainstart, trainend, 
                tickers_list, dataset):
        '''
        Constructor that takes in the type of estimator as a parameter
        As well as start and end dates for test and train data, the dataset
        and the list of tickers
        '''
        if estimator_type == 'linreg':
            self.learner = LinearRegression()
        if estimator_type == 'knn':
            self.learner = KNeighborsRegressor()
        if estimator_type == 'gbr':
            self.learner = GradientBoostingRegressor()
        if estimator_type == 'rfr':
            self.learner = RandomForestRegressor()

        self.train_start = trainstart
        self.train_end = trainend

        self.tickers = tickers_list
        self.data = dataset
        self.models = []
        self.predicts = []
        
    def get_data(self, start_date, end_date, ticker):
        '''
        INPUT - self

        OUTPUT - X and y as features and labels
        '''
        try:

            frame = self.data[(self.data.ticker == ticker) & 
            (self.data.date <= end_date) & (self.data.date >= start_date)]

            X = frame[['open', 'high', 'low', 'close', 'volume']]
                
            y = np.ravel(frame[['adj_close']])

        except:
            print('No such date available in the dataset. Choose dates again.')
        
        return X, y


    def train(self):
        '''
        INPUT - self

        OUTPUT - Returns True when models are succesfully learned
        '''

        for ticker in self.tickers:
            X, y  = self.get_data(self.train_start, self.train_end, ticker)
            model = self.learner.fit(X,y)
            self.models.append((ticker, model))
        
        return True

    def test(self, start, end):
        '''
        INPUT - start and end date for test data as well as list of tickers

        OUTPUT - returns true when test is done successfully
        '''
        for ticker in self.tickers:
            Xtest, ytest = self.get_data(start, end, ticker)
            try:
                model = [item[1] for item in self.models if item[0] == ticker][0]
            except:
                print('Something about ticker consistency not right!')
            self.predicts.append((ticker, model.predict(Xtest)))

        return True

    def show_results(self, start, end):
        '''
        INPUT - self

        OUPUT - Outputs the train and test results
        '''

        self.train()

        for tm in self.models:
            X, y = self.get_data(start, end, ticker = tm[0])
            print("R-squared on test data for {} between {} and {} is {}".format(
                tm[0], self.test_start, self.test_end,
                tm[1].score(X,y)))

