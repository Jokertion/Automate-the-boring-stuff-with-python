# 循环迭代message字符串中每个字符，计算每个字符出现的次数
# 涉及的技能包：1.字典的get()和setdeafult()方法 2.漂亮打印pprint
import pprint

message = 'It was a bright cold day in May,andd the clocks were striking thirteen.'
count = {}
# 1 字典的setdefault()方法
for character in message:
    count.setdefault(character, 0)  # 查询此次计数前此字母出现的次数
    count[character] = count[character] + 1  # 更新次数（for每次遍历一个字母，故次数加一）

pprint.pprint(count)

count1 = {}
# 2 字典的get()方法
for character in message:
    count1[character] = count1.get(character, 0) + 1  # 查询出现次数，并加一

print(count1)
