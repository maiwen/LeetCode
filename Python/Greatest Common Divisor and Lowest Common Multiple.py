# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:54:43 2018

@author: Administrator

最大公约数算法
辗转相除法

有两整数a和b： 
① a%b得余数c 
② 若c=0，则b即为两数的最大公约数 
③ 若c≠0，则a=b，b=c，再回去执行①

最小公倍数为两数的乘积除以最大公约数。
"""
class Solution:
    
    def gcd(self, a, b):
        return b if a%b == 0 else self.gcd(b, a%b)
    
    def lcm(self, a, b):
        return a * b / self.gcd(a, b)
