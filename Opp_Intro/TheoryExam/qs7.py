class phitron:
    def subset(self, set):
        return self.subsetsrecursion([], sorted(set))
    
    def subsetsrecursion(self, current, set):
        if set:
            return self.subsetsrecursion(current, set[1:]) + self.subsetsrecursion(current + [set[0]], set[1:])
        return [current]

Input= [4, 5, 6] 
output=phitron().subset(Input)

print("OutPut is :",output)
