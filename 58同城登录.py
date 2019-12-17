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


def login():
    ps = 'yinfeng666'
    ps1=get_js_function('58.js', 'password', ps)

    url = 'https://passport.58.com/58/login/pc/dologin'
    data = {
        'username': '15081282722',
        'password': ps1,
        'token': 'bFR7DwTt_YPFsIUL0UGYn-5X12RP6ChD',
        'source': '58-default-pc',
        'path': 'https%3A%2F%2Fsjz.58.com%2F%3Fpts%3D1576595679284',
        'domain': '58.com',
        'finger2': 'zh-CN|24|1.25|4|1536_864|1536_824|-480|1|1|1|undefined|1|unknown|Win32|unknown|3|false|false|false|false|false|0_false_false|d41d8cd98f00b204e9800998ecf8427e|4ff9a5d795e772694fcffa238df1f6ef',
        'psdk-d': 'jsdk',
        'psdk-v': '1.0.2',
        'fingerprint': 'tE3IrPQKUqgMzOaAlxvWi94CUW0DUvPl',
        'callback': 'SDK_CALLBACK_FUN.successFun',

    }
    header = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'content-length': '775',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'myLat=""; myLon=""; id58=2E60q133jh/NynmeNdcOaA==; mcity=sjz; city=sjz; 58home=sjz; 58tj_uuid=46158e7d-24c5-4a84-9699-7d86bd93e52b; als=0; wmda_new_uuid=1; wmda_uuid=758aacd78fa3677486e1145319d9e0ee; wmda_visited_projects=%3B11187958619315%3B10104579731767; xxzl_deviceid=6y1HdGkVaP%2Bv6ksQymRiFT3zT3RIFITWrgHkkLUadCU4CqN9WL0dIV9%2FYfdt0wcY; xxzl_cid=008d4031dd3c45ffbc4ae0bb14e94153; new_session=1; new_uv=3; utm_source=; spm=; init_refer=; xzuid=bc124b2d-455d-44fb-abb7-55709e83ad00; wmda_session_id_10104579731767=1576595680365-a0b9dc45-49c2-ff65; ppStore_fingerprint=9B1F2B5E2C03AAEF1A898E94922E1CA621DB3BD122764D2D; finger_session=tE3IrPQKUqgMzOaAlxvWi94CUW0DUvPl',
        'origin': 'https://passport.58.com',
        'pragma': 'no-cache',
        'referer': 'https://passport.58.com/login/?path=https%3A//sjz.58.com/&PGTID=0d100000-000f-11ae-f77d-af456bc2d480&ClickID=1',
        'sec-fetch-mode': 'nested-navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',

    }
    response = requests.post(url, data=data, headers=header)
    print(response.text)



if __name__=='__main__':
    login()
