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


def request1():
    url = 'https://h5api.m.taobao.com/h5/mtop.taobao.idle.mach.item.service.faas.item/1.0/?'
    t = time.time()*1000
    sign = get_js_function('xianyu.js', 'yuu', t)
    params = {
        'jsv': '2.5.6',
        'appKey': '12574478',
        't': t,
        'sign': sign,
        'api': 'mtop.taobao.idle.mach.item.service.faas.item',
        'v': '1.0',
        'uttid': 'ee66361e81e8',
        'type': 'jsonp',

        'dataType': 'jsonp',
        'callback': 'mtopjsonp7',
        'data': '{"utdid":"ee66361e81e8","dataSourceId":"376","pageNumber":4,"catIds":""}'

    }
    print(sign)

    head = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie':
        'referer': 'https://2.taobao.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',

    }

    respone = requests.get(url, params=params, headers=head)
    return respone.text


if __name__ == '__main__':
    a = request1()
    print(a)

