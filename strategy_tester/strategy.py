import importlib

class StrategySelector:
    def __init__(self, data, strategy):
        self.data = data
        self.strategy = strategy
        self.module = None

    def validate_strategy_file(self):
        try:
            self.module = importlib.import_module(f"strategies.{self.strategy}")
        except ModuleNotFoundError:
            raise Exception(f"File {self.strategy} not found")

    def run(self):
        self.validate_strategy_file()
        new_dataframe = self.data.apply(
            lambda x: getattr(self.module, 'positions_table')(x), axis=1)
        print(new_dataframe)
