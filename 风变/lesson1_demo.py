import requests

# demo1 三国文字获取
# res = requests.get('https://localprod.pandateacher.com/python-manuscript/crawler-html/sanguo.md')
# print(res.text)
# novel=res.text
# k = open('《三国演义》.txt','a+')
# k.write(novel)
# k.close()

# demo2 : 获取图片
res2 = requests.get("https://res.pandateacher.com/2018-12-18-10-43-07.png")
pic = res2.content
photo = open('ppt.jpg', 'wb')
photo.write(pic)
photo.close()