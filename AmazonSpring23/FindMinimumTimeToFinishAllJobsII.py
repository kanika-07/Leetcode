# 2323. Find Minimum Time to Finish All Jobs II
"""
You are given two 0-indexed integer arrays jobs and workers of equal length, where jobs[i] is the amount of time needed to complete the ith job, and workers[j] is the amount of time the jth worker can work each day.
Each job should be assigned to exactly one worker, such that each worker completes exactly one job.
Return the minimum number of days needed to complete all the jobs after assignment.
"""
"""
Time: O(sort)
Space: O(sort)
"""
class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        ans = 0
        jobs.sort()
        workers.sort()
        for job, worker in zip(jobs, workers):
            ans = max(ans, (job - 1) // worker + 1)
        return ans
"""
Sample 
Input
jobs = [5,2,4]
workers = [1,7,5]
Output
2
"""
