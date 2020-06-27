#! /usr/bin/python3
# -*- coding: utf-8 -*-

import json
import requests
import getpass
import pandas as pd
from typing import Dict

url = 'https://opendata.sz.gov.cn/api/29200_00403601/1/service.xhtml'
api_key = getpass.getpass('api key: ')
rows = 10000
pages = 134


def req_data(page: int, rows: int, url: str = url, api_key: str = api_key,
             method: str = 'POST') -> str:
    fun = {'GET': requests.get, 'POST': requests.post}[method]
    res = fun(url, params={'page': page, 'rows': rows, 'appKey': api_key})
    return res


def json_to_pd(json: Dict) -> pd.DataFrame:
    assert set(json.keys()) == {'data', 'page', 'rows', 'total'}
    return pd.DataFrame(json['data'])


def save_pd(df: pd.DataFrame, page: int) -> str:
    df.to_csv('data/data%d.csv' % (page), index=False, quoting=2)
    return 'page %d fetched.' % (page)


if __name__ == "__main__":
    for page in range(pages):
        res = req_data(page=page+1, rows=rows)
        dat = json.loads(res.text)
        save_pd(json_to_pd(dat), page=page+1)
