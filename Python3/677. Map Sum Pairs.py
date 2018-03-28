class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.Map = collections.defaultdict(int)
        

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        self.Map[key] = val
        

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        return sum([v for k, v in self.Map.items() if k.startswith(prefix)])
                
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
