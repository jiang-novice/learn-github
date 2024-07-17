import time


tinydict = {'RUNOOB' : {'url' : 'www.runoob.com'},'Name': 'Runoob', 'Age': 7}

if 'RUNOOB' in tinydict and 'url' in tinydict['RUNOOB']:
    url = tinydict.get('RUNOOB', {}).get('url', None)
    print(url)
    test = tinydict.get("dd",dict()).get("dd", "no this key")
    print(test)


for key, value in tinydict.items():
    print("key:", key)
    print("value:", value)
    print()

ha = [i+1 for i in range(50)]

   
    