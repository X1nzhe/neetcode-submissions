class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets, curr_time = 0, 0
        for p, s in sorted(zip(position, speed), reverse=True):
            travel_time = (target - p) / s
            if travel_time > curr_time:
                fleets += 1
                curr_time = travel_time
        return fleets



