import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.naver.com/').text
soup = BeautifulSoup(html, 'html.parser')

title_list = soup.select('.PM_CL_realtimeKeyword_rolling span[class*=ah_k]')
issue = []

for title in title_list[:10]:
    issue.append(title.text)