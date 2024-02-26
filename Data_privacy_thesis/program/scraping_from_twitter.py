import snscrape.modules.twitter as sntwitter
import pandas as pd
import warnings

warnings.filterwarnings(action='ignore')


# 트윗 데이터를 추가할 리스트
tweets_list = []

# TwitterSearchScraper를 사용하여 조건에 맞는 데이터를 스크래핑하고 리스트에 추가
for i, tweet in enumerate(sntwitter.TwitterSearchScraper('from:jarpad').get_items()):
    if i > 10000:
        break
    tweets_list.append([tweet.date, tweet.content, tweet.user.username])

# 리스트를 바탕으로 데이터프레임 형성
tweets_df1 = pd.DataFrame(tweets_list, columns=['Datetime', 'Text', 'Username'])

# 결과를 csv파일로 저장하기
tweets_df1.to_csv('test1.csv', index=False)
