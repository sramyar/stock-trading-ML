class Estimator:

    def __init__(self, estimator_type, trainstart, trainend, teststart,
                    testend, tickers_list, dataset):
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
        self.test_start = teststart
        self.test_end = testend

        self.tickers = tickers_list
        self.data = dataset
        self.models = []
        self.predicts = []
        
    def get_data(self, start_date, end_date, ticker):
        '''
        INPUT - self

        OUTPUT - a dictionary mapping the data for each corresponding ticker
        '''
        #dataset = {}
        
        #for ticker in self.tickers:
            try:
                xy = []

                frame = self.data[(self.data.ticker == ticker) & 
                (self.data.date <= end_date) & (self.data.date >= start_date)]

                xy.append(frame[['open', 'high', 'low', 'close', 'volume']])
                
                xy.append(frame[['adj_close']])

                #dataset[ticker] = xy

            except:
                print('No such date available in the dataset. Choose dates again.')
                break
        
        return xy #dataset


    def train(self):
        '''
        INPUT - self

        OUTPUT - Returns True when models are succesfully learned
        '''

        for ticker in self.tickers:
            train_data = self.get_data(self.train_start, self.train_end, ticker)
            X, y = train_data[0], train_data[1]
            model = self.learner.fit(X,y)
            self.models.append((ticker, model))
        
        return True

    def test(self):
        '''
        INPUT - start and end date for test data as well as list of tickers

        OUTPUT - returns true when test is done successfully
        '''

        test_data = self.get_data(self.test_start, self.test_end)

        for k,v in test_data.items():
            Xtest = v[0]
            ytest = v[1]
            try:
                model = [item[1] for item in self.models if item[0] == k][0]
            except:
                print('Something about ticker consistency not right!')
            self.predicts.append(k, model.predict(Xtest))

        return True

    def show_results(self):
        '''
        INPUT - self

        OUPUT - Outputs the train and test results
        '''

        self.train()

        for tm in self.models:
            test_data = self.get_data(self.test_start, self.test_end, ticker = tm[0])
            X = test_data[0]
            y = test_data[1]
            print("R-squared on test data for {} between {} and {} is {}".format(
                tm[0], self.test_start, self.test_end,
                tm[1].score(X,y)))

