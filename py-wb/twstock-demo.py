# 取得 ip 列表
# from getProxyIp import getProxiesFromProxyNova
# import sys
# print(getProxiesFromProxyNova())
# sys.exit()
# twstock.__update_codes()


# from twstock.proxy import RoundRobinProxiesProvider
import twstock

# proxies = getProxiesFromProxyNova()
# for index in range(len(proxies)):
#     proxies[index] = {'https': f'https://{proxies[index]}'}
# # print(proxies)
# # sys.exit()
# # proxies = [{'http': 'http://localhost:5000'}, {'http': 'http://localhost:5001'}]
# rrpr = RoundRobinProxiesProvider(proxies)
# twstock.proxy.configure_proxy_provider(rrpr)

from twstock import Stock
from twstock import BestFourPoint

def run(argv):
    for sid in argv:
        s = twstock.Stock(sid)
        print('-------------- %s ---------------- ' % sid)
        print('high : {:>5} {:>5} {:>5} {:>5} {:>5}'.format(*s.high[-5:]))
        print('low  : {:>5} {:>5} {:>5} {:>5} {:>5}'.format(*s.low[-5:]))
        print('price: {:>5} {:>5} {:>5} {:>5} {:>5}'.format(*s.price[-5:]))

def work(argv):
    print('四大買賣點判斷 Best Four Point'
    )
    for sid in argv:
        stock = Stock(sid)
        bfp = BestFourPoint(stock)
        bfp = bfp.best_four_point()
        print('%s: ' % (sid), end='')
        print(bfp)
        if bfp:
            if bfp[0]:
                print('Buy  ', bfp[1])
            else:
                print('Sell ', bfp[1])
        else:
            print("Don't touch")

values = [
    '2014'
]

run(values)
work(values)