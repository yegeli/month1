"""
    行
"""
# 3个物理行对应3个逻辑行(建议)
a = 10
b = 20
c = a + b

# 1个物理行对应3个逻辑行(不建议)
a = 10;b = 20;c = a + b

# 3个物理行对应1个逻辑行
# \ 换行符
a = 1 + 2 + \
    3 + 4 + \
    5 + 6

# 括号 是天然的换行符
b = (1 + 2 +
     3 + 4 +
     5 + 6)