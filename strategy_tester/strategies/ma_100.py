import pandas as pd

class Strategy:
    def position_type(self, close, ma_100):
        return 'sell' if close < ma_100 else 'buy'

    def open_close_position(self, data, index, close, ma_100):
        if (str(index) == '0'):
            return False
        previous = data.loc[int(index) - 1]
        return (
            (close < ma_100 and self.position_type(
                previous.close, previous.SMA_100) == 'buy') 
            or
            (close > ma_100 and self.position_type(
                previous.close, previous.SMA_100) == 'sell')
        )

    def open_positions(self, data, index, close, ma_100):
        data = {
            "date_open": data.loc[int(index)].date,
            "price_open": close,
            "date_close": None,
            "price_close": None,
            "type": self.position_type(close, ma_100),
        }
        self.prev = index
        return data

    def positions_table(self, data):
        data = [
            self.open_positions(data, index, close, ma_100)
            for index, close, ma_100 in
            zip(data['index'], data['close'], data['SMA_100'])
            if self.open_close_position(data, index, close, ma_100)
        ]
        results = pd.DataFrame(data=data)
        results['price_close'] = results['price_open'].shift(-1)
        results['date_close'] = results['date_open'].shift(-1)
        return results
