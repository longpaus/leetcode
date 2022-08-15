class solution:
    def isPalindrome(x: int) -> bool:
        if x < 0:
            return False
        numStr = str(x)
        if len(numStr) % 2 == 0:
            for i in range(len(numStr)/2):
                if numStr[i] != numStr[len(numStr) - 1 - i]:
                    return False
        else:
            for i in range(int((len(numStr) - 1)/2)):
                if numStr[i] != numStr[len(numStr) - 1 - i]:
                    return False