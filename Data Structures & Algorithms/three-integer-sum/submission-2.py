class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = set()

        if n < 3:
            return []

        for i in range(2, n):
            target = -nums[i]
            seen = set()

            for j in range(i):
                find = target - nums[j]

                if find in seen:
                    ans.add(tuple(sorted((find, nums[j], nums[i]))))

                seen.add(nums[j])

        return [list(x) for x in ans]