class Solution:
    def shipWithinDays(self, weights, D: int) -> int:
        left = 0
        right = sum(weights)
        mid = (left + right) // 2
        def check(ship:int)-> bool:
            if weights[-1] > ship:
                return False
            days = 0
            temp = 0
            for w in weights:
                temp += w
                if temp > ship:
                    temp = w
                    days += 1
            if temp > 0:
                days += 1
            return days <= D
        
        while right - left > 1:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        if right == left:
            return right
        else:
            if check(right):
                return right
            else:
                return left

s = Solution()
s.shipWithinDays([1,2,3,1,1],4)
