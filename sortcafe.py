import pandas as pd

# 데이터 로드
file_path = '네이버 지도 방문자 리뷰 크롤러 25부터 끝까지.csv'
df = pd.read_csv(file_path)

# 가게명 기준으로 데이터프레임을 그룹화
grouped_df = df.groupby('가게이름')

# 그룹화된 데이터를 가게별로 리스트로 저장
grouped_reviews = {name: group for name, group in grouped_df}

# 그룹화된 데이터를 가게명으로 정렬하여 CSV 파일로 저장
for store_name, reviews in grouped_reviews.items():
    reviews.to_csv(f'{store_name}_reviews.csv', index=False, encoding='utf-8-sig')
