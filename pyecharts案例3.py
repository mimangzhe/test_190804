# https://www.cnblogs.com/lizm166/p/9449261.html


# #示例2：EffectScatter（带有涟漪特效动画的散点图）
# from pyecharts import EffectScatter
# v1 =[10, 20, 30, 40, 50, 60]
# v2 =[25, 20, 15, 10, 60, 33]
# es =EffectScatter("动态散点图示例")
# es.add("effectScatter", v1, v2)
# es.render('./文件/案例3_动态散点图1.html')
# es =EffectScatter("动态散点图各种图形示例")
# es.add("", [10], [10], symbol_size=20, effect_scale=3.5, effect_period=3, symbol="pin")
# es.add("", [20], [20], symbol_size=12, effect_scale=4.5, effect_period=4,symbol="rect")
# es.add("", [30], [30], symbol_size=30, effect_scale=5.5, effect_period=5,symbol="roundRect")
# es.add("", [40], [40], symbol_size=10, effect_scale=6.5, effect_brushtype='fill',symbol="diamond")
# es.add("", [50], [50], symbol_size=16, effect_scale=5.5, effect_period=3,symbol="arrow")
# es.add("", [60], [60], symbol_size=6, effect_scale=2.5, effect_period=3,symbol="triangle")
# es.render('./文件/案例3_动态散点图2.html')
#
#
# #示例四：Funnel（漏斗图）
# from pyecharts import Funnel
# attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# value =[20, 40, 60, 80, 100, 120]
# funnel =Funnel("漏斗图示例")
# funnel.add("商品", attr, value, is_label_show=True, label_pos="inside", label_text_color="#fff")
# funnel.render('./文件/案例3_漏斗图.html')
#
# #示例五： Gauge（仪表盘）
# from pyecharts import Gauge
# gauge =Gauge("仪表盘示例")
# gauge.add("业务指标", "完成率", 66.66)
# gauge.show_config()
# gauge.render('./文件/案例3_仪表盘.html')
#
# #示例5： Geo（地理坐标系）
# #5.1
# from pyecharts import Geo
# data=[("海门",9),("鄂尔多斯",12),("招远",12),("舟山",12),("齐齐哈尔",14),("盐城",15),("赤峰",16),("青岛",18),("乳山",18),("金昌",19),("泉州",21),("莱西",21), ("日照",21),("胶南",22),("南通",23),("拉萨",24),("云浮",24),("梅州",25)]
# geo=Geo("全国主要城市空气质量","data from pm2.5",title_color="#fff",title_pos="center",width=1200,height=600,background_color='#404a59')
# attr,value=geo.cast(data)
# geo.add("",attr,value,visual_range=[0,200],visual_text_color="#fff",symbol_size=15,is_visualmap=True)
# geo.show_config()
# geo.render('./文件/案例3_地理坐标系1.html')
#
# #6.2
# from pyecharts import Geo
# data =[("海门", 9), ("鄂尔多斯", 12), ("招远", 12), ("舟山", 12), ("齐齐哈尔", 14), ("盐城", 15)]
# geo =Geo("全国主要城市空气质量", "data from pm2.5", title_color="#fff", title_pos="center", width=1200, height=600, background_color='#404a59')
# attr, value =geo.cast(data)
# geo.add("", attr, value, type="effectScatter", is_random=True, effect_scale=5)
# geo.show_config()
# geo.render('./文件/案例3_地理坐标系2.html')
#
#
# #示例6：Graph（关系图）
# #6.1
# # from pyecharts import Graph
# # nodes =[{"name": "结点1", "symbolSize": 10}, {"name": "结点2", "symbolSize": 20}, {"name": "结点3", "symbolSize": 30}, {"name": "结点4", "symbolSize": 40}, {"name": "结点5", "symbolSize": 50}, {"name": "结点6", "symbolSize": 40}, {"name": "结点7", "symbolSize": 30}, {"name": "结点8", "symbolSize": 20}]
# # links =[]
# # for i in nodes:
# #     for j in nodes:
# #         links.append({"source": i.get('name'), "target": j.get('name')})
# #         graph =Graph("关系图-环形布局示例")
# #         graph.add("", nodes, links, is_label_show=True, repulsion=8000, layout='circular', label_text_color=None)
# #         graph.show_config()
# #         graph.render('./文件/案例3_关系图.html')
#
# #7.2折线
# from pyecharts import Line
# attr =["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
# v1 =[5, 20, 36, 10, 10, 100]
# v2 =[55, 60, 16, 20, 15, 80]
# line =Line("折线图-阶梯图示例")
# line.add("商家A", attr, v1, is_step=True, is_label_show=True)
# line.show_config()
# line.render('./文件/案例3_折线.html')

# #12.1
# from pyecharts import Polar
# radius =['周一', '周二', '周三', '周四', '周五', '周六', '周日']
# polar =Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
# polar.add("A", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("B", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barRadius', is_stack=True)
# polar.add("C", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barRadius', is_stack=True)
# polar.show_config()
# polar.render('./文件/案例3_极坐标系1.html')
#
# #12.2
# from pyecharts import Polar
# radius =['周一', '周二', '周三', '周四', '周五', '周六', '周日']
# polar =Polar("极坐标系-堆叠柱状图示例", width=1200, height=600)
# polar.add("", [1, 2, 3, 4, 3, 5, 1], radius_data=radius, type='barAngle', is_stack=True)
# polar.add("", [2, 4, 6, 1, 2, 3, 1], radius_data=radius, type='barAngle', is_stack=True)
# polar.add("", [1, 2, 3, 4, 1, 2, 5], radius_data=radius, type='barAngle', is_stack=True)
# polar.show_config()
# polar.render('./文件/案例3_极坐标系2.html')


#13.1雷达图
from pyecharts import Radar
schema =[ ("销售", 6500), ("管理", 16000), ("信息技术", 30000), ("客服", 38000), ("研发", 52000), ("市场", 25000)]
v1 =[[4300, 10000, 28000, 35000, 50000, 19000]]
v2 =[[5000, 14000, 28000, 31000, 42000, 21000]]
radar =Radar()
radar.config(schema)
radar.add("预算分配", v1, is_splitline=True, is_axisline_show=True)
radar.add("实际开销", v2, label_color=["#4e79a7"], is_area_show=False)
radar.show_config()
radar.render('./文件/案例3_雷达图1.html')

#13.2
from pyecharts import Radar
value_bj =[[55, 9, 56, 0.46, 18, 6, 1], [25, 11, 21, 0.65, 34, 9, 2], [56, 7, 63, 0.3, 14, 5, 3], [33, 7, 29, 0.33, 16, 6, 4]]
value_sh =[[91, 45, 125, 0.82, 34, 23, 1], [65, 27, 78, 0.86, 45, 29, 2], [83, 60, 84, 1.09, 73, 27, 3], [109, 81, 121, 1.28, 68, 51, 4]]
c_schema=[{"name": "AQI", "max": 300, "min": 5}, {"name": "PM2.5", "max": 250, "min": 20}, {"name": "PM10", "max": 300, "min": 5}, {"name": "CO", "max": 5}, {"name": "NO2", "max": 200}, {"name": "SO2", "max": 100}]
radar =Radar()
radar.config(c_schema=c_schema, shape='circle')
radar.add("北京", value_bj, item_color="#f9713c", symbol=None)
radar.add("上海", value_sh, item_color="#b3e4a1", symbol=None)
radar.show_config()
radar.render('./文件/案例3_雷达图2.html')