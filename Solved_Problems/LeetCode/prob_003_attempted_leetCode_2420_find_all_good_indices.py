class Solution:
    def is_prev_non_decreasing(self, nums: List[int], k: int, i: int) -> bool:
        # print(f'\nis_prev -> k = {k}  i = {i}')
        last_idx = i - k
        i -= 1
        is_okay = True
        # print(f'last_idx = {last_idx}  i = {i}')

        while i >= last_idx+1:
            i -= 1
            if nums[i] < nums[i+1]:
                # print(f'FAILED.... i = {i}  nums[i]={nums[i]}  nums[i+1]={nums[i+1]}')
                is_okay = False
                break
                
        return is_okay
        
        
    def is_next_non_decreasing(self, nums: List[int], k: int, i: int) -> bool:
        # print(f'\nis_next -> k = {k}  i = {i}')
        last_idx = i + k
        i += 1
        is_okay = True
        # print(f'last_idx = {last_idx}  i = {i}')

        while i <= last_idx-1:
            i += 1
            if nums[i] < nums[i-1]:
                # print(f'FAILED.... i = {i}  nums[i]={nums[i]}  nums[i-1]={nums[i-1]}')
                is_okay = False
                break
                
        return is_okay
    
    
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        i = k
        end_idx = length - k - 1
        result_list = []
        
        while i <= end_idx:
            prev_status = self.is_prev_non_decreasing(nums, k, i)
            next_status = self.is_next_non_decreasing(nums, k, i)
            
            if prev_status and next_status:
                result_list.append(i)
            i += 1
        
        return result_list