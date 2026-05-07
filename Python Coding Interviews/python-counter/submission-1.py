from collections import Counter
from collections import defaultdict
from typing import Counter as CounterType

#implementation with default dict
"""res = defaultdict(int)
    joined_strs = s1 + s2

    for char in joined_strs:
        res[char] += 1
    
    return res
"""

def count_chars(s1: str, s2: str) -> CounterType:
    counter = Counter(s1)
    counter.update(s2)
    return counter
  

# do not modify below this line
print(count_chars("hello", "world"))
print(count_chars("hello", "worldhello"))
print(count_chars("areallylongstring", "heyhowisitgoing"))
