import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup

start_url = 'https://www.youtube.com/c/%EB%9D%BC%EC%9D%B4%EB%B8%8C%EC%95%84%EC%B9%B4%EB%8D%B0%EB%AF%B8/videos'

def url_crawling(url):
    isabe = pd.DataFrame({'name':[],
                             'video_url':[],
                                             })

    # 크롬드라이브 경로 설정해주기!
    browser = webdriver.Chrome('D:/chromedriver')
    browser.implicitly_wait(3)

    # 원하는 채널 동영상목록 url
    start_url = url
    browser.get(start_url)
    browser.maximize_window()

    browser.find_element_by_xpath('//*[@class="scrollable style-scope paper-tabs"]/paper-tab[2]').click()

    body = browser.find_element_by_tag_name('body')
    time.sleep(3)
    num_of_pagedowns = 14
    #10번 밑으로 내리는 것

    while num_of_pagedowns:
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(2) # 2초씩 쉬기 때문에 20초 면10번 스크롤을 내림..
        num_of_pagedowns -= 1

    html0 = browser.page_source
    html = BeautifulSoup(html0,'html.parser')
    video_ls=html.find_all('ytd-grid-video-renderer',{'class':'style-scope ytd-grid-renderer'})
    b = html.find('div',{'id':'items','class':'style-scope ytd-grid-renderer'})

    tester_url = []

    for i in range(len(video_ls)):
        url = start_url+video_ls[i].find('a',{'id':'thumbnail'})['href']
        tester_url.append(url)

    return tester_url

if __name__ == '__main__':
    url_crawling(start_url)