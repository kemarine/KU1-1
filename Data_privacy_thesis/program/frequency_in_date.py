import pandas as pd

# csv 파일 불러오기
df = pd.read_csv('patrick_sentiment.csv')

# 'Datetime' 열을 날짜 형식으로 변환하기
df['Datetime'] = pd.to_datetime(df['Datetime'])

# 'Datetime' 열을 '연-월' 형식으로 변경하기
df['Year_Month'] = df['Datetime'].dt.to_period('M')

# 각 '연-월'에 대한 빈도수 계산하기
df_count = df['Year_Month'].value_counts().reset_index()
df_count.columns = ['Date(YYYY-MM)', 'Count(the number of data)']

# 결과를 csv 파일로 저장하기
df_count.to_csv('patrick_date_count.csv', index=False)
