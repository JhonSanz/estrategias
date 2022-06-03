from plot_chart import plot_lines_chart
from algorithms import AlgorithmSelector
from strategy import StrategySelector
from results_table import ResultsTable
from constant import *

class StrategyTester:
    def __init__(self, data, strategy_params, parameters, months, title):
        self.data = data
        self.strategy_params = strategy_params
        self.parameters = parameters
        self.months = months
        self.title = title

    def _choose_algorithms(self):
        for parameter in self.parameters:
            self.data = (
                AlgorithmSelector(
                    self.data,
                    parameter["function"],
                    parameter["params"]
                ).select_algorithm()
            )

    def test(self):
        if (self.strategy_params.get("test_mode") == INITAL_DATA):
            print(self.data)
            return
        self._choose_algorithms()
        if (self.strategy_params.get("test_mode") == AFTER_ALGORITHM):
            print(self.data)
            return
        results = StrategySelector(
            self.data, self.strategy_params.get('file'),
            self.strategy_params.get("params")
        ).run()
        if (self.strategy_params.get("test_mode") == AFTER_STRATEGY):
            print(results)
            return
        results = ResultsTable(results).generate_totals()
        if (self.strategy_params.get("test_mode") == RESULTS_TABLE):
            print(results)
            return
        plot_lines_chart(
            results, 'date_close', 'total_sum',
            self.months, self.title.split('/')[-1]
        )
