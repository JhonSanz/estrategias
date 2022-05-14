def position_type(close, ma_100):
    return 'sell' if close < ma_100 else 'buy'

def open_close_position(data, index, close, ma_100):
    if (str(index) == '0'):
        return False
    previous = data.loc[int(index) - 1]
    return (
        (close < ma_100 and position_type(
            previous.close, previous.MA_100) == 'buy') 
        or
        (close > ma_100 and position_type(
            previous.close, previous.MA_100) == 'sell')
    )

def generate_positions_table(data, index, close, ma_100):
    return {
        "date_open": data.loc[int(index)].date,
        "price_open": close,
        "date_close": None,
        "price_close": None,
        "type": position_type(close, ma_100),
    }

def positions_table(data):
    return [
        generate_positions_table(data, index, close, ma_100)
        for index, close, ma_100 in
        zip(data['index'], data['close'], data['MA_100'])
        if open_close_position(data, index, close, ma_100)
    ]
