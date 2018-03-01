"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
#         def getImpAndSub(employees, id, ids): # 重复多次的查询会不会导致低效率？（276ms）
#             for employee in employees:
#                 if employee.id == id:
#                     count = employee.importance
#                     ids.extend(employee.subordinates)
#             return count, ids

#         ids = [id]
#         total = 0
#         while ids:
#             id = ids.pop()
#             count, ids = getImpAndSub(employees, id, ids)
#             total += count
#         return total
        
        hashtable = {} # hashtable快了一点(216ms)
        for employee in employees:
            hashtable[employee.id] = [employee.importance, employee.subordinates]
        
        ids = [id]
        total = 0
        while ids:
            id = ids.pop()
            total += hashtable[id][0]
            ids.extend(hashtable[id][1])
        return total
