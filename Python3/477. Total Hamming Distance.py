class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        # ans = 0 # 超时
        # dict1 = collections.defaultdict(int)
        # dict2 = collections.defaultdict(int)
        # for i in A:
        #     for j in B:
        #         dict1[i+j] += 1
        # for i in C:
        #     for j in D:
        #         dict2[-i-j] += 1
        # key1 = sorted(dict1.keys())
        # key2 = sorted(dict2.keys())
        # i = j = 0
        # while i < len(key1) and j < len(key2):
        #     if key1[i] == key2[j]:
        #         ans += dict1[key1[i]] * dict2[key2[j]]
        #         i += 1
        #         j += 1
        #     elif key1[i] < key2[j]:
        #         i += 1
        #     else:
        #         j += 1
        # return ans
        
        # counter = collections.Counter([i+j for i in A for j in B]) # 1156ms    
        # return sum([counter[-i-j] for i in C for j in D])

        hashtable = {} # 300ms 最基本的方法最快
        for a in A:
            for b in B :
                if a + b in hashtable :
                    hashtable[a+b] += 1
                else :
                    hashtable[a+b] = 1
        count = 0         
        for c in C :
            for d in D :
                if -c - d in hashtable :
                    count += hashtable[-c-d]
        return count
