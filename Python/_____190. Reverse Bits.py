# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 22:22:13 2018

@author: Administrator

Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation: 43261596 represented in binary as 00000010100101000001111010011100, 
             return 964176192 represented in binary as 00111001011110000010100101000000.
Follow up:
If this function is called many times, how would you optimize it?




Let's work on an example. Say, n = 19, which is 00000000000000000000000000010011 in binary, so in the output we should get 11001000000000000000000000000000 in binary, which is 3355443200.
We initialize answer to 0, so in binary it's 32 zeroes. We loop over 32 times, since every integer is gonna have 32 possible 0/1.
1st line in the loop: n & 1, we check if last bit of n is set, is it 1 or 0, ans << 1 we shift all bits that we already have in our answer to the left, so after this shifting the bit on the right is 0, + by using + we set the last bit in the answer to the value that we got in n & 1.
2nd line in the loop we shift bits of our initial number n to the right, since we've already checked the last bit of n, so we just move on to the next bit.

So, in our example, I'm gonna show only first 5 right bits, since other bits are 0.
answer = 0, in binary: 00000000000000000000000000000000
answer << 1 is 00000000000000000000000000000000, n & 1 is 00000000000000000000000000000001
after + operation answer is 00000000000000000000000000000001

answer = 1, in binary: 00000000000000000000000000000001
answer << 1 is 00000000000000000000000000000010, n & 1 is 00000000000000000000000000000001
after + operation answer is 00000000000000000000000000000011

answer = 3, in binary: 00000000000000000000000000000011
answer << 1 is 00000000000000000000000000000110, n & 1 is 00000000000000000000000000000000
after + operation answer is 00000000000000000000000000000110

answer = 6, in binary: 00000000000000000000000000000110
answer << 1 is 00000000000000000000000000001100, n & 1 is 00000000000000000000000000000000
after + operation answer is 00000000000000000000000000001100

answer = 12, in binary: 00000000000000000000000000001100
answer << 1 is 00000000000000000000000000011000, n & 1 is 00000000000000000000000000000001
after + operation answer is 00000000000000000000000000011001

And after that in our example, we'll just shift ** 00000000000000000000000000011001 all the way to the left, which is gonna lead to 11001000000000000000000000000000.
"""

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans