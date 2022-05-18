import pandas as pd
from solver import StrategyTester

meta_trader_data = pd.read_csv(
    'datos2.csv',
    names=['date', 'open', 'high', 'low', 'close', 'volume', 'unknown']
)
meta_trader_data = meta_trader_data[['date', 'open', 'high', 'low', 'close']]
meta_trader_data.reset_index(drop=True, inplace=True)
meta_trader_data.reset_index(inplace=True)
meta_trader_data['date'] = pd.to_datetime(meta_trader_data['date'], format='%Y.%m.%d')

PARAMETERS = [
    {
        "function": "sma",
        "params": {
            "length": 100
        }
    }
]
tester = StrategyTester(
    data=meta_trader_data,
    strategy="ma_100",
    parameters=PARAMETERS,
    months=12
)
tester.test()
