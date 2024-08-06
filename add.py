import os
import pandas as pd

# 리뷰 파일이 있는 디렉토리 경로
directory_path = 'review'

# 모든 리뷰를 하나의 데이터프레임으로 통합
all_reviews = []

for filename in os.listdir(directory_path):
    if filename.endswith('.csv'):
        file_path = os.path.join(directory_path, filename)
        df = pd.read_csv(file_path)
        all_reviews.append(df)

# 모든 리뷰 데이터프레임을 하나로 통합
combined_df = pd.concat(all_reviews, ignore_index=True)

# 통합된 리뷰 데이터프레임을 CSV 파일로 저장
combined_df.to_csv('combined_reviews.csv', index=False, encoding='utf-8-sig')
