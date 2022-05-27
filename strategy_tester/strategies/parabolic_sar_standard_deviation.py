import numpy as np
import pandas as pd

class Strategy:
    def __init__(self):
        self.result = []

    def positions_table(self, data):
        data = data[[
            "index", "date", "close", "STDEV_25", "PSARl_0.02_0.2",
            "PSARs_0.02_0.2", "PSARr_0.02_0.2"
        ]].copy()
        data["chance"] = False
        data.loc[:, "chance"] = data["STDEV_25"]
        data.loc[data["chance"] < 2, "chance"] = 0
        data["chance"] = data["chance"].diff()
        data["chance"] = np.where(
            data["chance"] == data["STDEV_25"],
            True, False
        )
        data = data[200:]
        position = {}
        for date, close, long, short, drop, chance in zip(
            data["date"], data["close"], data["PSARl_0.02_0.2"],
            data["PSARs_0.02_0.2"], data["PSARr_0.02_0.2"],
            data["chance"]
        ):
            if (chance and not position):
                position["date_open"] = date
                position["price_open"] = close
                if (pd.isna(long)):
                    position["type"] = "sell"
                elif (pd.isna(short)):
                    position["type"] = "buy"
            elif position:
                if (int(drop) == 1):
                    position["date_close"] = date
                    position["price_close"] = close
                    self.result.append(position)
                    position = {}

        results = pd.DataFrame(data=self.result)
        results.to_excel("files/strategy.xlsx")
        results.to_csv("files/strategy.csv")
        return results
