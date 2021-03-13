# https://www.youtube.com/watch?v=0XQjgmChtE4
import talib
import numpy
from numpy import genfromtxt
# sys.path.append('ta-lib')
# import talib

# get random data in numpy  array
# close = numpy.random.random(100)
# print(close)

# get RSI indicator from random ids
# moving_average  = talib.RSI(close)
# print (moving_average)

# convert csv to numpy array
my_data = genfromtxt('15minutes.csv', delimiter=',')
print(my_data)

# select 4th column from CSV
close_price = my_data[:,4]
print (close_price)

# shows RSI basing on numpy array taken from 15minutes.csv -> column (4)
moving_rsi = talib.RSI(close_price)
print(moving_rsi)


