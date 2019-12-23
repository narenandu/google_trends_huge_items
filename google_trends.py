import os
import sys
import time
import pandas as pd
from pytrends.request import TrendReq

# pytrends = TrendReq(hl='en-US', tz=360, retries=10, backoff_factor=0.5)
pytrends = TrendReq(hl='en-US',
                tz=360,
                timeout=(10,25),
                proxies=['https://34.203.233.13:80','https://35.201.123.31:880'],
                retries=2,
                backoff_factor=0.1)

here = os.path.dirname(__file__)

SEARCH_TERMS = "search_terms.csv"
start_term_idx = 700
end_term_idx = 1050
REF_TERM = "Ounces in Pound"


def get_terms(start_idx=start_term_idx, end_idx=end_term_idx):
    terms_file = os.path.join(here, SEARCH_TERMS)
    terms_df = pd.read_csv(terms_file)
    act = terms_df[int(start_idx):int(end_idx)].Act
    print(act.values)
    return act.values

def main(start, end):

    terms = get_terms(start, end)
    for i, term in enumerate(terms):
        print("term: {}".format(term))
        if i % 25 == 0:
            print("processing ... i, term: {} -> {}...".format(i, term))
        time.sleep(0.5)
        pytrends.build_payload([REF_TERM, term], timeframe="2015-11-01 2019-12-20", geo='US')
        df = pytrends.interest_over_time()
        df_ = df.drop("isPartial", axis=1)
        if i == 0:
            df_temp = df_.copy()
        else:
            result = pd.concat([df_temp, df_], axis=1)
            df_temp = result

    OUTPUT_FILE="ounces_to_pounds_vs_7000_google_trends_{}.csv".format(end)
    output_file = os.path.join(here, OUTPUT_FILE)
    print("writing to csv file")
    df_temp.to_csv(output_file)

if __name__ == "__main__":
    start = sys.argv[1]
    end = sys.argv[2]
    print(start, end)
    main(start, end)