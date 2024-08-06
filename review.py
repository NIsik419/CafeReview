import pandas as pd

# CSV 파일 읽기
file_path = '온아워오프 리뷰.csv'
df = pd.read_csv(file_path)

# 리뷰 내용이 있는 열의 이름을 설정 (예: 'Review')
# 열 이름을 'reviews'로 가정합니다. 실제 파일의 열 이름에 따라 수정하십시오.
review_column = '리뷰내용'

# 리뷰 내용만 추출
reviews = df[review_column]

# 추출된 리뷰 내용 출력
print(reviews)