class Solution:
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        charDict = dict(zip(string.ascii_letters[:26], range(26)))
        nums = [charDict[i] for i in letters]
        target = charDict[target]
        for num in sorted(nums):
            if num > target:
                return string.ascii_letters[num]
        return string.ascii_letters[nums[0]]
