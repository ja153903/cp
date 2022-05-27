from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        total_tank = 0
        curr_tank = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total_tank += diff
            curr_tank += diff

            # current tank is the cumulative sum of the trip assuming
            # we started from some past point j
            # we should reset this tank if it dips below 0
            if curr_tank < 0:
                # note that we update start to i + 1 instead of i
                # because if this combination of gas[i] and cost[i]
                # brings the current down to below 0, then it's negative.
                start = i + 1
                curr_tank = 0

        return start if total_tank >= 0 else -1
