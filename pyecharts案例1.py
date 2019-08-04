
# https://www.cnblogs.com/yuxuanlian/p/9794835.html

from pyecharts import Bar
bar=Bar('我的第一个图表','副标题')
bar.add("服装",["衬衫","羊毛衫","雪纺衫","裤子","高跟鞋","袜子"],[5,20,36,10,75,90])
bar.show_config()
bar.render('./文件/案例1_柱状图.html')



from pyecharts import WordCloud
name =['110', 'haihai', '鬼子', '豆腐', '旺旺', '南哥', '黑子', '两凡', '蒙多', '一哥', '小三', '末伏', '相大胖', '大路', '幺爸', '刘能', '刘瑞']
value =[10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360]
wordcloud =WordCloud(width=1300, height=620)
wordcloud.add("", name, value, word_size_range=[30, 100], shape='')
#词云图轮廓，有'circle', 'cardioid', 'diamond', 'triangle-forward', 'triangle', 'pentagon', 'star'可选
#意思：圆，心形，钻石，三角形，三角形，五角大楼，星星
wordcloud.show_config()
wordcloud.render('./文件/案例1_回忆.html')

# 山西地图示例
from pyecharts import Map
value = [20,190,253,77,65,40,70,80,20,180,800]
attr = ['运城市', '临汾市', '太原市', '大同市', '忻州市','长治市','晋中市','吕梁市','晋城市','阳泉市','朔州市']
map = Map("山西地图示例", width=1200,height=600)
map.add("", attr, value, maptype='山西',
                is_visualmap=True,
                visual_text_color='#000',is_label_show=True)
map.render('./文件/案例1_山西地图.html')


# 安徽省图例
from pyecharts import Map
city = ['合肥市', '芜湖市', '宿州市', '淮北市', '亳州市', '阜阳市', '蚌埠市', '淮南市', '滁州市', '六安市', '马鞍山市', '安庆市', '铜陵市', '宣城市', '池州市', "黄山市"]
area = [11445.1, 6026.05, 9938.77, 2741.39, 8521.23, 10118.17, 5950.72, 5532.30, 13515.99, 15450.82, 4049.13, 13537.96,
        2922.60, 12312.55, 8398.72, 9678.39]
# 绘制地图
map_1 = Map("安徽省图例－各地市面积", title_pos='center', width=1200, height=600)
# 地图详细信息
map_1.add("", city, area, maptype='安徽', is_visualmap=True, visual_range=[min(area), max(area)],
          visual_text_color='black', is_map_symbol_show=False, is_label_show=True)

# 输出到当前文件夹下，保存名为 安徽省地图，文件类型为html
map_1.render("./文件/案例1_安徽省地图.html")
