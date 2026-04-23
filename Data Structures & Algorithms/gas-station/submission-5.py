class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(gas) < sum(cost):
            return -1

        start_indexes = []

        for (index, value) in enumerate(zip(gas, cost)):
            g, c = value
            if g - c >= 0:
                start_indexes.append(index)

        n = len(gas)

        for index in start_indexes:
            count = 0
            tank = 0
            idx = index
            while count < n:
                idx = idx % n
                tank += gas[idx]
                tank -= cost[idx]
                idx += 1
                if tank < 0:
                    break
                count += 1
            if count == n:
                return index
        
        return -1