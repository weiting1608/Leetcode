class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:

        # Approach 1: using priority queue
        # pq = []
        # for p in points:
        #     dis = p[0]**2 + p[1]**2
        #     heapq.heappush(pq, (dis, p))
        # print(pq)
        # res = []
        # for i in range(K):
        #     res.append(pq[0][1])
        #     heapq.heappop(pq)

        points.sort(key=lambda P: P[0]**2 + P[1]**2)
        return points[:K]
