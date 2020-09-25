import all_imports as ai
import TechStrategies as TS

folder_name = 'Securities/'
stock = input('Enter name of stock: ').strip()
df = ai.pd.read_csv(r'%s' % (folder_name + stock + '.NS.csv'))

closing_prices = df.loc[:, 'Close']
count = 0

for i in closing_prices:
  if ai.math.isnan(i):
    df = df.drop(count, axis=0)
  count = count + 1
df = df.reset_index()

count = 0

dates = df.loc[:, 'Date']
opening_prices = df.loc[:, 'Open']
high_daily = df.loc[:, 'High']
low_daily = df.loc[:, 'Low']
closing_prices = df.loc[:, 'Close']
volume_daily = df.loc[:, 'Volume']

dates_array= ai.np.array([1])
dates_array = ai.np.append(dates_array, dates)
dates_array = ai.np.delete(dates_array, 0)

opening_prices_array = ai.np.array([1])
opening_prices_array = ai.np.append(opening_prices_array, opening_prices)
opening_prices_array = ai.np.delete(opening_prices_array, 0)

high_daily_array = ai.np.array([1])
high_daily_array = ai.np.append(high_daily_array, high_daily)
high_daily_array = ai.np.delete(high_daily_array, 0)

low_daily_array = ai.np.array([1])
low_daily_array = ai.np.append(low_daily_array, low_daily)
low_daily_array = ai.np.delete(low_daily_array, 0)

closing_prices_array= ai.np.array([1])
closing_prices_array = ai.np.append(closing_prices_array, closing_prices)
closing_prices_array = ai.np.delete(closing_prices_array, 0)

volume_daily_array = ai.np.array([1])
volume_daily_array = ai.np.append(volume_daily_array, volume_daily)
volume_daily_array = ai.np.delete(volume_daily_array, 0)

# CODE TO CALCULATE BEST EMA (BY CUMULATIVE PROFIT PERCENTAGE) OF ALL POSSIBLE EMAS BY BRUTE FORCE METHOD

'''print('Profit percentage earned if stayed invested from start date: ')
print(((closing_prices_array[-1]-closing_prices_array[0])/closing_prices_array[0])*100)
print('-------------------------------------------------')
cou = 0
grandpa_dict = {}
for abc in range(1,51):
  for xyz in range(abc+1, 201):


    m1 = TS.EMA(abc, closing_prices_array)
    m2 = TS.EMA(xyz, closing_prices_array)
    m1 = m1[len(m1)-len(m2):]
    closing_prices_array_new = closing_prices_array[len(closing_prices_array) - len(m2):]
    buy_flag = 0
    profit_array = ai.np.array([1])
    profit_percentage_array = ai.np.array([1])

    for i in range(3, len(m2)):
      if ((buy_flag == 0) and (m1[i] > m2[i]) and (m1[i-1] > m2[i-1]) and (m1[i-2] > m2[i-2]) and (m1[i-3] < m2[i-3])):
        buy_price = closing_prices_array_new[i]
        buy_flag = 1

      elif ((buy_flag == 1) and (m1[i] < m2[i])):
        sell_price = closing_prices_array_new[i]
        buy_flag = 0


        profit_array = ai.np.append(profit_array, sell_price-buy_price)
        profit_percentage_array = ai.np.append(profit_percentage_array, ((sell_price-buy_price)*100)/buy_price)

    profit_array = ai.np.delete(profit_array, 0)
    profit_percentage_array = ai.np.delete(profit_percentage_array, 0)

    print('Average per trade profit percentage and total trades: ')
    print(ai.np.average(profit_percentage_array), len(profit_percentage_array))
    cumulative_profit_multiplier = 1
    for i in profit_percentage_array:
      if (i>0):
        cumulative_profit_multiplier = cumulative_profit_multiplier*(1+(i/100))
      elif (i<0):
        cumulative_profit_multiplier = cumulative_profit_multiplier*(1-(i/100))
    print('Cumulative profit percentage of strategy: ')
    print((cumulative_profit_multiplier-1)*100)
    print(abc, 'cross', xyz)
    grandpa_dict[abc, 'cross', xyz] = ((cumulative_profit_multiplier-1)*100)
    cou=cou+1
    print('-------------------------------------------------------')
keymax = max(grandpa_dict, key=grandpa_dict.get)
print(keymax, grandpa_dict[keymax])'''


# CODE TO CALCULATE BEST EMA (BY NUMBER OF PROFITABLE TRADES) OF ALL POSSIBLE EMAS BY BRUTE FORCE METHOD


