// https://leetcode.com/problems/permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nodes = set(nums)
        
        def _recursive_paths(node: int, path: List[int]) -> List[List[int]]:
            if len(path) == n:
                return [path]
            lst = []
            for neighbor in nodes:
                if neighbor not in path:
                    # concatenate list
                    veje =_recursive_paths(neighbor, path + [neighbor])
                    lst += veje
            return lst
              
        permutations = []
        for node in nodes:
            permutations += _recursive_paths(node, path=[node])
        return permutations
            
        
                            
                            
    
        