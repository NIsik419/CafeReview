import os
import pandas as pd
from transformers import pipeline

# 심볼릭 링크 경고 비활성화
os.environ['HF_HUB_DISABLE_SYMLINKS_WARNING'] = '1'

# CSV 파일 읽기
file_path = '온아워오프 리뷰.csv'
df = pd.read_csv(file_path)

# 리뷰 내용이 있는 열의 이름을 설정 (예: 'Review')
review_column = '리뷰내용'

# 리뷰 내용만 추출
reviews = df[review_column].tolist()

# 요약 파이프라인 설정 (사전 학습된 모델 사용)
model_name = 'sshleifer/distilbart-cnn-12-6'
summarizer = pipeline('summarization', model=model_name)

# 각 리뷰 요약
summary_list = []
for review in reviews:
    if len(review) > 0:  # 빈 리뷰는 무시
        summary = summarizer(review, max_length=50, min_length=25, do_sample=False)
        summary_list.append(summary[0]['summary_text'])
    else:
        summary_list.append('')  # 빈 리뷰는 빈 요약 추가

# 요약된 리뷰 출력
for i, summary in enumerate(summary_list):
    print(f"Original Review {i+1}: {reviews[i]}")
    print(f"Summary {i+1}: {summary}")
    print("-" * 80)
