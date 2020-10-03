import execjs
import requests
import time
import json

def get_js_function(js_path, func_name,  func_args1):
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
        return ctx.call(func_name, func_args1)



def loginre(coun,pas):
    url ='https://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.15)&_=1576838753093'
    header={
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Length': '514',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': 'login=e5e8571d42ffdfe74d93d3d0cd37d474; ULOGIN_IMG=tc-9e586821ce211518ced6caae98b456b09ef0',
    'Host': 'login.sina.com.cn',
    'Origin': 'https://login.sina.com.cn',
    'Referer': 'https://login.sina.com.cn/signup/signin.php?entry=sso',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }
    data={
    'entry': 'sso',
    'gateway': '1',
    'from': 'null',
    'savestate': '30',
    'useticket': '0',
    'pagerefer': '',
    'vsnf': '1',
    'su': coun,
    'service': 'sso',
    'servertime': '1576838743',
    'nonce': 'XMHL47',
    'pwencode': 'rsa2',
    'rsakv': '1330428213',
    'sp': pas,
    'sr': '1920*1080',
    'encoding': 'utf-8',
    'cdult': '3',
    'domain': 'sina.com.cn',
    'prelt': '9441',
    'returntype': 'TEXT',
    }
    loginre = requests.post(url,headers=header,data=data)
    tt = json.loads(loginre.text)

    print(tt)
   



if __name__=='__main__':
##账号密码   
    pas= get_js_function('weibo.js','mima','xxx')
    coun = get_js_function('weibo.js','encode','xxx')
    loginre(coun,pas)
