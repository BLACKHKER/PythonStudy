"""
@Author  ：BLACKHKER
@Date    ：2023/8/28 15:37
@File    ：LineChart.py
@Description: Pyecharts折线图代码
@Version 1.0
"""
from pyecharts.charts import Line
from pyecharts.options import TitleOpts, LegendOpts, ToolboxOpts

# 创建一个折线图对象
line = Line()
# 给折线图添加X轴数据
line.add_xaxis(["中国", "美国", "英国"])
# 给折线图添加Y轴数据
line.add_yaxis("GDP", [30, 20, 10])

line.set_global_opts(
    # 标题配置,居中,距离底部只有%1的距离
    title_opts=TitleOpts(title="GDP展示", pos_left="center", pos_bottom="1%"),
    # 图例配置
    legend_opts=LegendOpts(is_show=True),
    # 工具箱配置
    toolbox_opts=ToolboxOpts(is_show=True),
)

# 通过render()方法，将代码生成为图像
line.render()
