import pandas as pd
import re
from collections import Counter
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')

# csv 파일 불러오기
df = pd.read_csv('new_file.csv')

# 어퍼스트로피를 제외한 모든 특수문자와 한글을 제거하는 함수
def remove_punctuation_and_korean(text):
    if isinstance(text, str):
        text = re.sub(r"[^a-zA-Z0-9' ]+", ' ', text)  # 어퍼스트로피를 제외한 모든 특수문자 제거
        text = re.sub(r'[ㄱ-ㅎㅏ-ㅣ가-힣]', '', text)  # 한글 제거
        return text
    else:
        return text

# 'Text' 열에 대해 함수 적용하기
df['Text'] = df['Text'].apply(remove_punctuation_and_korean)

# 감정 분석기 초기화하기
sid = SentimentIntensityAnalyzer()

# 감정 분석을 수행하는 함수
def get_sentiment(text):
    if isinstance(text, str):
        sentiment = sid.polarity_scores(text)
        return sentiment['compound']
    else:
        return None

# 'Text' 열에 대해 함수 적용하기
df['sentiment'] = df['Text'].apply(get_sentiment)

# 결과를 csv 파일로 저장하기
df.to_csv('sentiment.csv', index=False)
