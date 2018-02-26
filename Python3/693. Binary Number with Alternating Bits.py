# class Solution:
#     def hasAlternatingBits(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         def is1010(n):
#             if n == 0:
#                 return True
#             elif not n%2:
#                 return is10101(n>>1)
#             else:
#                 return False
        
#         def is10101(n):
#             if n == 0 or n == 1:
#                 return True
#             elif n%2:
#                 return is1010(n>>1)
#             else:
#                 return False
        
#         if is1010(n) or is10101(n):
#             return True
#         else:
#             return False

# class Solution:
#     def hasAlternatingBits(self, n):
#         """
#         :type n: int
#         :rtype: bool
#         """
#         n_bit = bin(n)
#         return all([n_bit[i] != n_bit[i+1] for i in range(2, len(n_bit)-1)])

class Solution:
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = bin(n)
        return not '00' in n and not '11' in n
