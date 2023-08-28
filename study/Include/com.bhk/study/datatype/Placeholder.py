# 占位符学习Demo
# 公司名
company = "蜀国"
# 当前股价
stock_price = 5.41
# 股票代码
stock_code = 521
# 股票每日增长系数
stock_price_daily_growth_factor = 1.3
# 增长天数
gorwth_days = 7
print(f"公司：{company},股票代码：{stock_code},当前股价：{stock_price}")
print("每日增长系数：%f，经过%d的增长后，股价达到了:%4.2f" % (
stock_price_daily_growth_factor, gorwth_days, 5.41 ** stock_price_daily_growth_factor))