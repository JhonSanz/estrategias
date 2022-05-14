import importlib
import pandas as pd

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
        new_dataframe = getattr(self.module, 'positions_table')(self.data)
        results = pd.DataFrame(data=new_dataframe)
        print(results)
