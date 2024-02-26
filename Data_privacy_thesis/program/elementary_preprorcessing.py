import pandas as pd
import re

# csv 파일 불러오기
df = pd.read_csv('test1.csv')

# '@'로 시작하는 문자열을 찾아서 제거하고, 한글을 제거하는 함수
def remove_at_words_and_korean(text):
    text = re.sub(r'@\S+', '', text)  # '@'로 시작하는 문자열 제거
    text = re.sub(r'[ㄱ-ㅎㅏ-ㅣ가-힣]', '', text)  # 한글 제거
    text = re.sub(r'\s+', ' ', text)  # 공백 여러 개를 하나로 바꾸는 부분
    return text.strip()  # 앞뒤 공백 제거

# 'text' 열에 대해 함수 적용하기
df['Text'] = df['Text'].apply(remove_at_words_and_korean)

# 결과를 새로운 csv 파일로 저장
df.to_csv('new_file.csv', index=False)
