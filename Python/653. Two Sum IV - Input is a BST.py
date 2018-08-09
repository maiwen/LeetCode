# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 17:19:23 2018

@author: Administrator

Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""
class Solution:
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def inorder(root, nums):
            if not root:
                return None
            inorder(root.left, nums)
            nums.append(root.val)
            inorder(root.right, nums)
            
        nums = []
        inorder(root, nums)
        i, j = 0, len(nums)-1
        while(i < j):
            if nums[i] + nums[j] == k:
                return True
            elif nums[i] + nums[j] < k:
                i += 1
            else:
                j -= 1
        return False
