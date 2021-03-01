import re
text ="xinm:48545,sum:4445645"
# result = re.findall("(\w+):(\d+)",text)
# print(result)
# res = re.split("\W",text)
# print(res)
# res = re.sub("\W+","",text)
# print(res)

# res = re.match("\w+:\d+",text)
# print(res)
# print(res.span())
# print(res.group())

# result = re.search("(\w+):(?P<name>\d+)",text)
# print(result)
# print(result.group(2))
# print(result.span(2))
#
#
# a = [lambda item:item/2]
# -*- coding:utf-8 -*-
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        #list01 = s.split(" ")
        #print(list01)
        str01 = "%20".join(s)
        print(str01)
res = Solution()
res.replaceSpace("hello world ")