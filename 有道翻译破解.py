import execjs
import requests

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

def request1(word):
    a = get_js_function('youdao.js', 'youdao', word)
    head = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '242',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1602708304@101.24.158.18; OUTFOX_SEARCH_USER_ID_NCOO=808601871.0569409; _ntes_nnid=33b4adc8f150c4b5cb4449fe2a669c72,1570714300146; JSESSIONID=aaapIxALwum5kd9Zeia7w; ___rl__test__cookies=1575212668960',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Pragma': 'no-cache',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',

    }
    datas = {
        'i': word,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': a['salt'],
        'sign': a['sign'],
        'ts': a['ts'],
        'bv': a['bv'],
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
    }
    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
    respone = requests.post(url, headers=head,data=datas)
    print(respone.text)


if __name__ == '__main__':
    while True:
        a = input('请你输入一个数')
        request1(a)
