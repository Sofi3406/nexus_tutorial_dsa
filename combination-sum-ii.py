from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()  
        results = []
        
        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                results.append(path)
                return
            if remaining < 0:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, path + [candidates[i]], remaining - candidates[i])
        
        backtrack(0, [], target)
        return results