class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        if m > n :
            return False

        target = Counter(s1)
        window = Counter(s2[:m])
        if target == window: 
            return True

        for i in range(m, n):
            window[s2[i]] += 1
            left_char = s2[i-m]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char] 
            if target == window: 
                return True
        return False


