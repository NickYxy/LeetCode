__author__ = 'nickyuan'
'''
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.
Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
'''


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = [x + 1 for x in range(n)]
        for i in range(len(l)):
            if l[i] % 3 == 0 and l[i] % 5 != 0:
                l[i] = "Fizz"
            elif l[i] % 5 == 0 and l[i] % 3 != 0:
                l[i] = "Buzz"
            elif l[i] % 5 == 0 and l[i] % 3 == 0:
                l[i] = "FizzBuzz"
            else:
                l[i] = str(l[i])
        return l

    def fizzBuzz1(self, n):
        return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n + 1)]

    def fizzBuzz2(self, n):
        return ['Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or str(i) for i in range(1, n + 1)]


s = Solution()
print(s.fizzBuzz2(15))