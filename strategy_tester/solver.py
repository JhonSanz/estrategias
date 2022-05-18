from plot_chart import plot_lines_chart
from algorithms import AlgorithmSelector
from strategy import StrategySelector
from results_table import ResultsTable


class StrategyTester:
    def __init__(self, data, strategy, parameters, months):
        self.data = data
        self.strategy = strategy
        self.parameters = parameters
        self.months = months

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
        self._choose_algorithms()
        results = StrategySelector(self.data, self.strategy).run()
        results = ResultsTable(results).generate_totals()
        plot_lines_chart(results, 'date_close', 'total_sum', self.months)
