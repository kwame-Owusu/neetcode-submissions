from collections import Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        count = Counter(students)

        for s in sandwiches:
            if count[s] > 0:
                count[s] -= 1
            else:
                break
        return count[0] + count[1]

