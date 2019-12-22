import os
import time
import pandas as pd
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=480, retries=3, backoff_factor=0.2)

here = os.path.dirname(__file__)

SEARCH_TERMS = "search_terms.csv"
start_term_idx = 700
end_term_idx = 1050
REF_TERM = "Ounces in Pound"
OUTPUT_FILE="ounces_to_pounds_vs_7000_google_trends_1050.csv"

def get_terms(start_idx=start_term_idx, end_idx=end_term_idx):
    terms_file = os.path.join(here, SEARCH_TERMS)
    terms_df = pd.read_csv(terms_file)
    act = terms_df[start_idx:end_idx].Act
    print(act.values)
    return act.values

terms = get_terms()

for i, term in enumerate(terms):
    if i % 25 == 0:
        print("processing ... i, term: {} -> {}...".format(i, term))
    time.sleep(1)
    pytrends.build_payload([REF_TERM, term], timeframe="2015-11-01 2019-12-20", geo='US')
    df = pytrends.interest_over_time()
    df_ = df.drop("isPartial", axis=1)
    if i == 0:
        df_temp = df_.copy()
    else:
        result = pd.concat([df_temp, df_], axis=1)
        df_temp = result

output_file = os.path.join(here, OUTPUT_FILE)
print("writing to csv file")
df_temp.to_csv(output_file)