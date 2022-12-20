class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        
        counter = 0
        for i in range(len(nums)):
            if nums[i] == val:
                temp = nums[i]
                nums[i] = nums[- i - counter]
                nums[- i - counter] = temp
                counter = counter + 1
                i = i - 1
          

        print(nums)

solution = Solution()

solution.removeElement([1,2,3,4,3,2], 3)