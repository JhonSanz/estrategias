from plot_chart import plot_lines_chart
from algorithms import AlgorithmSelector
from strategy import StrategySelector
import pandas as pd


class StrategyTester:
    def __init__(self, data, strategy, parameters):
        self.data = data
        self.strategy = strategy
        self.parameters = parameters

    def _choose_algorithms(self):
        for parameter in self.parameters:
            self.data[parameter["field_alias"]] = (
                AlgorithmSelector(
                    self.data,
                    parameter["function"],
                    parameter["params"]
                ).select_algorithm()
            )

    def test(self):
        self._choose_algorithms()
        results = StrategySelector(self.data, self.strategy).run()
        
        plot_lines_chart()


df = pd.read_csv(
    'datos2.csv',
    names=['date', 'open', 'high', 'low', 'close', 'volume', 'unknown']
)
df = df[['date', 'open', 'high', 'low', 'close']]
df.reset_index(drop=True, inplace=True)
df.reset_index(inplace=True)
PARAMETERS = [
    {
        "field_alias": "MA_100",
        "function": "moving_average",
        "params": {
            "field": "close",
            "periods": 100
        }
    }
] 
tester = StrategyTester(df, "ma_100", PARAMETERS)
tester.test()
