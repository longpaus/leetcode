#!/usr/bin/env python3

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        tmp = []
        for row in matrix:
            tmp.append([])
            for col in row:
                tmp[-1].append(col)

        for rowIndex in range(len(tmp) - 1,-1,-1):
            for colValue,index in zip(tmp[rowIndex],range(len(tmp))):
                print(colValue)
                matrix[index][len(tmp) - 1 - rowIndex] = colValue

        


