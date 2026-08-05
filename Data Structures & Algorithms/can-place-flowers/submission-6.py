class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        m = len(flowerbed)  
        for i in range(m):
            left = (i == 0) or (flowerbed[i-1]==0)
            right = (i==m-1) or (flowerbed[i+1]==0)

            if flowerbed[i] == 0 and left and right:
                flowerbed[i] = 1
                n -= 1

        return n<=0
