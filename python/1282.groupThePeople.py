#!/usr/bin/env python3
class Solution:
    def groupThePeople(self, groupSizes: list[int]) -> list[list[int]]:
        map = {}
        for i in range(len(groupSizes)):
            if groupSizes[i] not in map:
                map[groupSizes[i]] = [[i]]
            else:
                if len(map[groupSizes[i]][-1]) < groupSizes[i]:
                    map[groupSizes[i]][-1].append(i)
                else:
                    map[groupSizes[i]].append([i])
        ans = []
        for key in map:
            for group in map[key]:
                ans.append(group)
        return ans
                




