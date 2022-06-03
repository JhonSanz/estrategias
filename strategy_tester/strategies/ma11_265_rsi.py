from turtle import pos
import pandas as pd
import numpy as np

class Strategy:
    def __init__(self, params = {}):
        self.params = params
        self.result = []
        self.rsi_high = 75
        self.rsi_low = 25
        self.presition = 2

    def positions_table(self, data):
        data = data[[
            "index", "date", "close", "RSI_2", "SMA_11", "SMA_265"
        ]].copy()

        data.loc[:, "chance_low"] = data["RSI_2"]
        data.loc[:, "chance_high"] = data["RSI_2"]
        data.loc[data["chance_low"] < self.rsi_low, "chance_low"] = 0
        data.loc[data["chance_high"] > self.rsi_high, "chance_high"] = 0
        data["chance_low"] = data["chance_low"].diff()
        data["chance_high"] = data["chance_high"].diff()
        data["chance_low"] = np.where(
            data["chance_low"] == data["RSI_2"],
            True, False
        )
        data["chance_high"] = np.where(
            data["chance_high"] == data["RSI_2"],
            True, False
        )

        data.loc[:, "cross_sma_low"] = data["SMA_11"]
        data.loc[:, "cross_sma_high"] = data["SMA_11"]
        data.loc[data["cross_sma_low"] > data["close"], "cross_sma_low"] = 0
        data.loc[data["cross_sma_high"] < data["close"], "cross_sma_high"] = 0
        data["cross_sma_low"] = data["cross_sma_low"].diff()
        data["cross_sma_high"] = data["cross_sma_high"].diff()
        data["cross_sma_low"] = np.where(
            data["cross_sma_low"] == data["SMA_11"],
            True, False
        )
        data["cross_sma_high"] = np.where(
            data["cross_sma_high"] == data["SMA_11"],
            True, False
        )

        position = {}
        stop = 0
        for (
            date, close, sma11, sma265,
            chance_low, chance_high,
            cross_sma_low, cross_sma_high
        ) in zip(
            data["date"], data["close"], data["SMA_11"],
            data["SMA_265"], data["chance_low"],
            data["chance_high"], data["cross_sma_low"],
            data["cross_sma_high"]
        ):
            if not position:
                if (
                    (
                        # compra
                        close > sma265
                        and close < sma11
                        and chance_low
                    ) or
                    (
                        # venta
                        close < sma265
                        and close > sma11
                        and chance_high
                    )
                ):
                    position["date_open"] = date
                    position["price_open"] = close
                    if chance_high:
                        # venta
                        position["type"] = "sell"
                        stop = close + close * (0.1 * 10**(self.presition * -1))
                    elif chance_low:
                        # compra
                        position["type"] = "buy"
                        stop = close - close * (0.1 * 10**(self.presition * -1))
            elif position:
                if (
                    (
                        position["type"] == "sell"
                        and close > stop 
                    ) or (
                        position["type"] == "buy"
                        and close < stop 
                    )
                ):
                    position["date_close"] = date
                    position["price_close"] = stop
                    position["stop"] = stop
                    self.result.append(position)
                    position = {}
                    stop = 0
                elif (
                    (
                        position["type"] == "sell"
                        and cross_sma_high
                    ) or 
                    (
                        position["type"] == "buy"
                        and cross_sma_low
                    )
                ):
                    position["date_close"] = date
                    position["price_close"] = close
                    position["stop"] = stop
                    self.result.append(position)
                    position = {}
                    stop = 0

        results = pd.DataFrame(data=self.result)
        results.to_excel("files/strategy.xlsx")
        results.to_csv("files/strategy.csv")
        return results
