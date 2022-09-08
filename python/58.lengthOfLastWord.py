#!/usr/bin/env python3


from curses.ascii import isalpha


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        lastWordLen = 0
        for i in range(len(s)):
            if s[i] == ' ':
                count = 0
            elif s[i].isalpha():
                count += 1
                lastWordLen = count

        return lastWordLen

