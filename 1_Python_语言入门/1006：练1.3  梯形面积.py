# 1006：练1.3  梯形面积
#
# 【题目描述】
# 在梯形中阴影部分面积是150平方厘米，求梯形面积。
#
#
#
# 【输入】
# (无)
#
# 【输出】
# 输出梯形面积(保留两位小数)。
#
# 【输入样例】
# (无)
# 【输出样例】
# 400.00

# 先求出来, 梯形的高
# 三角形的面积是: 底边 * 高  / 2 = 三角形面积

height = 150 * 2 / 15  # 这个是一个整数

# (上底 + 下底) * 高 / 2
area = (15 + 25) * height / 2

# 保留两位小数
print("{:.2f}".format(area))
