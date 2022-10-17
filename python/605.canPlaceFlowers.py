class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if len(flowerbed) == 1 and n == 1:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and len(flowerbed) > 1:
                if i == 0 and flowerbed[i + 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
                elif i == len(flowerbed) - 1 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1;
                    n -= 1;
                elif flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
                    flowerbed[i] = 1
                    n -= 1
        return True if n <= 0 else False
