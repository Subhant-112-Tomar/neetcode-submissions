class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h ={}
        for s in strs:
            key = "".join(sorted(s)) # Important
            h[key] = h.get(key, [])
            """
            Multi line bakchodi
            """

            h[key].append(s)

        return list(h.values())