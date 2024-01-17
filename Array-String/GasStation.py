# 134. Gas Station
"""
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""
"""
Time: O(n)
Space: O(1)
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = 0
        net = 0
        total = 0
        for i in range(len(gas)):
            net += gas[i] - cost[i]
            total += gas[i] - cost[i]        
            if total < 0:
                total = 0
                ans = i+1 
        return -1 if net < 0 else ans
"""
Sample
Input
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
Output
3
"""
