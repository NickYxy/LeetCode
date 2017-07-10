'''
    461 Hamming Distance
    The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
    Given two integers x and y, calculate the Hamming distance.
    
    Input: x = 1, y = 4
    Output: 2
    Explanation:
    1   (0 0 0 1)
    4   (0 1 0 0)
           ?   ?
    The above arrows point to positions where the corresponding bits are different.
'''


# So,this is the easiest problem all through the leetcode columns.
# 1、如果用位异运算符，可以直接得到结果，但是速度不是很理想
class solution(object):
    def hammingdistance(self, x, y):
        return bin(x ^ y).count('1')


s = solution()
print(s.hammingdistance(1, 9))
print(bin(123))


# 2、通过补位让两个数的位数相等，然后两两比较同一个索引上的数字，不同的加1
class solution(object):
    def hammingdistance(self, x, y):
        bx = bin(x)
        by = bin(y)
        bx = bx[2:]
        by = by[2:]
        lx = len(bx)
        ly = len(by)
        l = 0
        count = 0
        if lx > ly:
            l = lx
            by = '0' * (l - ly) + by
        else:
            l = ly
            bx = '0' * (l - lx) + bx

        for i in range(l):
            if bx[i] != by[i]:
                count += 1
        return count


s1 = solution()
print(s1.hammingdistance(1, 9))
