class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dic = collections.Counter() # why collections.Counter()
        # dic = {} doesn't work, throw error for line 11
        
        for domain in cpdomains:
            count, domain = domain.split()
            count = int(count)
            frags = domain.split('.')
            for i in range(len(frags)):
                dic['.'.join(frags[i:])] += count
        
        return ['{} {}'.format(v,k) for k,v in dic.items()]