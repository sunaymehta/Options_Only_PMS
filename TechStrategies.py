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

# Strategy 3: Average movement every x days
def movement(trade_days, closing_prices_array, ):
    move_array = ai.np.array([1])
    for i in range(len(closing_prices_array)-trade_days):
        move_array = ai.np.append(move_array, closing_prices_array[i+trade_days] - closing_prices_array[i])
    move_array = ai.np.delete(move_array, 0)
    return move_array

#Strategy 4: Bollinger Bands

def Bollinger_Bands(middle_sma, standard_deviation_coefficient, closing_prices_array):
    middle_band_array = SMA(middle_sma, closing_prices_array)
    variance_array = ai.np.array([1])
    for i in range(len(middle_band_array)):
        xxx_array = closing_prices_array[i:i+middle_sma]
        summ = 0
        for j in range(len(xxx_array)):
            summ = summ + (xxx_array[j]-middle_band_array[i])**2
        variance_array = ai.np.append(variance_array, summ/middle_sma)
    variance_array = ai.np.delete(variance_array, 0)
    standard_deviation_array = ai.np.sqrt(variance_array)
    upper_band_array = middle_band_array + (standard_deviation_coefficient*standard_deviation_array)
    lower_band_array = middle_band_array - (standard_deviation_coefficient*standard_deviation_array)
    return [middle_band_array, upper_band_array, lower_band_array]