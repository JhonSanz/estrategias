import importlib

class StrategySelector:
    def __init__(self, data, strategy, strategy_params = {}):
        self.data = data
        self.strategy = strategy
        self.strategy_params = strategy_params
        self.module = None

    def validate_strategy_file(self):
        try:
            self.module = importlib.import_module(f"strategies.{self.strategy}")
        except ModuleNotFoundError:
            raise Exception(f"File {self.strategy} not found")

    def run(self):
        self.validate_strategy_file()
        new_dataframe = (
            getattr(self.module, 'Strategy')(self.strategy_params)
            .positions_table(self.data)
        )
        return new_dataframe
