"""
    画图
"""
list01 = ["湖北", "河南", "北京"]
list01[0] = ["武汉", "孝感"]
list01[-2:-1] = ["信阳", "郑州", "南阳"]
print(list01)

list02 = ["温州", ["杭州", "宁波"], "台州"]
list03 = list02[:]
list02[1][1] = "嘉兴"
print(list03)