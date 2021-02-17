class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        if len(tree) <= 2: return len(tree)
        
        l = 0
        counter = {}
        output = 0
        for r in range(len(tree)):
            counter[tree[r]] = counter.get(tree[r], 0) + 1
            while len(counter) > 2:
                counter[tree[l]] -= 1
                if counter[tree[l]] == 0:
                    # delete the key tree[l]
                    del counter[tree[l]]
                l += 1
            output = max(output, r-l+1)
        return output
    
                
            
            
        