from bs4 import BeautifulSoup
import  requests
import smtplib

url='https://www.amazon.in/Nikon-TC-20E-Teleconverter-AF-S-Lenses/dp/B00JGJAQQE/ref=sr_1_2?crid=2VBNEVZNW6P6L&dchild=1&keywords=nikon+teleconverter+2x&qid=1595920504&sprefix=nikon+tele%2Caps%2C321&sr=8-2'
url1='https://www.amazon.in/HASTHIP%C2%AE-Colorful-Electronic-Extension-Silver/dp/B07YFG2V6M/ref=pd_sbs_23_1/262-8864297-9406867?_encoding=UTF8&pd_rd_i=B07YFG2V6M&pd_rd_r=60fb35a7-ec4d-43b5-9081-9b4ac86dff4d&pd_rd_w=mYkjj&pd_rd_wg=otHLY&pf_rd_p=00b53f5d-d1f8-4708-89df-2987ccce05ce&pf_rd_r=D5BTDGSVQNMRVNXDVP8W&psc=1&refRID=D5BTDGSVQNMRVNXDVP8W'
def price_check():
    header={"user-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}
    page= requests.get(url,headers=header)
    soup=BeautifulSoup(page.content,'html.parser')
    #print(soup.prettify())
    title=soup.find(id='productTitle').get_text()

    print(title.strip())
    price=soup.find(id='priceblock_ourprice').get_text()
    converted_price=price[1:8]
    m ,o= converted_price.split(',')
    n = str(m)
    converted_price=n + str(o)
    if  int(converted_price) > 40000:
        print('price is low')
        list = []
        send_mail(list)

    print(converted_price)

def send_mail(list):

    # message to be sent
    message = "its time for purchasing " + ' , '.join(list)
    mail_id = ['chessmanikanta@gmail.com', 'chessmanikanta@gmail.com']
    for i in mail_id:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login("chessmanikanta@gmail.com", "1156@Ismylife")
        server.sendmail(mail_id, i, message)
        server.quit()

price_check()