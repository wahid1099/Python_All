class TwoSum:  
    def __init__(self, list1, target):  
        self.numbers = numbers  
        self.target = target  
          
    def solution(self):  
        length = len(numbers)  
          
        for i in range(length-1):  
            for j in range(i+1, length):  
                if numbers[i]+numbers[j] == self.target:  
                    new_list = i+1, j+1  
                    return list(new_list)  
        return -1  
  
numbers= [10,20,10,40,50,60,70]
target=50   
obj = TwoSum(numbers, target)  
print(obj.solution())  