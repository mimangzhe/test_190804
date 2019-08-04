# https://www.cnblogs.com/aby321/p/9252609.html
#
# 柱形图
import random
from pyecharts import Bar
bar = Bar("我的第一个图表", "这里是vintage")
# bar.use_theme('vintage')
X_AXIS=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar.add("商家A", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家B", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家C", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家D", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.render('./文件/案例2_柱形图vintage.html')

bar = Bar("我的第一个图表", "这里是macarons")
# bar.use_theme('macarons')
X_AXIS=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar.add("商家A", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家B", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家C", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家D", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.render('./文件/案例2_柱形图macarons.html')

bar = Bar("我的第一个图表", "这里是infographic")
# bar.use_theme('infographic')
X_AXIS=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar.add("商家A", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家B", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家C", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家D", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.render('./文件/案例2_柱形图infographic.html')

bar = Bar("我的第一个图表", "这里是shine")
# bar.use_theme('shine')
X_AXIS=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar.add("商家A", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家B", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家C", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家D", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.render('./文件/案例2_柱形图shine.html')

bar = Bar("我的第一个图表", "这里是roma")
# bar.use_theme('roma')
X_AXIS=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar.add("商家A", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家B", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家C", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家D", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.render('./文件/案例2_柱形图roma.html')

bar = Bar("我的第一个图表", "这里是dark")
# bar.use_theme('dark')
X_AXIS=["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
bar.add("商家A", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家B", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家C", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.add("商家D", X_AXIS, [random.randint(10, 100) for _ in range(6)])
bar.render('./文件/案例2_柱形图dark.html')



# 饼图Pie
from pyecharts import Pie
attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [11, 12, 13, 10, 10, 10]
pie = Pie("饼图示例")#新建饼图示例pie

pie.add("", attr, v1, is_label_show=True)
pie.show_config()#是否在命令行中显示config，此行可省略
pie.render("./文件/案例2_普通饼图示例.html")


# 玫瑰饼图
from pyecharts import Pie
attr=['衬衣','羊毛衫','雪纺衫','裤子','高跟鞋','袜子']
v1=[5,9,22,6,9,30]
v2=[5,9,22,6,9,30]
pie=Pie('饼图-玫瑰图示例',title_pos='right',width=1200,height=700)
#pie.use_theme('vintage')
# add()
# center为调整饼图圆心坐标
# is_random为是否随即排列颜色列表（bool）
# radius为半径，第一个为内半径，第二个是外半径
# rosetype为是否展示成南丁格尔图:'radius' 圆心角展现数据半分比，半径展现数据大小;'area'圆心角相同，为通过半径展现数据大小(默认）
# label_text_size为调整标签字体大小
pie.add('商品A',attr,v1,center=[25,50],is_random=True,radius=[10,45],rosetype='radius',is_lable_show=True)
pie.add('商品B',attr,v2,center=[75,50],is_random=False,radius=[30,70],is_legend_show=True,is_lable_show=True)
pie.render('./文件/案例2_饼图-玫瑰图示例.html')