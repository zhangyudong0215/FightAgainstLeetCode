class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        indexsumDict = {} # 128ms
        common = list(set(list1) & set(list2)) 
        for name in common:
            count = list1.index(name) + list2.index(name)
            if count not in indexsumDict:
                indexsumDict[count] = [name]
            else:
                indexsumDict[count].append(name)
        return indexsumDict[min(indexsumDict.keys())]
