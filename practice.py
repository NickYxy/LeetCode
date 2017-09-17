# __author__ = 'nickyuan'
# d = dict()
# nums = [1,2,3,4,5,4,5,6]
#
# for num in nums:
#     d[num] = d.get(num,0) + 1
#
# print(d)
#
# l = [1,2,3,4]
# print(l[1:])
# print(l[:1])
#
# s1 = "z"
#
#
# s2 = "loveleetcode"

# from collections import Counter
# print(Counter(s1))
# print(len(Counter(s1)))
#
# def unique(s):
#     s3 = []
#     for k, v in Counter(s).items():
#         if v == 1:
#             s3.append(k)
#
#     for i in range(len(s)):
#         if s[i] in s3:
#             return i
# print(unique(s1))
#
# print(s2.index('e'))

# s3 = ""
# s4 = []
# print(s3 is None)
# print(s4 is None)

def isAnagram2(s, t):
    dic1, dic2 = [0] * 26, [0] * 26
    for item in s:
        dic1[ord(item) - ord('a')] += 1
    for item in t:
        dic2[ord(item) - ord('a')] += 1
    return dic1

s1 = 'avdadesa'
t1 = 'adaefeafefae'

print(isAnagram2(s1,t1))