# -*- coding: utf-8 -*-
import time
import datetime
import requests
# http://push2his.eastmoney.com/api/qt/stock/kline/get?cb=jQuery112401779541629980841_1575296121360&secid=1.000001&ut=fa5fd1943c7b386f172d6893dbfba10b&fields1=f1%2Cf2%2Cf3%2Cf4%2Cf5&fields2=f51%2Cf52%2Cf53%2Cf54%2Cf55%2Cf56%2Cf57%2Cf58&klt=101&fqt=0&beg=19900101&end=20220101&_=1575296121361

def get_next_month_date():
    now = datetime.datetime.now()
    if now.day < 15:
        next_month = now + datetime.timedelta(days=31)
    else:
        next_month = now + datetime.timedelta(days=21)

    return "%04d%02d01" % (next_month.year, next_month.month)

def get_stock_day_data(code):
    url = r'http://push2his.eastmoney.com/api/qt/stock/kline/get'
    session = requests.session()
    """Accept: */*
    Accept-Encoding: gzip, deflate
    Accept-Language: zh-CN,zh;q=0.9
    Connection: keep-alive
    Cookie: qgqp_b_id=f4f0f8a3737f39cad08b5740421122e7; em_hq_fls=js; st_si=32527865650162; st_asi=delete; em-quote-version=topspeed; HAList=f-0-000001-%u4E0A%u8BC1%u6307%u6570%2Ca-sz-300059-%u4E1C%u65B9%u8D22%u5BCC; st_pvi=14243683468449; st_sp=2019-12-02%2000%3A09%3A46; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=11; st_psi=20191202221521546-113200301324-0912382810
    Host: push2his.eastmoney.com
    Referer: http://quote.eastmoney.com/zs000001.html
    User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"""
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Cookie": "qgqp_b_id=f4f0f8a3737f39cad08b5740421122e7; em_hq_fls=js; st_si=32527865650162; st_asi=delete; em-quote-version=topspeed; HAList=f-0-000001-%u4E0A%u8BC1%u6307%u6570%2Ca-sz-300059-%u4E1C%u65B9%u8D22%u5BCC; st_pvi=14243683468449; st_sp=2019-12-02%2000%3A09%3A46; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=11; st_psi=20191202221521546-113200301324-0912382810",
        "Host": "push2his.eastmoney.com",
        "Referer": "http://quote.eastmoney.com/zs000001.html",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    }
    """
    cb: jQuery112401779541629980841_1575296121360
    secid: 1.000001
    ut: fa5fd1943c7b386f172d6893dbfba10b
    fields1: f1,f2,f3,f4,f5
    fields2: f51,f52,f53,f54,f55,f56,f57,f58
    klt: 101
    fqt: 0
    beg: 19900101
    end: 20220101
    _: 1575296121361
    """
    params = {
        "cb": "jQuery112401779541629980841_1575296121360",
        "secid": "1.%06d"%code,
        "ut": "fa5fd1943c7b386f172d6893dbfba10b",
        "fields1": "f1,f2,f3,f4,f5",
        "fields2": "f51,f52,f53,f54,f55,f56,f57,f58",
        "klt": "101",
        "fqt": "0",
        "beg": "19900101",
        "end": get_next_month_date(),
        "_": "%d" % int(time.time()*1000)
    }
    print(params)
    resp = session.get(url, headers=headers, params=params)
    print(resp.content)

if __name__ == '__main__':
    datetime.timedelta()
    get_stock_day_data(1)