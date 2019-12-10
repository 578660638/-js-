import requests
import json
import execjs
import requests
import time


def get_js_function(js_path, func_name, func_args):
    '''
    获取指定目录下的js代码, 并且指定js代码中函数的名字以及函数的参数。
    :param js_path: js代码的位置
    :param func_name: js代码中函数的名字
    :param func_args: js代码中函数的参数
    :return: 返回调用js函数的结果
    '''

    with open(js_path, encoding='utf-8') as fp:
        js = fp.read()
        ctx = execjs.compile(js)
        return ctx.call(func_name, func_args)
'''
 获取指定目录下的js代码, 并且指定js代码中函数的名字以及函数的参数。
 :param js_path: js代码的位置
 :param func_name: js代码中函数的名字
 :param func_args: js代码中函数的参数
 :return: 返回调用js函数的结果


 '''
offect = 20
yeshu = get_js_function('baiduyun.js','yinyue',offect)
data = {
    'params': yeshu['encText'],
    'encSecKey': yeshu['encSecKey']
    }
header = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'content-length': '476',
    'content-type': 'application/x-www-form-urlencoded',
    'cookie': 'JSESSIONID-WYYY=sbcWZYMPoYFO28nWCG3pBrBd4jKVhSG%5Cci2edMhF19p6EpWEwtds%5CmUUw5n5ASMnWcJMdf9PF0OwNmEDJxaMSRyMczKmC%2Bzw0pV5e%2FgcdDlAX8jpweoI8GRlVz%2BgcnSvcbfFk8vF2v5CDWKUOEd2%5Cy%2FgrrJ1SaFjAm%2BCfiJOiscpzx5z%3A1575970328707; _iuqxldmzr_=32; _ntes_nnid=59d73f0d101235375f5c46b23362b88b,1575968528780; _ntes_nuid=59d73f0d101235375f5c46b23362b88b; WM_NI=zuw13pvie7Fxpj2%2FdOy4JXgF6rMpcD0951rwYuG7VyNmio%2BW7Jw%2Bzn7Zeyctp%2FbOZnT9WEqVUs5Ek2GtHWuefuzIRttLDcAjejgIvAU4h%2F1l22RyeTCaowB4l%2F5pjujlRkU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee83b164b39aa490cb4eb2968eb3d54b928e8b84b72189a6bfb3e240abb0ba8ee82af0fea7c3b92abaabb9d2b27cb6b7abd8c574b4b6fed0e745bbec86b9e64ef6ae8391e250f4e7fbd2f17d9bab89d8d5738eb3a790aa5df596b9ccf966f586ab9ae280b4f1aeb0d96698e799a6f45e97adfba6ea3a85ac88b8f86fa6abb6aad180b8948c84c462a7b6a9aaf54b97eca8d0b468f2ee9e9ae86081bfa198c140b0f1fb91e97faab49e8cd837e2a3; WM_TID=Tt0LfCdvZkhBEFVQAUdt6e3qRJ5y9uyP; playerid=54620300',
    'origin': 'https://music.163.com',
    'referer': 'https://music.163.com/song?id=1374056689',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',



}

url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_1374056689?csrf_token='
request1 = requests.post(url, data=data, headers=header)
print(request1.text)