'''print('Profit percentage earned if stayed invested from start date: ')
print(((closing_prices_array[-1]-closing_prices_array[0])/closing_prices_array[0])*100)
print('-------------------------------------------------')
cou = 0
grandpa_dict = {}
for abc in range(1,11):
  for xyz in range(abc+1, 51):


    m1 = TS.EMA(abc, closing_prices_array)
    m2 = TS.EMA(xyz, closing_prices_array)
    m1 = m1[len(m1)-len(m2):]
    closing_prices_array_new = closing_prices_array[len(closing_prices_array) - len(m2):]
    buy_flag = 0
    profit_array = ai.np.array([1])
    profit_percentage_array = ai.np.array([1])

    for i in range(3, len(m2)):
      if ((buy_flag == 0) and (m1[i] > m2[i]) and (m1[i-1] > m2[i-1]) and (m1[i-2] > m2[i-2]) and (m1[i-3] < m2[i-3])):
        buy_price = closing_prices_array_new[i]
        buy_flag = 1

      elif ((buy_flag == 1) and (m1[i] < m2[i])):
        sell_price = closing_prices_array_new[i]
        buy_flag = 0


        profit_array = ai.np.append(profit_array, sell_price-buy_price)
        profit_percentage_array = ai.np.append(profit_percentage_array, ((sell_price-buy_price)*100)/buy_price)

    profit_array = ai.np.delete(profit_array, 0)
    profit_percentage_array = ai.np.delete(profit_percentage_array, 0)

    print('Total number of profitable trades: ')
    flagg = 0
    flagg_inverse = 0
    for i in range(len(profit_percentage_array)):
      if (profit_percentage_array[i] > -2):
        flagg = flagg + 1
      else:
        flagg_inverse = flagg_inverse +1
    print('Total number of profitable and unprofitable trades respectively are:  ')
    print(flagg,'and ', flagg_inverse)
    print(abc, 'cross', xyz)
    grandpa_dict[abc, 'cross', xyz] = ((flagg/(flagg+flagg_inverse))*100)
    cou=cou+1
    print('-------------------------------------------------------')
keymax = max(grandpa_dict, key=grandpa_dict.get)
print(keymax, grandpa_dict[keymax])

print('Dictionary of profitable trades in descending order is')
print(dict(sorted(grandpa_dict.items(), key=ai.o.itemgetter(1),reverse=True)))'''


# CODE TO FIND DETAILS OF A PARTICULAR DUAL EMA CROSSOVER STRATEGY

abc = int(input('Enter lower EMA: '))
xyz= int(input('Enter higher EMA: '))
m1 = TS.EMA(abc, closing_prices_array)
m2 = TS.EMA(xyz, closing_prices_array)
m1 = m1[len(m1)-len(m2):]
closing_prices_array_new = closing_prices_array[len(closing_prices_array) - len(m2):]
buy_flag = 0
profit_array = ai.np.array([1])
profit_percentage_array = ai.np.array([1])

for i in range(3, len(m2)):
  if ((buy_flag == 0) and (m1[i] > m2[i]) and (m1[i-1] > m2[i-1]) and (m1[i-2] > m2[i-2]) and (m1[i-3] < m2[i-3])):
    buy_price = closing_prices_array_new[i]
    buy_flag = 1

  elif ((buy_flag == 1) and (m1[i] < m2[i])):
    sell_price = closing_prices_array_new[i]
    buy_flag = 0


    profit_array = ai.np.append(profit_array, sell_price-buy_price)
    profit_percentage_array = ai.np.append(profit_percentage_array, ((sell_price-buy_price)*100)/buy_price)

profit_array = ai.np.delete(profit_array, 0)
profit_percentage_array = ai.np.delete(profit_percentage_array, 0)

print('Average per trade profit percentage and total trades: ')
print(ai.np.average(profit_percentage_array), len(profit_percentage_array))
cumulative_profit_multiplier = 1
for i in profit_percentage_array:
  if (i>0):
    cumulative_profit_multiplier = cumulative_profit_multiplier*(1+(i/100))
  elif (i<0):
    cumulative_profit_multiplier = cumulative_profit_multiplier*(1-(i/100))
print('Cumulative profit percentage of strategy: ')
print((cumulative_profit_multiplier-1)*100)
print(abc, 'cross', xyz)
print('Sorted array is: ')
print(ai.np.sort(profit_percentage_array))