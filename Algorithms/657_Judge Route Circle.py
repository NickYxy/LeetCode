__author__ = 'nickyuan'
'''
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false
'''

'''
只需要保证往右移的次数和往左移的次数一样，往上移和往下移的次数一样即可
'''
class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        s1 = 'rl'
        s2 = 'ud'
        if moves == '':
            return True
        if moves.count('R') == moves.count('L') and moves.count('U') == moves.count('D'):
            return True
        else:
            return False


'''当然这里有一行代码的版本'''
def judgeCircle(self, moves):
    return moves.count('L') == moves.count('R') and moves.count('U') == moves.count('D')