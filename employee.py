class employee:
    def __init__(self, eid, name, salary):
        self.eid = eid
        self.empName = name
        self.salary = salary
    
    '''def descripe(self):
        return f"emp Name: {self.empName} is {self.category} cost {self.price} Omani Riyals"
        
    def discount(self, amount):
        self.price = self.price - self.price * (amount/100)
        if self.category == 'Electronics':
            self.price += 10'''
    def getid(self):
        return self.eid
    def getname(self):
        return self.empName
    
    def getsalary(self):
        return self.salary