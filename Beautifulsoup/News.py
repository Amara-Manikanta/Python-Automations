from bs4 import BeautifulSoup
import  requests

url1='https://www.google.com/search?q=space+news&rlz=1C1GCEB_enIN885IN885&sxsrf=ALeKk01r6tikepgK1NI8Cl8mMNPej-' \
    'WSTA:1595934902208&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiv17jn6O_qAhVo63MBHQtsBJkQ_AUoAXoECBgQAw&biw=1216&bih=650'
url='https://www.google.com/search?q=kakinada+corna+virus&rlz=1C1GCEB_enIN885IN885&oq=kakinada+corna+virus&aqs=chrome..69i57j0l7.7808j0j7&sourceid=chrome&ie=UTF-8'
header={"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
page= requests.get(url,headers=header)
soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

#title=soup.find(role="heading").get_text()
#title=soup.find_all("div", {"role": "heading"})
title = soup .findAll(role="heading")
headlines=[]
for i in title:
    m=i.get_text()
    headlines.append(m)
    print('\n')

print(headlines)
#class="JheGif nDgy9d"
#class ="JheGif nDgy9d"