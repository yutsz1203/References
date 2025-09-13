# parent array: storing the parent of each node, initially every node is its own parent
# rank array: storing the rank (no. of childrens) of each node
# the idea is to merge node that does not share the same parent, and then update the parent accordingly

# Examples
# Leetcode 323: Number of Connected Components in an Undirected Graph
# Reference: https://youtu.be/8f1XPm4WOUc?si=WkJQDm_OMKwxeH94

def countComponents(self, n: int, edges: list[list[int]]) -> int:
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            
            return res

        def union(n1, n2):    
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            
            return 1
        
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)
        
        return res

# Leetcode 547: Number of Provinces
# Reference: https://leetcode.com/problems/number-of-provinces/solutions/3420785/number-of-provinces

def findCircleNum(self, isConnected: list[list[int]]) -> int:
        n = len(isConnected)
        par = [i for i in range(n)]
        rank = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p2] > rank[p1]:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            
            return 1
            
        provinces = n
        for i in range(n):
            for j in range(i + 1, n):
                 if isConnected[i][j] == 1:
                      provinces -= union(i, j)

        return provinces