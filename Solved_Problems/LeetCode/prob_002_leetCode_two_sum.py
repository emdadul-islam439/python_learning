class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        isExist = dict()
        for idx, item in enumerate(nums):
            mList = list()
            if item in isExist:
                mList = isExist[item]
            mList.append(idx)
            isExist[item] = mList
        for item in nums:
            if item + item == target:
                if (item in isExist) and (len(isExist[item]) >= 2):
                    return [isExist[item][0], isExist[item][1]]
            else:
                dif = target - item
                if dif in isExist:
                    return [isExist[item][0], isExist[dif][0]]