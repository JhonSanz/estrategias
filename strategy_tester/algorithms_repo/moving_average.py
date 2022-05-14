def moving_average(data, field, periods):
    '''
        Returns a Series object with moving average
    '''
    return data[f'{field}'].rolling(periods).mean()
