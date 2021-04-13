def linkParent(node, par= None):
            if node:
                node.par = par
                linkParent(node.left, node)
                linkParent(node.right, node)
                
        linkParent(root)
        
        que = collections.deque([(target, 0)])
        seen = {target}
        
        while que:
            if que[0][1] == K:
                return [node.val for node, step in que]
            
            node, step = que.popleft()
            for nei in (node.left, node.right, node.par):
                if nei not in seen:
                    seen.add(nei)
                    que.append((nei, step+1))
                    
        return []
        