class phitron:
   def findpair(self, nums, target_num):      
     
       result_dict = dict()
       pos = 0
       while pos < len(nums):
           if (target_num - nums[pos]) not in result_dict:
               result_dict[nums[pos]] = pos
               pos += 1
           else:
               return [result_dict[target_num - nums[pos]], pos]
