class Solution:
    def exclusiveTime(self, n, logs):
        """
        :type n: int
        :type logs: List[str]
        :rtype: List[int]
        """
        ans = [0 for _ in range(n)]
        stack = []
        for log in logs:
            uid, status, time = map(int, log.replace('start', '1').replace('end', '0').split(":"))
            if status:
                stack.append([time, 0])
            else:
                starttime, timecost = stack.pop()
                ans[uid] += time - starttime + 1 - timecost
                if stack:
                    stack[-1][1] += time - starttime + 1
        return ans
