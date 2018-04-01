class Solution:
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        if len(cpdomains) == 0:
            return []
        countDict = {}
        for cpdomain in cpdomains:
            count, url = tuple(cpdomain.split(' '))
            count = int(count)
            url = url.split('.')
            for i in range(1, len(url)+1):
                domain = '.'.join(url[-i: ])
                countDict[domain] = countDict.get(domain, 0) + count
        return ["%d %s" %(v, k) for k, v in countDict.items()]
