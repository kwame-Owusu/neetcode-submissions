class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        pairs = set()
        for u, v in similarPairs:
            pairs.add((u, v))
            pairs.add((v, u))

        for i in range(len(sentence1)):
            w1, w2 = sentence1[i], sentence2[i]
            if w1 != w2 and (w1, w2) not in pairs:
                return False
        
        return True