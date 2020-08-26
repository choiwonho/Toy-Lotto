from bs4 import BeautifulSoup
import requests
import random
import re
from selenium import webdriver

'''
driver = webdriver.chrome('/Users/apple/Downloads/chromedriver')

driver.implicitly_wait(3)
url = 'https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo=1'
driver.get()
'''

page = 1
total_dic = {}
n_array = ()

# 회차 설정 (1 ~ page_num)
def set_page(page_num):
    page_num = page_num + 1
    for page in range(page_num):
        crawl_page(page)
        print (page)


# 실제 크롤링 메서드
def crawl_page(page):
    url = f'https://www.dhlottery.co.kr/gameResult.do?method=byWin&drwNo={page}'
    response = requests.get(url)
    temp_response = response.text
    soup = BeautifulSoup(temp_response)

    temp_number = soup.find("div", {"class":"nums"})

    num_arr = []
    for number in temp_number.find_all("span"):
        number = number.get_text(" ", strip=True)
        if number == "":
            continue
        num_arr.append(number)

    extration_num(num_arr)

# 번호 추출 및 저장
def extration_num(num_arr):
    for number in num_arr:
        if number in total_dic:
            total_dic[number] = total_dic[number] + 1
        else:
            total_dic[number] = 1

    return total_dic.items()
    #n_count(total_dic.items())

    #result = sorted(total_dic.items(), key=lambda x: x[1], reverse=True)

# n번 이상 나온 번호 조합 (1번)
def n_count(total_dic, n):
    result = []
    for num, count in zip(total_dic.keys(),total_dic.values()):
        if int(count) > int(n):
            result.append(num)
        else:
            continue
    predict_num(result)


# 예측번호 추출
def predict_num(result):
    predict_list = []
    count = 0

    while count <= 5:
        predict_number = random.sample(result, 6)
        predict_list.append(predict_number)
        count += 1
    print (predict_list)

# 추출된 예측번호 훈련
# 특정회차 input으로 받고 ncount값 이랑 최대한 비슷하게 나올 수 있도록

if __name__  == '__main__':
    set_page(919)
    #
    n = 120
    n_count(total_dic, n)



