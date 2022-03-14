import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json
import requests
from matplotlib import ticker
from pyecharts import options as opts
from pyecharts.charts import Map, BMap

def China_log_plot():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.max_rows', 1000)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False

    China = pd.read_csv('China.csv')
    China.plot('Date_String', logy=True)
    plt.title('China疫情地图折线对数图',)
    plt.savefig('China疫情地图折线对数图.png')
    plt.show()

def Us_log_plot():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.max_rows', 1000)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False

    Us = pd.read_csv('Us.csv')
    Us.plot('Date_String', logy=True)
    plt.title('Us疫情地图折线对数图')
    plt.savefig('Us疫情地图折线对数图.png')
    plt.show()

def Italy_log_plot():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.max_rows', 1000)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False

    Italy= pd.read_csv('Italy.csv')
    Italy.plot('Date_String', logy=True)
    plt.title('Italy疫情地图折线对数图')
    plt.savefig('Italy疫情地图折线对数图.png')
    plt.show()

def India_log_plot():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.max_rows', 1000)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False

    India= pd.read_csv('Italy.csv')
    India.plot('Date_String', logy=True)
    plt.title('India疫情地图折线对数图')
    plt.savefig('India疫情地图折线对数图.png')
    plt.show()

def India_plot():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.max_rows', 1000)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False

    India = pd.read_csv('Italy.csv')
    India.plot('Date_String')
    plt.title('India疫情地图折线图')
    plt.savefig('India疫情地图折线图.png')
    plt.show()

def China_plot():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.max_rows', 1000)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False

    China = pd.read_csv('China.csv')
    China.plot('Date_String')
    plt.title('China疫情地图折线图')
    plt.savefig('China疫情地图折线图.png')
    plt.show()

def Italy_plot():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.max_rows', 1000)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False

    Italy = pd.read_csv('Italy.csv')
    Italy.plot('Date_String')
    plt.title('Italy疫情地图折线图')
    plt.savefig('Italy疫情地图折线图.png')
    plt.show()

def US_plot():
    pd.set_option('display.max_columns', 1000)
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.max_rows', 1000)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False

    US = pd.read_csv('US.csv')
    US.plot('Date_String')
    plt.title('US疫情地图折线图')
    plt.savefig('US疫情地图折线图.png')
    plt.show()

def China_Province():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    url2 = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_foreign"
    # 伪装请求头
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'}
    # 获取网页数据
    r = requests.get(url, timeout=30, headers=headers)
    req = requests.get(url2, timeout=30, headers=headers)
    # 将数据json化去掉/,方便操作
    data = json.loads(r.text)
    data = json.loads(data['data'])

    data3 = json.loads(req.text)
    data3 = json.loads(data3['data'])

    # 从爬取的信息中提取所需信息
    china = data['areaTree'][0]['children']
    # 爬取各大国家疫情情况
    country = data3['countryAddConfirmRankList']

    chinaTotals = "确诊人数:" + str(data['chinaTotal']['confirm']) + \
                  "疑似人数:" + str(data['chinaTotal']['suspect']) + \
                  "死亡人数:" + str(data['chinaTotal']['dead']) + \
                  "治愈人数:" + str(data['chinaTotal']['heal']) + \
                  "更新日期:" + data['lastUpdateTime']
    print(type(chinaTotals))
    # 获取中国各省名称，确诊人数，疑似人数，死亡人数，治愈人数
    # 建立空列表保存数据
    Total = []
    for i in range(len(china)):
        Total.append([china[i]['name'], china[i]['total']['confirm'],
                      china[i]['total']['suspect'], china[i]['total']['dead'],
                      china[i]['total']['heal']])
    # 获取各国新增加确诊人数
    # 建立空列表保存数据
    Country = []
    for i in range(len(country)):
        Country.append([country[i]['nation'], country[i]['addConfirm']])
    # print(Country)
    # 将数据转换为二维表方便数据清洗和进一步的数据可视化
    data1 = pd.DataFrame(Total, index=range(1, 35), columns=['省份', '确诊人数', '疑似人数', '死亡人数', '治愈人数'])
    data4 = pd.DataFrame(Country, index=range(1, 11), columns=['国家', '新增确诊人数'])
    # print(data1)#查看输出二维表是否出错
    # 数据清洗
    # 查找是否有缺失值
    data1.isnull()
    data4.isnull()
    # 只显示存在缺失的行列
    data1[data1.isnull().values == True]
    data4[data4.isnull().values == True]
    # 查找重复值
    data1.duplicated()
    data4.duplicated()
    # 删除重复值
    data2 = data1.drop_duplicates()
    data5 = data4.drop_duplicates()
    # 统计空值
    data2.isna()
    data5.isna()
    # 进行数据可视化
    # 正常显示中文
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    # 正常显示负号
    plt.rcParams['axes.unicode_minus'] = False
    # 创建画布
    plt.figure(figsize=(15, 15))  # 设置画布大小
    # 绘制子图1
    axes1 = plt.subplot(2, 1, 2)
    X = data2.loc[:, '省份']
    Y = data2.loc[:, '确诊人数']
    # 绘制柱状图
    plt.bar(X, Y)
    # 标题
    plt.title('我国各省至今确诊人数')
    # x轴名称
    plt.xlabel('省份')
    # y轴名称
    plt.ylabel('确诊人数')
    # 绘制子图2
    axes2 = plt.subplot(2, 2, 2)
    # 绘制确诊人数,疑似人数,死亡人数,治愈人数的饼图
    a = [data['chinaTotal']['confirm'], data['chinaTotal']['suspect'],
         data['chinaTotal']['dead'], data['chinaTotal']['heal']]
    # 绘制饼图
    plt.pie(a, labels=['确诊人数', '疑似人数', '死亡人数', '治愈人数'])
    # 绘制子图3
    axes3 = plt.subplot(2, 2, 1)
    f = data5.loc[:, '国家']
    g = data5.loc[:, '新增确诊人数']
    # 绘制柱状图
    plt.bar(f, g)
    plt.title("国外新增确诊人数")
    plt.savefig("各国及各省病例直方图.jpg")
    plt.show()

