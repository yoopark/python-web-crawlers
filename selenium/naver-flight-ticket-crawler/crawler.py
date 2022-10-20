from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import mail


driver = webdriver.Chrome()
url = 'https://flight.naver.com/flights/domestic/CJU-GMP-20221023?adult=1&child=0&infant=0&fareType=YC&selectedFlight='

found = False
cnt = 1
while True:
    driver.get(url)
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.result')))
    for _ in range(5):
        driver.execute_script('window.scrollTo(0, 10000)')
    time.sleep(3)

    elements = driver.find_elements(By.CSS_SELECTOR, '.result')
    for idx, element in enumerate(elements):
        l = element.text.split('\n')
        if l[1].find('이벤트') != -1:
            del l[1]
        flight, departure_raw_str, price_str = \
            l[0], l[1][:-3], l[4].split()[1][:-2]
        h, m = map(int, departure_raw_str.split(':'))
        price = int(price_str.replace(',', ''))

        if (14, 30) <= (h, m) < (16, 0) and price < 150000:
            driver.find_element(
                By.XPATH, f"//*[@id=\"__next\"]/div/div[1]/div[6]/div/div[2]/div[{idx+2}]").click()  # 해당 항공편 선택
            time.sleep(2)
            driver.find_element(
                By.XPATH, "//*[@id=\"__next\"]/div/div[1]/div[5]/div/div[2]/div[2]/div/div[1]").click()  # 첫번째 여행사 선택
            time.sleep(2)
            driver.switch_to.window(driver.window_handles[-1])

            mail_title = "조건에 맞는 항공권을 발견했습니다"
            mail_body = f"""{flight} {str(h).zfill(2)}:{str(m).zfill(2)} 출발
{price_str}원

가장 저렴한 여행사 예약링크로 이동합니다. 
결제를 진행해주세요!

{driver.current_url}
"""

            mail.send_to_me(mail_title, mail_body)
            print("Success!")
            found = True
            break

    if found:
        break
    print(f"Try #{cnt} Failed.", "30초 후 다시 탐색합니다...")
    cnt += 1
    time.sleep(30)
