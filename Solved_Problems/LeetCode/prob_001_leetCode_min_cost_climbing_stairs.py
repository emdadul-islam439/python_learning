class Solution:
    total_stairs = 0
    stair_cost = dict()
    saved_min_cost = dict()
    
    def findMinCost(self, stair_idx, already_cost = 0) -> int:
        if self.saved_min_cost[stair_idx] != -1:
            return self.saved_min_cost[stair_idx]
        else:
            if stair_idx == self.total_stairs - 1:
                return self.stair_cost[stair_idx]
            elif stair_idx == self.total_stairs - 2:
                return self.stair_cost[stair_idx]
            else:
                self.saved_min_cost[stair_idx] = min(self.findMinCost(stair_idx+1, already_cost + self.stair_cost[stair_idx]), self.findMinCost(stair_idx+2, already_cost + self.stair_cost[stair_idx]))
                return self.saved_min_cost[stair_idx]
            
    
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.total_stairs = len(cost)
        for i in range(self.total_stairs):
            self.stair_cost[i] = cost[i]
            self.saved_min_cost[i] = -1
        
        return min(self.findMinCost(0, 0), self.findMinCost(1, 0))