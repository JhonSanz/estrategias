class ResultsTable:
    def __init__(self, data):
        self.data = data
    
    def generate_totals(self):
        results = self.data
        results['total'] = results['price_close'] - results['price_open']
        results.loc[results['type'] == 'sell', 'total'] = results['total'] * (-1)
        results['total_sum'] = results.total.cumsum()
        results = results[[
            'date_open', 'price_open', 'date_close',
            'price_close', 'type', 'total', 'total_sum'
        ]]
        results.to_excel("files/totals.xlsx")
        results.to_csv("files/totals.csv")
        return results
