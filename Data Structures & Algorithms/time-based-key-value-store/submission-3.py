from collections import defaultdict

class TimeMap:

    def __init__(self):
        self._map = defaultdict(list)
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self._map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._map:
            return ""
        
        timestamps = self._map[key]
        l, r = 0, len(timestamps) - 1
        res = ""

        while l <= r:
            mid = (l + r) // 2

            if timestamps[mid][1] <= timestamp:
                res = timestamps[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        
        return res
 