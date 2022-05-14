class ResultsTable:
    def __init__(self, data):
        self.data = data
    
    def generate_totals(self):
        results = self.data
        results['total'] = results['price_open'] - results['price_close']
        results['type_2'] = results['type'].shift(1)
        results.loc[results['type_2'] == 'sell', 'total'] = (
            results[results['type_2'] == 'sell']['total'] * -1
        )
        results.loc[results['type_2'] == 'buy', 'total'] = (
            results[results['type_2'] == 'buy']['total']
        )
        results['total_sum'] = results.total.cumsum()
        results = results[[
            'date_open', 'price_open', 'date_close',
            'price_close', 'type', 'total', 'total_sum'
        ]]
        return results
