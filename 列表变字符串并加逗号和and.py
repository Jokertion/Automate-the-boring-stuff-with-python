'''
    假定有下面这样的列表：spam=['apples','bananas','tofu',' cats']
    编写一个函数，它以一个列表值作为参数，返回一个字符串。
    该字符串包含所有表项，表项之间以逗号和空格分隔，并在最后一个表项之前插入 and 。

    例如，将前面的spam列表传递给函数，将返回'apples,bananas,tofu,and cats'。

    你的函数应该能够传递给它的任何列表。
'''


# 方法一： join加逗号， format 拼接

def comma1(items):
    # 若列表项唯一，则取出此值输出（必须先取值再输出，不然输出的是列表）
    if len(items) == 1:
        print(items[0])
    else:
        # 创建新列表xx，确保列表每项都是字符串，可被连接
        xx = []
        for i in items:
            xx.append(str(i))
        a = ', '.join(xx[:-1])
        b = xx[-1]
        print('{}, and {}'.format(a, b))


#spam = ['apples','bananas','tofu',' cats']
spam = ['apples', 1, 2, 3, 4, 5]
comma1(spam)


# 方法二：print关键字参数end加逗号，print（and + 最后一项拼接）
def comma2(items):
    if len(items) == 1:
        print(str(items[0]))
    else:
        for i in range(len(items) - 1):
            print(str(items[i]),
                  end=", ")
        print('and ' + str(items[-1]))


spam = ['apples', 1, 2, 3, 4, 5]
comma2(spam)
