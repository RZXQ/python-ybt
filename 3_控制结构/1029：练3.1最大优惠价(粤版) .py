# 1029：练3.1最大优惠价(粤版)
#
# 【题目描述】
# 三款笔记本的优惠价不同，请给出优惠价最大值。
#
# 【输入】
# 一行三个实数，分别表示三款笔记本的优惠价。
#
# 【输出】
# 输出一个实数，表示优惠价最大值。
#
# 【输入样例】
# 32.5 63.4 78

# 【输出样例】
# 78.0

# 读取用户输入，例如：用户输入 "32.5 63.4 78"
# 此时，shuru 是一个完整的字符串，例如 "32.5 63.4 78"
shuru = input()

# 使用 split(' ') 方法将字符串按照空格分割，转化为一个列表。
# 示例：输入字符串 "32.5 63.4 78" 会被分割成列表 ['32.5', '63.4', '78']
shuru = shuru.split(' ')

# 提取分割后的列表中的每个数字字符串，并将其转换为浮点数，方便数学运算
a = float(shuru[0])  # shuru[0] 是 '32.5'，转换后 a = 32.5
b = float(shuru[1])  # shuru[1] 是 '63.4'，转换后 b = 63.4
c = float(shuru[2])  # shuru[2] 是 '78'，转换后 c = 78.0

# 求最大值，新建一个变量，用于存储最大值的结果
zuida = 0  # 初始值设置为 0

# 比较 a, b, c，找到最大值，按照以下逻辑：
if a > b:
    if a > c:
        zuida = a  # 如果 a 大于 b 并且大于 c，则最大值是 a
    else:
        zuida = c  # 如果 a 大于 b，但小于等于 c，则最大值是 c
else:
    if b > c:
        zuida = b  # 如果 b 大于 a 且大于 c，则最大值是 b
    else:
        zuida = c  # 如果 b 大于 a，但小于等于 c，则最大值是 c

# 输出结果，也就是优惠价的最大值
print(zuida)
