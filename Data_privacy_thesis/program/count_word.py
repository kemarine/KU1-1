import pandas as pd
import re
from collections import Counter

# csv 파일 불러오기
df = pd.read_csv('jarpad_preprocess.csv')

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

# 모든 텍스트를 하나로 합치기
text = ' '.join(df['Text'].astype(str))

# 텍스트를 공백 기준으로 단어로 나누기
words = text.split()

# 단어의 빈도 계산하기
word_counts = Counter(words)

# 단어와 빈도를 DataFrame으로 만들기
df_word_counts = pd.DataFrame.from_dict(word_counts, orient='index').reset_index()
df_word_counts.columns = ['word', 'frequency']

# 결과를 csv 파일로 저장하기
df_word_counts.to_csv('jarpad_word_counts.csv', index=False)
