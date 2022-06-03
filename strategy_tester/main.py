import pandas as pd
from solver import StrategyTester


DIR_URL = 'datos/'
SUBDIR_URL = '2022_06_03/'
APPLE = 'Apple_M1_201201031640_202206021657.csv'
BTC = 'BTCUSD_M1_201301020000_202206021657.csv'
EURUSD = 'EURUSD_M1_200001030001_202206021657.csv'
GOLD = 'GOLDmicro_M1_200106040100_202111292255.csv'
MICROSOFT = 'Microsoft_M1_201201031640_202206021657.csv'
US100 = 'US100Cash_M1_201109190000_202206021657.csv'
US500 = 'US500Cash_M1_201108080000_202206021657.csv'

# DIR_URL = 'datos/'
# SUBDIR_URL = ''
# FILE_URL = 'syp_1m_.csv'

DATA_URL = f'{DIR_URL}{SUBDIR_URL}{US500}'

meta_trader_data = pd.read_csv(
    DATA_URL,
    # names=['date', 'open', 'high', 'low', 'close', 'volume', 'unknown'],
    sep='\t' if SUBDIR_URL != '' else ',',
)

if SUBDIR_URL != '':
    meta_trader_data['<DATE>'] = meta_trader_data['<DATE>'] + ' ' + meta_trader_data['<TIME>']
    meta_trader_data.rename(columns={
        "<DATE>": "date",
        "<OPEN>": "open",
        "<HIGH>": "high",
        "<LOW>": "low",
        "<CLOSE>": "close",
    }, inplace=True)

meta_trader_data = meta_trader_data[['date', 'open', 'high', 'low', 'close']]
meta_trader_data.reset_index(drop=True, inplace=True)
meta_trader_data.reset_index(inplace=True)
meta_trader_data['date'] = pd.to_datetime(meta_trader_data['date'], format='%Y.%m.%d')

# meta_trader_data = meta_trader_data[1635618:] # bitcoin
# meta_trader_data = meta_trader_data[6000000:] # eurusd


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
    months=12,
    title=DATA_URL
)
tester.test()
