class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # length = len(people) # 132ms
        # ans = [[] for i in range(length)]
        # index = list(range(length))
        # personDict = {}
        # for person in people:
        #     if person[0] in personDict:
        #         personDict[person[0]].append(person[1])
        #     else:
        #         personDict[person[0]] = [person[1]]
        # for key in sorted(personDict.keys()):
        #     trashs = []
        #     for value in personDict[key]:
        #         ans[index[value]] = [key, value]
        #         trashs.append(index[value])
        #     for trash in trashs:
        #         index.remove(trash)
        # return ans
        
        # ans = [] # 104ms
        # personDict = {}
        # for person in people:
        #     if person[0] in personDict:
        #         personDict[person[0]].append(person[1])
        #     else:
        #         personDict[person[0]] = [person[1]]
        # for key in sorted(personDict.keys(), reverse=True):
        #     for value in sorted(personDict[key]):
        #         ans.insert(value, [key, value])
        # return ans
        
        ans = [] # 92ms
        people.sort(key=lambda x: (-x[0], x[1]))
        for person in people:
            ans.insert(person[1], person)
        return ans
