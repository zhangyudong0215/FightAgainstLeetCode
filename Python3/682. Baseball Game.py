class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        ans = []
        for item in ops:
            if item == "+":
                ans.append(ans[-2]+ans[-1])
            elif item == "D":
                ans.append(2*ans[-1])
            elif item == "C":
                ans.pop()
            else:
                ans.append(int(item))
        return sum(ans)              
