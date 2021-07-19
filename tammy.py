import requests
import demjson
from lxml import html
from bs4 import BeautifulSoup as bs
from fake_useragent import UserAgent

ENTER_POINT = 'https://www.cmoney.tw/finance/technicalanalysis.aspx?s=2330'

session_requests = requests.session()
request_headers = {'user-agent': UserAgent().random}
result = session_requests.get(ENTER_POINT, headers = request_headers)


# 抓取網頁的 cmkey
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(result.content, 'html.parser')
ele = soup.find('a', title=re.compile('技術分析'))

# sid = '00881'
cookie = result.headers['Set-Cookie']
cmkeyCode = ele['cmkey']

def getStock(sid='', cookie='', cmkey=''):
    mainHeader = {
        'user-agent': UserAgent().random,
        'Cookie': cookie,
        'Referer': f'https://www.cmoney.tw/finance/technicalanalysis.aspx?s={sid}'
    }

    url = f'https://www.cmoney.tw/finance/ashx/MainPage.ashx?action=GetTechnicalData&stockId={sid}&time=d&range=1&cmkey={cmkey}'

    return session_requests.get(url, headers = mainHeader)
main = ['2611', '2613', '2617', '2637']
# main = ['2611']
sList = []

for sid in main:
    result = getStock(sid, cookie, cmkeyCode)
    jsonFormat = demjson.decode(result.content)
    # print(jsonFormat)
    # {'Date': '20210719', 'OpenPr': 35.9, 'HighPr': 37.7, 'LowPr': 34.25, 'ClosePr': 34.55, 'PriceDifference': -0.8, 'MagnitudeOfPrice': -2.26, 'MA5': 33.1, 'MA20': 35.4, 'MA60': 23.92, 'DealQty': 27467, 'K9': 37.47, 'D9': 31.98, 'DIF': 2.733, 'MACD': 3.776, 'DIF_MACD': -1.043, 'RSI5': 49.4, 'RSI10': 52.92}
    sList.append({
        '日期': jsonFormat[0]['Date'],
        'K值': jsonFormat[0]['K9'],
        'D值': jsonFormat[0]['D9'],
        'DIF': jsonFormat[0]['DIF'],
        'MACD': jsonFormat[0]['MACD'],
        'DIF-MACD': jsonFormat[0]['DIF_MACD'],
        '交易量': jsonFormat[0]['DealQty'],
        '五日線': jsonFormat[0]['MA5'],
    })

print(sList)