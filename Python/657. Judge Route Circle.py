# -*- coding: utf-8 -*-
"""
Created on 2018/7/10 17:06

@author: vincent
Initially, there is a Robot at position (0, 0). Given a sequence of its moves, judge if this robot makes a circle, which means it moves back to the original place.

The move sequence is represented by a string. And each move is represent by a character. The valid robot moves are R (Right), L (Left), U (Up) and D (down). The output should be true or false representing whether the robot makes a circle.

Example 1:
Input: "UD"
Output: true
Example 2:
Input: "LL"
Output: false

"""
class Solution:
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        x, y = 0, 0
        for item in moves:
            if item == 'R':
                x += 1
            elif item == 'L':
                x -= 1
            elif item == 'U':
                y += 1
            elif item == 'D':
                y -= 1
            else:
                print('no valid input')
                return False
        if x == 0 and y == 0:
            return True
        else:
            return False

    def judgeCircle1(self, moves):
        """
        :type moves: str
        :rtype: bool
        """

        if moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R'):
            return True
        else:
            return False