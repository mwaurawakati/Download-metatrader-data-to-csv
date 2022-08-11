from datetime import datetime
import MetaTrader5 as mt5
# display data on the MetaTrader 5 package
print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)
broker="Scope_Markets"
instrument="XAUUSD.r"
timeframe= 'TIMEFRAME_H1'
tmf=getattr(mt5,timeframe)
utc_from = datetime(2015, 1, 1)
utc_to = datetime(2022, 8, 11)
# import the 'pandas' module for displaying data obtained in the tabular form
import pandas as pd
pd.set_option('display.max_columns', 500) # number of columns to be displayed
pd.set_option('display.width', 1500)      # max table width to display
# import pytz module for working with time zone
import pytz
 
# establish connection to MetaTrader 5 terminal
if not mt5.initialize():
    print("initialize() failed, error code =",mt5.last_error())
    quit()
import MetaTrader5 as mt5
from datetime import datetime

account = int(4412337)

mt5.initialize()
authorized=mt5.login(account)

if authorized:
    print("Connected: Connecting to MT5 Client")
else:
    print("Failed to connect at account #{}, error code: {}"
          .format(account, mt5.last_error()))


rates = mt5.copy_rates_range(instrument, tmf, utc_from, utc_to)
for rate in rates:
	print(rates)
# create DataFrame out of the obtained data
rates_frame = pd.DataFrame(rates)
# convert time in seconds into the 'datetime' format
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')
 
# display data
print("\nDisplay dataframe with data")
print(rates_frame.head(10))

timeframe=timeframe[-(len(timeframe)-10):]

utc_from = utc_from.strftime('%Y-%m-%d' )
utc_to = utc_to.strftime('%Y-%m-%d' )
filename=broker+"_"+instrument+"_"+timeframe+"_from_"+utc_from+"_to_"+utc_to+".csv"
rates_frame.to_csv(filename)
