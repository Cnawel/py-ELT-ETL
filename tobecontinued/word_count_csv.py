import itertools
import collections
import pandas as pd

file_csv = 'multiplesclerosis_20220912.csv'

df = pd.read_csv(file_csv, skipinitialspace=True, encoding="utf-8")

all_words_no_urls = list(itertools.chain(df))

# Create counter
counts_no_urls = collections.Counter(all_words_no_urls)

print(counts_no_urls.most_common(15))