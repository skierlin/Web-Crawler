import requests
import pandas as pd
import json
import pprint

def getContract():
    df = pd.read_csv('address_bsc.csv')
    # print(df)
    return df['address']

fakeHeaders = {'User-Agent': #用于伪装浏览器发送请求
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \ '
'Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77',
'Accept': 'text/html,application/xhtml+xml,*/*'}

data = []
name = ['wallet', 'buy_amount', 'sell_amount', 'buy_volume', 'sell_volume', 'buy_times', 'sell_times', 'profit',
        'profit_rate']
# contracts = getContract()
# print(contracts)
index = 1
profit = 1
# for index in range(1,6):
while profit > 0:
    try:
        url = f"https://pc.diting.ai/api/dex/profit/analysis?token=0x416162b73cf0168a01c525cd3040d05f25ecf5a2&chain=bsc&pageIndex={index}&desc=true"
        res2 = requests.get(url, headers = fakeHeaders)
        print("index = " + str(index))
        # print(res2.text)
        # print(type(res2.text))
        json_data = json.loads(res2.text)
        each_msg = json_data['data']['list']
        # print(*json_data['data']['list'], sep="\n")

        for i in range(20):
            it = each_msg[i]
            if (it['profit'] > 0):
                data1 = [it['wallet'], it['buy_amount'], -it['sell_amount'], it['buy_volume'], -it['sell_volume'], it['buy_times'],
                         it['sell_times'], it['profit'], it['profit_rate']]
                # print(data1)
                data.append(data1)
            else:
                profit = -1
                break
        index = index + 1
        print("last profit : " + str(each_msg[19]['profit']))

    except Exception as e:
        print(e)

print(len(data))
print(*data, sep="\n")


df = pd.DataFrame(data= data, columns= name)
print(df)
df.to_csv('Renmine')


