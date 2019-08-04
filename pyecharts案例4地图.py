
from pyecharts import Map
# 世界地图数据
value = [95.1, 23.2, 43.3, 66.4, 88.5]
attr= ["China", "Canada", "Brazil", "Russia", "United States"]

# 省和直辖市
province_distribution = {'河南': 45.23, '北京': 37.56, '河北': 21, '辽宁': 12, '江西': 6, '上海': 20, '安徽': 10, '江苏': 16, '湖南': 9, '浙江': 13, '海南': 2, '广东': 22, '湖北': 8, '黑龙江': 11, '澳门': 1, '陕西': 11, '四川': 7, '内蒙古': 3, '重庆': 3, '云南': 6, '贵州': 2, '吉林': 3, '山西': 12, '山东': 11, '福建': 4, '青海': 1, '舵主科技，质量保证': 1, '天津': 1, '其他': 1}
provice=list(province_distribution.keys())
values=list(province_distribution.values())

# 城市 -- 指定省的城市 xx市
city = ['郑州市', '安阳市', '洛阳市', '濮阳市', '南阳市', '开封市', '商丘市', '信阳市', '新乡市']
values2 = [1.07, 3.85, 6.38, 8.21, 2.53, 4.37, 9.38, 4.29, 6.1]

# 区县 -- 具体城市内的区县  xx县
quxian = ['夏邑县', '民权县', '梁园区', '睢阳区', '柘城县', '宁陵县']
values3 = [3, 5, 7, 8, 2, 4]

# 世界地图：
map0 = Map("世界地图示例", width=1200, height=600)
map0.add("世界地图", attr, value, maptype="world",  is_visualmap=True, visual_text_color='#000')
map0.render(path="./文件/案例4_世界地图.html")

# maptype='china' 只显示全国直辖市和省级
# 数据只能是省名和直辖市的名称
map = Map("中国地图",'中国地图', width=1200, height=600)
map.add("", provice, values, visual_range=[0, 50],  maptype='china', is_visualmap=True,
    visual_text_color='#000')
map.show_config()
map.render(path="./文件/案例4_中国地图.html")

# 河南地图  数据必须是省内放入城市名
map2 = Map("河南地图",'河南', width=1200, height=600)
map2.add('河南', city, values2, visual_range=[1, 10], maptype='河南', is_visualmap=True, visual_text_color='#000')
map2.show_config()
map2.render(path="./文件/案例4_河南地图.html")

# # 商丘地图 数据为商丘市下的区县
map3 = Map("高陵县地图",'商丘', width=1200, height=600)
map3.add("高陵", quxian, values3, visual_range=[1, 10], maptype='高陵县', is_visualmap=True,
    visual_text_color='#000')
map3.render(path="./文件/案例4_高陵县地图.html")