import requests
import demjson
from lxml import html
from bs4 import BeautifulSoup
import re
from fake_useragent import UserAgent

# 當日跌幅
STOCK_DOWN_URL = 'https://fubon-ebrokerdj.fbs.com.tw/Z/ZG/ZG_AA.djhtm'
stockDown = requests.get(STOCK_DOWN_URL, headers = {'user-agent': UserAgent().random})
soup = BeautifulSoup(stockDown.text, 'html.parser')
ele = soup.find_all('td', attrs={'class': 't3n0'})
mainList = []
for x in ele:
    # print(x.text)
    y = x.find_next_siblings()[0]
    sid = y.find('a')['href'].split("javascript:Link2Stk('")[1].split("')")[0]
    name = y.text[6:]
    dealQty = x.find_next_siblings()[-1].text #.replace(',', '')
    if len(x.find_next_siblings()) != 5:
        mainList.append({
            'sid': sid,
            'name': name
        })
    else:
        if int(dealQty.replace(',', '')) > 1000:
            mainList.append({
                'sid': sid,
                'name': name
            })

print(mainList)
print(len(mainList))


ENTER_POINT = 'https://www.cmoney.tw/finance/technicalanalysis.aspx?s=2330'

session_requests = requests.session()
request_headers = {'user-agent': UserAgent().random}
result = session_requests.get(ENTER_POINT, headers = request_headers)


# 抓取網頁的 cmkey
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


# 建立 CSV 檔寫入器
import csv
with open('output.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # 寫入一列資料
    writer.writerow(['代號', '名稱', '日期', '收盤價', '五日線', '跌破五日', '成交量', 'K值', 'D值', 'KD值', 'DIF-MACD'])

    for obj in mainList:
        result = getStock(obj['sid'], cookie, cmkeyCode)
        jsonFormat = demjson.decode(result.content)
        # print(jsonFormat)
        # {'Date': '20210719', 'OpenPr': 35.9, 'HighPr': 37.7, 'LowPr': 34.25, 'ClosePr': 34.55, 'PriceDifference': -0.8, 'MagnitudeOfPrice': -2.26, 'MA5': 33.1, 'MA20': 35.4, 'MA60': 23.92, 'DealQty': 27467, 'K9': 37.47, 'D9': 31.98, 'DIF': 2.733, 'MACD': 3.776, 'DIF_MACD': -1.043, 'RSI5': 49.4, 'RSI10': 52.92}
        stockObj = {
            '名稱': obj['name'].replace("\n", "").replace("\r", "").replace(" ", ""),
            '日期': jsonFormat[0]['Date'],
            '收盤價': jsonFormat[0]['ClosePr'],
            '跌破五日': float(jsonFormat[0]['ClosePr']) - float(jsonFormat[0]['MA5']),
            'K值': jsonFormat[0]['K9'],
            'D值': jsonFormat[0]['D9'],
            'KD值': float(jsonFormat[0]['K9']) - float(jsonFormat[0]['D9']),
            'DIF': jsonFormat[0]['DIF'],
            'MACD': jsonFormat[0]['MACD'],
            'DIF-MACD': jsonFormat[0]['DIF_MACD'],
            '成交量': jsonFormat[0]['DealQty'],
            '五日線': jsonFormat[0]['MA5'],
        }
        if float(stockObj['K值']) < 40:
            writer.writerow([obj['sid'], stockObj['名稱'], stockObj['日期'], stockObj['收盤價'], stockObj['五日線'], stockObj['跌破五日'], stockObj['成交量'], stockObj['K值'], stockObj['D值'], stockObj['KD值'], stockObj['DIF-MACD']])
            sList.append(stockObj)

print(sList)