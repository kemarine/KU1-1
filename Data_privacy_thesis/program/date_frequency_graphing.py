import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv('patrick_date_count.csv')

sns.lineplot(data=df, x="Date", y="Count")

# X축 레이블 제어하기
locs, labels = plt.xticks()  # 현재의 X축 레이블 위치와 레이블 가져오기
N = 10  # 표시할 레이블 수
plt.xticks(locs[::len(locs)//N], labels[::len(labels)//N], rotation=45)  # N개의 레이블만 표시

plt.show()
