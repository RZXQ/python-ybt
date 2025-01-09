# 1042：练4.2  输出偶数  #thisFile
#
# 【题目描述】
# 按照由小到大的顺序，输出1∼n之间的所有偶数。
#
# 【输入】
# 输入一个整数 n，表示输出范围的上限。
#
# 【输出】
# 输出 1 到 n 之间所有的偶数，每两个偶数用空格隔开，结果在一行中。

# 读取用户输入，转换为整数 n
n = int(input())  # 用户输入，例如 10

# 初始化变量 i，从第一个偶数开始
i = 2  # 偶数序列从 2 开始

# 使用 while 循环生成偶数，并逐个输出
# 条件：当 i 小于或等于 n 时，继续循环
while i <= n:
    print(i, end=' ')  # 打印当前偶数，并在后面加一个空格而不是换行
    i = i + 2  # 每次将 i 增加 2，使其跳到下一个偶数

