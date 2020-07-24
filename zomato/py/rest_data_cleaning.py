import pandas as pd
import numpy as np

df = pd.read_csv('csv/rest.csv')

df = df[['names', 'category', 'rating', 'reviews', 'cost', 'cuisine', 'featured', 'location','urls']]


# print(type(df['featured'][1])) # its a string, not a list. convert to list by split.

df['names'] = df['names'].apply(lambda x : x.strip())

df['rating'] = df['rating'].str.extract(r'(^\d.\d)')
df['rating'] = df['rating'].apply(lambda x : float(x))

df['reviews'] = df['reviews'].str.extract(r'(\d*,?\d+)')
df['reviews'] = df['reviews'].apply(lambda x : float(x.replace(',','') if isinstance(x, str) else np.nan))
# df['reviews'] = df['reviews'].astype('Int32')

df['cost'] = df['cost'].str.extract(r'(\d*,?\d+)')
df['cost'] = df['cost'].apply(lambda x : float(x.replace(',','') if isinstance(x, str) else np.nan))

print(df.info())
# print(df['location'].value_counts())


urls_re = df['urls'].to_frame()
urls_re.to_csv('csv/urls.csv', index=False, header=False)
df.to_csv('csv/rest_cleaned.csv',index=False)
