import requests
import pandas as pd
import json
import pprint


def getContract():
    df = pd.read_csv('address_bsc.csv')
    addresses = list(df['address'])
    names = list(df['name'])
    result = dict(zip(addresses, names))

    # print(df)
    return result


fakeHeaders = {'User-Agent':  # 用于伪装浏览器发送请求
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) \ '
                   'Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.77',
               'Accept': 'text/html,application/xhtml+xml,*/*'}

data = []
column = ['wallet', 'buy_amount', 'sell_amount', 'buy_volume', 'sell_volume', 'buy_times', 'sell_times', 'profit',
        'profit_rate']
all_info = getContract()
# print(contracts)
index = 1
profit = 1

for contract, name in all_info.copy().items():
    print(name)
    print(contract)
    contract = contract.casefold()
    while profit > 0:
        try:
            url = f"https://pc.diting.ai/api/dex/profit/analysis?token={contract}&chain=bsc&pageIndex={index}&desc=true"
            print(url)
            res2 = requests.get(url, headers=fakeHeaders)
            print("index = " + str(index))
            # print(res2.text)
            # print(type(res2.text))
            json_data = json.loads(res2.text)
            each_msg = json_data['data']['list']
            # print(*json_data['data']['list'], sep="\n")

            for i in range(20):
                it = each_msg[i]
                if (it['profit'] > 0):
                    data1 = [it['wallet'], it['buy_amount'], -it['sell_amount'], it['buy_volume'], -it['sell_volume'],
                             it['buy_times'],
                             it['sell_times'], it['profit'], it['profit_rate']]
                    # print(data1)
                    data.append(data1)
                else:
                    profit = -1
                    break
            index = index + 1
            print("last profit : " + str(each_msg[19]['profit']))

        except Exception as e:
            profit = -1
            index = 1
            print("break")
            print(e)

    # print(len(data))
    # print(*data, sep="\n")

    index = 1
    profit = 1
    df = pd.DataFrame(data=data, columns=column)
    print(df)
    filename = name + '.csv'
    df.to_csv(filename)
