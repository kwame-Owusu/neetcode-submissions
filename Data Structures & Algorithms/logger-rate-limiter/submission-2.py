class Logger:

    def __init__(self):
        self._timestamps = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self._timestamps:
            self._timestamps[message] = timestamp
            self._timestamps[message] += 10
            return True

        if timestamp >= self._timestamps[message]:
            self._timestamps[message] = timestamp
            self._timestamps[message] += 10
            return True
        
        return False
        
        


        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
