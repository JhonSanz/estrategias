import pandas as pd
from solver import StrategyTester

meta_trader_data = pd.read_csv(
    'datos/syp_1m_.csv',
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
            "length": 11
        }
    },
    {
        "function": "sma",
        "params": {
            "length": 265
        }
    },
    {
        "function": "rsi",
        "params": {
            "length": 2
        }
    },
]

STRATEGY_PARAMS = {
    "file": "ma11_265_rsi",
    "params": {}
}

tester = StrategyTester(
    data=meta_trader_data,
    strategy_params=STRATEGY_PARAMS,
    parameters=PARAMETERS,
    months=12
)
tester.test()
