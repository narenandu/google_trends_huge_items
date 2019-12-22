import os
import time
import pandas as pd
from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=480, retries=3, backoff_factor=0.2)

here = os.path.dirname(__file__)

OUTPUT_FILE="ounces_to_pounds_vs_7000_google_trends.csv"
SEARCH_TERMS = "search_terms.csv"
NUM_TERMS_TO_READ = 7000
REF_TERM = "Ounces in Pound"


def get_terms(num_terms=NUM_TERMS_TO_READ):
    terms_file = os.path.join(here, SEARCH_TERMS)
    terms_df = pd.read_csv(terms_file)
    act = terms_df.head(num_terms).Act
    print(act.values)
    return act.values

terms = get_terms()

for i, term in enumerate(terms):
    if i % 25 == 0:
        print("processing ... i, term: {} -> {}...".format(i, term))
    time.sleep(0.25)
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