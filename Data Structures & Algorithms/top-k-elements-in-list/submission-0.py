class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        # Count frequency
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        ans = []

        # Find top k elements
        for _ in range(k):
            maxi = -1
            num = 0

            for key in freq:
                if freq[key] > maxi:
                    maxi = freq[key]
                    num = key

            ans.append(num)
            freq[num] = -1      # Mark as used

        return ans