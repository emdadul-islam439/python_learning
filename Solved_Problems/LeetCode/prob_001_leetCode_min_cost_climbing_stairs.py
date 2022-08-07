class Solution:
    total_stairs = 0
    stair_cost = dict()
    saved_min_cost = dict()

    def findMinCost(self, stair_idx, already_cost) -> int:
        print(f"stair_idx = {stair_idx}  already_cost = {already_cost} saved_min_cost = {self.saved_min_cost} ")

        if self.saved_min_cost[stair_idx] != -1:
            return self.saved_min_cost[stair_idx]
        else:
            if stair_idx == self.total_stairs - 1:
                return self.stair_cost[stair_idx] + already_cost
            elif stair_idx == self.total_stairs - 2:
                return self.stair_cost[stair_idx] + already_cost
            else:
                self.saved_min_cost[stair_idx] = min(self.findMinCost(stair_idx+1, already_cost + self.stair_cost[stair_idx]), self.findMinCost(stair_idx+2, already_cost + self.stair_cost[stair_idx]))
                return self.saved_min_cost[stair_idx]
            

    def minCostClimbingStairs(self, cost = list()) -> int:
        self.total_stairs = len(cost)
        for i in range(self.total_stairs):
            self.stair_cost[i] = cost[i]
            self.saved_min_cost[i] = -1
        
        return min(self.findMinCost(0, 0), self.findMinCost(1, 0))


cost_arr = list(map(int, input().split()))
print(Solution().minCostClimbingStairs(cost_arr))



# test case 1 = [10,15,20] = 10 15 20
# test case 2 = [1,100,1,1,1,100,1,1,100,1] = 1 100 1 1 1 100 1 1 100 1