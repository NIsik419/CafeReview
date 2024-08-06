import time

import warnings
warnings.filterwarnings('ignore')
from selenium import webdriver  # 동적크롤링
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import pandas as pd

data = {
    '업소명': [
        '스타벅스 강남역점',
        '투썸플레이스 신촌점',
        '이디야커피 합정점',
        # 여기에 더 많은 카페 이름 추가
    ]
}
df = pd.DataFrame(data)
def extract_review():
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    # 리뷰 추출
    rev = []  # 추출한 리뷰 저장
    for i in range(1, 11):  # 더보기 누르지 않은 상태로 최대 10개
        try:  # 사진 없는 후기는 div 3번째에 텍스트 위치
            driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[4]/div[1]/ul/li[' + str(
                i) + ']/div[3]/a').send_keys(Keys.ENTER)  # 텍스트 전체 볼 수 있게 클릭
            time.sleep(2)
            comment = driver.find_element(By.XPATH,
                                          '//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[4]/div[1]/ul/li[' + str(
                                              i) + ']/div[3]/a/span').text  # 리뷰
            rev.append(comment)
        except:  # 사진 있는 후기는 div 4번째에 텍스트가 위치
            driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[4]/div[1]/ul/li[' + str(
                i) + ']/div[4]/a').send_keys(Keys.ENTER)
            time.sleep(2)
            comment = driver.find_element(By.XPATH,
                                          '//*[@id="app-root"]/div/div/div/div[7]/div[3]/div[4]/div[1]/ul/li[' + str(
                                              i) + ']/div[4]/a/span').text  # 리뷰
            rev.append(comment)
    return rev

data = []
# 크롬 드라이버 실행
driver = webdriver.Chrome(ChromeDriverManager().install())

for i in df['업소명']:
    #     # 검색창에 입력하지 않고 직접 해당 숙소의 주소로 이동
    url = "https://map.naver.com/v5/search/서울 " + str(i) + '/place'
    driver.get(url)
    time.sleep(8)

    try:
        driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="entryIframe"]'))  # iframe 이동
        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # 리뷰 탭으로 이동
        lists = soup.select(
            '#app-root > div > div > div > div.place_section.OP4V8 > div.zD5Nm.f7aZ0 > div.dAsGb > span')

        # 별점/방문자리뷰/블로그리뷰 순일때 방문자리뷰는 두번째에 위치=span[2]
        if len(lists) > 2:
            driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[2]/a').send_keys(
                Keys.ENTER)  # 방문자 리뷰
            time.sleep(3)

        # 방문자리뷰/블로그리뷰 순일때 방문자리뷰는 첫번째에 위치=span[1]
        else:
            driver.find_element(By.XPATH, '//*[@id="app-root"]/div/div/div/div[2]/div[1]/div[2]/span[1]/a').send_keys(
                Keys.ENTER)  # 방문자 리뷰
            time.sleep(3)

        review = extract_review()  # 리뷰 추출 함수 호출
        data.append(review)
        # print(Review)

    except:
        data.append(' ')
        # print(' ')