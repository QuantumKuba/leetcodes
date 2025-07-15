from typing import List


class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        n = len(replacements)
        nodes = {key:val for key, val in replacements}

        graph = {node:set() for node in nodes}

        indegree = {node:0 for node in nodes}

        # build the grahp and compute the indegree 

        return ""
    


if __name__ == "__main__":
    replacement = [["A","abc"],["B","def"]]
    text = "%A%_%B%"
    s = Solution()
    s.applySubstitutions(replacement, text)