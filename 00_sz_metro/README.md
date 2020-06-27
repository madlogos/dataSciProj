# 深圳地铁通数据

中文版 | [English Version](README_en.md)

## 数据提取

[数据集](https://opendata.sz.gov.cn/data/dataSet/toDataDetails/29200_00403601)来自[深圳市开放数据平台](https://opendata.sz.gov.cn)，共133.7万条记录，包含2018-8-31到9-1的样例数据。

样例数据只有1万条。下载全量数据需要申请appKey：

1. 在深圳开放数据平台注册并[申报应用](https://opendata.sz.gov.cn/application/develop/referApplication)。
2. 审批通过后，在[数据集页面](https://opendata.sz.gov.cn/data/api/toApiDetails/29200_00403601)的API服务文档页点击“订阅接口”，选中自己申报的应用并订阅。
3. 在[接口测试](https://opendata.sz.gov.cn/maintenance/personal/toApiTest)页提交表单，测试结果。可以获得JSON类型的返回结果。

```json
{"total":1337000,
 "data":[
     {"deal_date":"2018-08-31 22:14:50",
      "close_date":"2018-09-01 00:00:00",
      "card_no":"CBEHFCFCG",
      "deal_value":"0",
      "deal_type":"地铁入站",
      "company_name":"地铁五号线",
      "car_no":"IGT-105",
      "station":"布吉",
      "conn_mark":"0",
      "deal_money":"0",
      "equ_no":"263032105"},
     ...
 ],
 "page":1,
 "rows":2}
```

本项目中，用[get_data.py](get_data.py)脚本来获取全量数据。需要用到json, requests, getpass, pandas等包。利用`requests.post()`方法发送请求，每次获取1页数据（1万行），并转为pandas DataFrame，共计导出为134个.csv文件。

## 数据存储

存入Hive。

## 数据字段

序号 | 字段名称 | 字段描述
---:|---------|-----------
1 | card_no | 卡号
2 | deal_date | 交易日期时间
3 | deal_type | 交易类型
4 | deal_money | 交易金额
5 | deal_value | 交易值
6 | equ_no | 设备编码
7 | company_name | 公司名称
8 | station | 线路站点
9 | car_no | 车牌号
10 | conn_mark | 联程标记
11 | close_date | 结算日期

