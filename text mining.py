import os
import re
from konlpy.tag import Okt
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# 리뷰 파일이 있는 디렉토리 경로
directory_path = 'review'

# 사용자 정의 단어 목록
custom_words = ['소금빵']

# 불용어 목록
stop_words = {'도', '이', '가', '에', '를', '은', '는', '께서', '와', '과', '의', '에', '에서', '부터', '까지', '하고', '하여', '이다', '하다',
              '되다'}

okt = Okt()


def preprocess_text(text):
    if not isinstance(text, str):
        text = ''
    text = re.sub(r'[^\w\s]', '', text)
    text = text.lower()

    # 사용자 정의 단어 결합 처리
    for word in custom_words:
        text = text.replace(word, word.replace(' ', ''))

    tokens = okt.morphs(text)

    # 불용어 제거
    tokens = [token for token in tokens if token not in stop_words]

    return ' '.join(tokens)


def analyze_keywords(file_path):
    df = pd.read_csv(file_path)
    review_column = '리뷰내용'

    reviews = df[review_column]
    processed_reviews = [preprocess_text(review) for review in reviews]

    # N-gram 벡터화
    vectorizer = CountVectorizer(ngram_range=(1, 3))
    X = vectorizer.fit_transform(processed_reviews)

    # 키워드 빈도 분석
    all_keywords = vectorizer.get_feature_names_out()
    keyword_counts = X.toarray().sum(axis=0)
    keyword_freq = dict(zip(all_keywords, keyword_counts))

    # 상위 10개 키워드 출력
    sorted_keywords = sorted(keyword_freq.items(), key=lambda item: item[1], reverse=True)
    print(f'Top keywords in {os.path.basename(file_path)}: {sorted_keywords[:10]}')

    # # 워드 클라우드 생성 및 시각화
    # wordcloud = WordCloud(font_path='malgun.ttf', width=800, height=400,
    #                       background_color='white').generate_from_frequencies(keyword_freq)
    # plt.figure(figsize=(10, 5))
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis('off')
    # plt.title(f'Word Cloud for {os.path.basename(file_path)}')
    # plt.show()


# 디렉토리 내의 모든 파일 처리
for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory_path, filename)
        analyze_keywords(file_path)
