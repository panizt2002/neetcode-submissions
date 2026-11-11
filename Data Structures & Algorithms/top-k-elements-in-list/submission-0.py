class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts= {}

        for i in nums:
            if i in counts:
                counts[i] += 1
            else:
                counts[i] = 1   
        ordered = sorted(counts, key=counts.get, reverse=True)
        E= []
        for i in range (0,k):
            E.append(ordered[i])
        return(E)



        