class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def eat(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours

        while l <= r:
            mid = l + (r-l) // 2
            curr_h = eat(mid)
            if curr_h <= h:
                r = mid - 1
            else:
                l = mid + 1
        return l

            
                



