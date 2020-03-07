"""
    复习
    函数
        可变与不可变的传参结论：
            1.传入可变对象  2.修改可变对象  3. 可以不用return
            def 排序(列表):
                修改列表对象（ 列表[?] = ? ）
                不用通过return返回结果
        作用域
            局部变量：小(一个函数使用的信息)
            全局变量：大(多个函数使用的信息)

        实际参数：按照何种方式与形参对应
            位置实参：按照顺序
                序列实参：使用容器包装信息,[拆]分后按顺序对应
            关键字实参：按照名称
                字典实参：使用容器包装信息,[拆]分后按名称对应
"""
list01 = [4, 5, 6, 67, 7]
# list01.reverse()
list01.sort()
print(list01)


def func01(p1=0, p2=0, p3=0):
    print(p1)
    print(p2)
    print(p3)

func01(1, 2, 3)
func01(*"abc")
func01(p2=2)
func01(**{"p2": 22, "p1": 11})