class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
#         ans = []
#         for num in range(1, n+1):
#             if not num%3 and not num%5:
#                 ans.append("FizzBuzz")
#             elif not num%3:
#                 ans.append("Fizz")
#             elif not num%5:
#                 ans.append("Buzz")
#             else:
#                 ans.append(str(num))
                
#         return ans
        return [str(i) if (i%3!=0 and i%5!=0) else (('Fizz'*(i%3==0)) + ('Buzz'*(i%5==0))) for i in range(1, n+1)]