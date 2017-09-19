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

# def isAnagram2(s, t):
#     dic1, dic2 = [0] * 26, [0] * 26
#     for item in s:
#         dic1[ord(item) - ord('a')] += 1
#     for item in t:
#         dic2[ord(item) - ord('a')] += 1
#     return dic1
#
# s1 = 'avdadesa'
# t1 = 'adaefeafefae'
#
# print(isAnagram2(s1,t1))
from collections import Counter

l1 = [1, 2, 2, 1]
l2 = [2, 2]

s1 = Counter(l1)
s2 = Counter(l2)

print(s1)
print(s2)
print(s1 & s2)

for k, v in enumerate(l1):
    print(k, v)


class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

    def insert(self, newData):
        if newData == self.data:
            return False
        elif newData < self.data:
            if self.leftchild == None:
                self.leftchild = Node(newData)
            else:
                self.leftchild.insert(newData)
        elif newData > self.data:
            if self.rightchild == None:
                self.rightchild = Node(newData)
            else:
                self.rightchild.insert(newData)

    def findOne(self, num):
        if num == self.data:
            return True
        elif num < self.data:
            if self.leftchild == None:
                return False
            else:
                return elf.leftchild.findOne(num)
        else:
            if self.rightchild == None:
                return False
            else:
                return self.rightchild.findOne(num)

    # preOrder: <ROOT><Left><Right>
    def preOrder(self):
        print(self.data)
        if self.leftchild:
            self.leftchild.preOrder()
        if self.rightchild:
            self.rightchild.preOrder()

    # midOrder: <Left><Root><Right>
    def midOrder(self):
        if self.leftchild:
            self.leftchild.preOrder()
        print(self.data)
        if self.rightchild:
            self.rightchild.preOrder()

    # backOrder: <Left><Root><Right>
    def backOrder(self):
        if self.rightchild:
            self.rightchild.preOrder()
        print(self.data)
        if self.leftchild:
            self.leftchild.preOrder()


if __name__ == '__main__':
    treeNode = Node(5)
