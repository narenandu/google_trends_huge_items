import os
import pandas as pd

NUM_TERMS_TO_READ = 7
here = os.path.dirname(__file__)
terms_file = os.path.join(here, "search_terms.csv")

terms_df = pd.read_csv(terms_file)
act = terms_df.head(NUM_TERMS_TO_READ).Act
print(act.values)
