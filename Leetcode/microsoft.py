'''
                     1
                   / | \
                  2  3  4
               /  | \   
              5   6  7
                 / | \
                8  9  10
    {1: [2, 3, 4], 2: [5, 6, 7], 6: [8, 9, 10]}              
'''

from collections import deque

class Employee:
    def __init__(self, id_):
        self.id = id_
        self.children = {}
    
    def getChildren(self):
        return self.children
    
    def addChildren(self, emp):
        self.children[emp.id] = emp


class Org:
    def reportsTo(self, empId, org):
        result = []
        if org.get(empId):
            for emp in org[empId]:
                self.traverse(emp, result, org)
        return result
    
    def traverse(self, emp_id, alist, org):
        q = deque()
        q.append(emp_id)
        while len(q) > 0:
            emp = q.popleft()
            if org.get(emp):
                for s in org[emp]:
                    q.append(s)
            alist.append(emp)


if __name__ == "__main__":
    org = {1: [2, 3, 4], 2: [5, 6, 7], 6: [8, 9, 10]}
    print(Org().reportsTo(2, org))


