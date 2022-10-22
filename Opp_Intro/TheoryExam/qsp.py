class phitron:
    def __init__(self,X,n):
        self.X = X
        self.n = n


    def sum(self):
        # summ=self.X+self.n
        return self.X+self.n
       
    
    def pow(self):
        return pow(self.X,self.n)
       


demo=phitron(2,3)
print("Exponential is:",demo.pow())
print("Sum is:",demo.sum())
