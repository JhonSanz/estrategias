import pandas as pd

class Strategy:
    def __init__(self):
        self.result = []

    def position_type(self, close, ma_100):
        return 'sell' if close < ma_100 else 'buy'

    def open_positions(self, data, index, date, close, long, short, drop):
        if(drop == 1):
            close_data = data[data['date'] == date]
            row = next((item for item in self.result if item["date_open"] == date), None)
            if row:
                row["date_close"] = close_data.chance_date
                row["price_close"] = close_data.close
            return
        new_item = {
            "date_open": date,
            "price_open": close,
            "date_close": "",
            "price_close": "",
            "type": "",
        }
        if (pd.isna(long)):
            # compra
            new_item["type"] = "buy"
        elif (pd.isna(short)):
            # venta
            new_item["type"] = "sell"
        self.result.append(new_item)

    def define_chance(self, x, data):
        if (str(x.name) == '0'):
            return False
        if (not x.chance):
            return False
        previous = data.loc[int(x.name) - 1]
        return previous.STDEV_20 < 2

    def positions_table(self, data):
        data['chance'] = False
        data.loc[data['STDEV_20'] > 2, 'chance'] = True
        data['chance'] = data.apply(lambda x: self.define_chance(x, data), axis=1)
        changed_indicator = data.loc[data["PSARr_0.02_0.2"] == 1]
        changed_indicator = [
            (current, next) for current, next in zip(
                changed_indicator.index, changed_indicator.index[1:]
            )
        ]
        for item in changed_indicator:
            for i in range(item[0], item[1]):
                data.loc[i, ['chance_date']] = data.loc[item[0], ['date']].date

        for index, date, close, long, short, drop, chance in zip(
            data['index'], data['date'], data['close'], data['PSARl_0.02_0.2'],
            data['PSARs_0.02_0.2'], data['PSARr_0.02_0.2'],
            data['chance']
        ):
            if (chance):
                self.open_positions(data, index, date, close, long, short, drop)

        results = pd.DataFrame(data=self.result)
        print(results)
        return data
