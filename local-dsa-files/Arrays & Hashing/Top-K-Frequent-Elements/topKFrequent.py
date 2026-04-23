class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]  # buckets 0..n

        for num in nums:                            # step 1: count
            count[num] = 1 + count.get(num, 0)

        for num, cnt in count.items():              # step 2: drop into buckets
            freq[cnt].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):      # step 3: walk backwards
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

        # --- Alternative: Sorting — O(n log n) ---
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # arr = [[cnt, num] for num, cnt in count.items()]
        # arr.sort()
        # res = []
        # while len(res) < k:
        #     res.append(arr.pop()[1])
        # return res

        # --- Alternative: Min-Heap — O(n log k) ---
        # import heapq
        # count = {}
        # for num in nums:
        #     count[num] = 1 + count.get(num, 0)
        # heap = []
        # for num in count.keys():
        #     heapq.heappush(heap, (count[num], num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [heapq.heappop(heap)[1] for _ in range(k)]


if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([1, 1, 1, 2, 2, 3],       2, [1, 2]),
        ([7, 7],                    1, [7]),
        ([1, 2, 3, 1, 2, 1],       1, [1]),
        ([4, 4, 4, 5, 5, 6, 6, 6], 2, [4, 6]),
        ([1],                       1, [1]),
    ]

    print("Top K Frequent Elements")
    print("Time: O(n) | Space: O(n)\n")

    for i, (nums, k, expected) in enumerate(tests, 1):
        result = sol.topKFrequent(nums, k)
        status = "✅" if sorted(result) == sorted(expected) else "❌"
        print(f"  {status} Test {i}: nums={nums}, k={k} → {result}")
