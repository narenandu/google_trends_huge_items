import pandas as pd
from pytrends.request import TrendReq
pytrends = TrendReq(hl='en-US', tz=480)



pytrends.build_payload(["bagel", "pizza", "chocolate", "test", "hello"], timeframe="now 1-H", geo='US')
df = pytrends.interest_over_time()
print("------------df------------")
print(df)
print(".......................................................")

pytrends.build_payload(["bagel", "pizza"], timeframe="now 1-H", geo='US')
dfp = pytrends.interest_over_time()
print("------------dfp------------")
print(dfp)
print(".......................................................")


pytrends.build_payload(["bagel", "chocolate"], timeframe="now 1-H", geo='US')
dfc = pytrends.interest_over_time()
print("------------dfc------------")
print(dfc)
print(".......................................................")


pytrends.build_payload(["bagel", "test"], timeframe="now 1-H", geo='US')
dft = pytrends.interest_over_time()
print("------------dft------------")
print(dft)
print(".......................................................")


pytrends.build_payload(["bagel", "hello"], timeframe="now 1-H", geo='US')
dfh = pytrends.interest_over_time()
print("------------dfh------------")
print(dfh)
print(".......................................................")