def map_china() -> Map:
    f = pd.read_csv('中国各省份疫情数据.csv')
    p = f["省份"].to_list()
    a = f["确诊人数"].to_list()
    Province_Confirmed = dict(zip(p, a))
    map = Map()
    BMap(init_opts=opts.InitOpts(width="1200px", height="800px"))
    map.set_global_opts(
        title_opts=opts.TitleOpts(title="疫情地图"),
        visualmap_opts=opts.VisualMapOpts(max_=999999, is_piecewise=True,
                                          pieces=[
                                              {"max": 0, "min": 0, "lable": "0人",
                                               "color": "#FFCCFF"},
                                              {"max": 9, "min": 1, "label": "1-9人",
                                               "color": "#FFCCCC"},
                                              {"max": 99, "min": 10, "label": "10-99人",
                                               "color": "#FFCC99"},
                                              {"max": 499, "min": 100, "label": "100-499人",
                                               "color": "#FFCC00"},
                                              {"max": 999, "min": 500, "label": "500-999人",
                                               "color": "#FF9900"},
                                              {"max": 9999, "min": 1000, "label": "1000-9999人",
                                               "color": "#FF6600"},
                                              {"max": 999999, "min": 10000, "label": "10000人及以上",
                                               "color": "#FF3300"}, ]
                                          )
    )
    map.add(series_name="累计确诊病例", data_pair=list(Province_Confirmed.items()), maptype="china", zoom=1, center=[105, 38])
    map.render('中国疫情地图.html')

def china_us():
    China = pd.read_csv('中美国家Recovered.csv', index_col=0, sep=';')
    file_China = pd.read_csv('China.csv')
    file_US = pd.read_csv('US.csv')
    plt.title('9个国家治愈饼图')
    pd.set_option('display.max_columns', 1000)
    pd.set_option('max_colwidth', 1000)
    pd.set_option('display.max_rows', 1000)

    plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示中文标签
    plt.rcParams['axes.unicode_minus'] = False
    plt.title('中美国家治愈饼图')
    China['Recovered'].plot.pie(counterclock=False, startangle=-270)
    plt.show()


    fig, ax = plt.subplots()
    tick_spacing = 15  # 通过修改tick_spacing的值可以修改x轴的密度
    ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
    # 分析9个国家疫情趋势
    plt.title('分析中美国家的疫情趋势图')
    plt.plot(file_China['Date_String'], file_China['Confirmed'], label='China')
    plt.plot(file_China['Date_String'], file_US['Confirmed'], label='US')
    plt.legend()
    fig.savefig("分析中美国家的疫情趋势图.png")
    plt.show()


map_china()
China_plot()
US_plot()
India_plot()
Italy_plot()
China_log_plot()
Us_log_plot()
India_log_plot()
Italy_log_plot()
China_Province()
china_us()