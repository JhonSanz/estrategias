import pandas as pd
from solver import StrategyTester

meta_trader_data = pd.read_csv(
    'syp_1m2 copy.csv',
    names=['date', 'open', 'high', 'low', 'close', 'volume', 'unknown']
)
meta_trader_data = meta_trader_data[['date', 'open', 'high', 'low', 'close']]
meta_trader_data.reset_index(drop=True, inplace=True)
meta_trader_data.reset_index(inplace=True)
meta_trader_data['date'] = pd.to_datetime(meta_trader_data['date'], format='%Y.%m.%d')

PARAMETERS = [
    {
        "function": "stdev",
        "params": {
            "length": 20
        }
    },
    {
        "function": "psar",
        "params": {}
    },
]

STRATEGY_PARAMS = {
    "file": "parabolic_sar_standard_deviation",
    "test_mode": True
}

tester = StrategyTester(
    data=meta_trader_data,
    strategy_params=STRATEGY_PARAMS,
    parameters=PARAMETERS,
    months=12
)
tester.test()
