class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}

        # Iterate through each string
        for s in strs:
            # Sort the string and use it as the key
            sorted_str = ''.join(sorted(s))
            
            # If the sorted version of the string is not in the hashmap, add it
            if sorted_str not in hashmap:
                hashmap[sorted_str] = [s]
            else:
                # If the sorted version exists, append the original string
                hashmap[sorted_str].append(s)

        # Return the list of grouped anagrams
        return list(hashmap.values())

          