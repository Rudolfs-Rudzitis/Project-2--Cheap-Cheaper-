import requests
from bs4 import BeautifulSoup
import smtplib
import time
# Enter a link to an item of your choice to check it's price
URL = "https://www.amazon.com/Monikers-WAV01-Wavelength/dp/B07T446163/ref=sr_1_19?dchild=1&keywords=board+games&pf_rd_i=21439846011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=a8bcad66-2a7f-405d-b0e0-8b0e94ebfd3d&pf_rd_r=XFF9KTYTKFK08MM8JB7C&pf_rd_s=merchandised-search-6&pf_rd_t=101&qid=1615793154&sr=8-19"

# To know your 'User-Agent' just Google it and copy it below
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,lv;q=0.8"
}

def check_price():
    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:3])

    if(converted_price < 20):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price > 20):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
# Enter your email and password from you want to send Price Alert
    server.login('test.python.exercise@gmail.com', 'examplepassword')

    subject = 'Price fell down!'
    body = 'Hurry up! Check the link  https://www.amazon.com/Monikers-WAV01-Wavelength/dp/B07T446163/ref=sr_1_19?dchild=1&keywords=board+games&pf_rd_i=21439846011&pf_rd_m=ATVPDKIKX0DER&pf_rd_p=a8bcad66-2a7f-405d-b0e0-8b0e94ebfd3d&pf_rd_r=XFF9KTYTKFK08MM8JB7C&pf_rd_s=merchandised-search-6&pf_rd_t=101&qid=1615793154&sr=8-19'

# Below we construct message that we will send, and specify email that will send and email that will receive it
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'test.python.exercise@gmail.com',
        'rudzitisrio@gmail.com',
        msg
    )
    print('Email has been sent')

    server.quit()

# Make the code run once a day (there is a 86400 seconds in a day)
while(True):
    check_price()
    time.sleep(86400)