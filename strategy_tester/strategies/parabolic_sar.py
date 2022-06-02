import numpy as np
import pandas as pd

class Strategy:
    def __init__(self, params = {}):
        self.params = params
        self.result = []

    def positions_table(self, data):
        data = data[[
            "index", "date", "close", "PSARl_0.02_0.2",
            "PSARs_0.02_0.2", "PSARr_0.02_0.2"
        ]].copy()
        data = data[200:]
        position = {}
        for date, close, long, short, drop in zip(
            data["date"], data["close"], data["PSARl_0.02_0.2"],
            data["PSARs_0.02_0.2"], data["PSARr_0.02_0.2"],
        ):
            if (not self.result or not position):
                position["date_open"] = date
                position["price_open"] = close
                if (pd.isna(long)):
                    position["type"] = "sell"
                elif (pd.isna(short)):
                    position["type"] = "buy"
            if (int(drop) == 1):
                position["date_close"] = date
                position["price_close"] = close
                self.result.append(position)
                position = {}

        results = pd.DataFrame(data=self.result)
        results.to_excel("files/strategy.xlsx")
        results.to_csv("files/strategy.csv")
        return results
