import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('patrick_sentiment.csv')

sns.stripplot(data=df, x="user", y="sentiment", s=2)

plt.show()
