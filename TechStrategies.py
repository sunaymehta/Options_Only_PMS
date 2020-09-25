import all_imports as ai

# Strategy 1: Simple Moving Averages
def SMA(sma, closing_prices_array):
    sma_array = ai.np.array([1])
    for i in range(len(closing_prices_array)-sma+1):
        sma_array = ai.np.append(sma_array, ai.np.average(closing_prices_array[i:i+sma]))
    sma_array = ai.np.delete(sma_array, 0)
    return sma_array

# Strategy 2: Exponential Moving Averages
def EMA(ema, closing_prices_array):
    ema_array = ai.np.array([ai.np.average(closing_prices_array[0:ema])])
    for i in range(1, len(closing_prices_array) - ema + 1):
        ema_array = ai.np.append(ema_array, (2/(ema+1))*(closing_prices_array[ema+i-1]-ema_array[i-1]) + ema_array[i-1])
    return ema_array