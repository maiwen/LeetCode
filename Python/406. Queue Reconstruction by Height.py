# -*- coding: utf-8 -*-
"""
Created on 2018/7/4 12:58

@author: vincent

Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
"""
class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key=lambda x: x[1])
        people.sort(key= lambda x: x[0])
        for i in range(len(people)-1,-1,-1):
            step = people[i][1]
            for j in range(i):
                if people[j][0] >= people[i][0]:
                    step -= 1
            if (i+step) <= len(people)-1:
                temp = people.pop(i)
                people.insert(i+step,temp)
        return people

class Solution1:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x: (-x[0], x[1]))
        queue = []
        for p in people:
            queue.insert(p[1], p)
        return queue

s = Solution()
print(s.reconstructQueue([[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]))