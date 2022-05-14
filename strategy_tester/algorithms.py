
class AlgorithmSelector:
    def __init__(self, data, algorithm, params):
        self.data = data
        self.algorithm = algorithm
        self.params = params
        self.function = None

    def validate_algorithm_params(self):
        if (
            set(self.params.keys()) !=
            set(self.function.__code__.co_varnames[1:])
        ):
            raise Exception(f"Invalid params {self.params} for {self.algorithm} function")

    def validate_algorithm_name(self):
        try:
            self.function = getattr(AlgorithmSelector, self.algorithm)
        except AttributeError:
            raise Exception(f"Function {self.algorithm} not found")

    def select_algorithm(self):
        self.validate_algorithm_name()
        self.validate_algorithm_params()
        return self.function(self, **self.params)

    def moving_average(self, field, periods):
        '''
            Returns a Series object with moving average
        '''
        return self.data[f'{field}'].rolling(periods).mean()

