from typing import List

class Solution:
    sep = chr(256)

    def encode(self, strs: List[str]) -> str:
        es = ""
        for st in strs:
            # Accessing via self.sep
            es = es + st + self.sep
        return es

    def decode(self, s: str) -> List[str]:
        ds = []
        st = ""
        for c in s:
            # Accessing via self.sep
            if c != self.sep:
                st += c
            else:
                ds.append(st)
                st = ""
        return ds
