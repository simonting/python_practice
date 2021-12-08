import requests
from bs4 import BeautifulSoup
import os
data = []

cookies = {'over18':'1'}

search_input= input("請輸入想要搜尋的關鍵字:")
print( "關鍵字:"+ search_input)

file_exists = os.path.isfile('./result.txt')

if file_exists == True:
    os.remove('./result.txt')


for id in range(1,3):
    url = "https://www.ptt.cc/bbs/Beauty/index" + str(id) +".html"
    response = requests.get(url, cookies=cookies)
    status = response.status_code
    Soup = BeautifulSoup(response.text, 'html.parser')

    if status == 200:
        for i in Soup.find_all(class_="r-ent"):
            title = i.find(class_="title").a.text
            if search_input in title:
                current_data = {}
                current_data['title_result'] = title
                current_data['url_result'] = "https://www.ptt.cc"+i.find(class_="title").a['href']
                data += [current_data]

    else:
        break
for i in data:
    result = i['title_result'] + i['url_result'] + "\n"
    with open ('result.txt','a', encoding='utf-8') as f:
        f.write(result)

file_check = os.path.isfile('./result.txt')


if file_check == True:
    print ("請查看result.txt")
else:
    print("找不到關鍵字")
