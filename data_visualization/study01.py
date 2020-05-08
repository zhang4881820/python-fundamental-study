import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)


dates = pd.date_range('20200501', periods=8)
print(dates)
df = pd.DataFrame(np.random.randn(8, 4), index=dates, columns=list('ABCD'))
print(df)
