class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = defaultdict(int)
        for num in nums:
            freq_table[num] += 1
        sorted_table = sorted(freq_table, key=freq_table.get)
        return sorted_table[-k:]
